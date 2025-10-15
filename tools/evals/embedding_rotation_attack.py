#!/usr/bin/env python3
"""Embedding-space rotation attack finder.

Inputs:
  --ref ref.npy  --test test.npy
Outputs JSON with a rotation angle that evades shallow stats yet trips deep drift.
"""
import argparse, numpy as np, json
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist

def mmd_rbf(x, y, gamma=1.0):
    def ker(a,b): 
        d2 = cdist(a,b,'sqeuclidean')
        return np.exp(-gamma*d2)
    n, m = len(x), len(y)
    Kxx = ker(x,x); np.fill_diagonal(Kxx,0)
    Kyy = ker(y,y); np.fill_diagonal(Kyy,0)
    Kxy = ker(x,y)
    return Kxx.sum()/(n*(n-1)) + Kyy.sum()/(m*(m-1)) - 2*Kxy.mean()

def subspace_angle_deg(x, y, k=10):
    p1 = PCA(n_components=min(k, x.shape[1])).fit(x).components_.T
    p2 = PCA(n_components=min(k, y.shape[1])).fit(y).components_.T
    s = np.linalg.svd(p1.T @ p2, full_matrices=False)[1]
    s = np.clip(s, -1, 1)
    ang = np.arccos(s).max()
    return float(np.degrees(ang))

def shallow_ok(x, y, tol=1e-2):
    md = np.linalg.norm(x.mean(0) - y.mean(0))
    vd = np.linalg.norm(x.var(0) - y.var(0))
    return md < tol and vd < tol

def rotate(x, theta_deg):
    pca = PCA(n_components=x.shape[1]).fit(x)
    z = x @ pca.components_.T
    t = np.radians(theta_deg)
    R = np.eye(z.shape[1])
    R[:2,:2] = [[np.cos(t), -np.sin(t)],[np.sin(t), np.cos(t)]]
    zr = z @ R
    return zr @ pca.components_

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', required=True)
    ap.add_argument('--test', required=True)
    ap.add_argument('--gamma', type=float, default=1.0)
    args = ap.parse_args()
    ref = np.load(args.ref); tst = np.load(args.test)

    best = None
    for theta in range(0, 91, 5):
        rt = rotate(tst, theta)
        if shallow_ok(ref, rt):
            mmd = float(mmd_rbf(ref, rt, gamma=args.gamma))
            angle = subspace_angle_deg(ref, rt)
            if mmd > 0.01 or angle > 30:
                best = {'theta_deg': theta, 'mmd': mmd, 'angle_deg': angle}
                break
    print(json.dumps({'attack': best}, indent=2))

if __name__ == '__main__':
    main()
