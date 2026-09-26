import numpy as np
def svd_2x2_singular_values(A):
    B=A.T@A
    a=B[0,0]
    b=B[0,1]
    d=B[1,1]
    t=0.5*np.arctan2(2*b,a-d)
    c=np.cos(t)
    s=np.sin(t)
    V=np.array([[c,-s],[s,c]])
    D=V.T@B@V
    S=np.sqrt(np.maximum(np.diag(D),0))
    idx=np.argsort(S)[::-1]
    S=S[idx]
    V=V[:,idx]
    U=np.zeros((2,2))
    for i in range(2):
        if S[i]>1e-10:
            U[:,i]=(A@V[:,i])/S[i]
    return U,S,V.T