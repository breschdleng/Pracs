import numpy as np

def conv(img, k, s):
    sx = len(img[0])
    sy = len(img[1])
    kerx = len(k[0])
    kery = len(k[1])

    conv = np.zeros([int(((sx-kerx)/s+1)) ,int(((sy-kery)/s+1))])

    cx = 0
    cy = 0
    for  i in range(0,sx,s):
        if (i >= 0 and i < int(((sx - kerx)/s + 1))):
            cy = 0
            for j in range(0,sy,s):
                if(j >= 0 and j < int(((sy - kery/s) + 1))):
                    print(cx,cy)
                    for kx in range(kerx):
                        for ky in range(kery):

                            conv[cx][cy] += img[i+kx][j+ky]*k[kx][ky]
                    cy +=1
            cx +=1
    return conv

if __name__ == '__main__':

       img = np.round(10*np.random.rand(9,9))
       k = np.round(np.random.rand(3,3))
       print(img,k)
       result = conv(img,k,2)
       print("conv size", result.size)
       print("conv result", result)
