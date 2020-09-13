     #Histogram based Segmentation

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from scipy import ndimage as nd

img = img_as_float(io.imread("rand_walk.png"))

sigma_est = np.mean(estimate_sigma(img,multichannel=True))

denoise = denoise_n1_means(img, h=1.15*sigma_est,fast_mode=True,patch_size=5,patch_distance=3,multichannel=true)

denoise_ubyte=img_as_ubyte(denoise)

seg1 = (denoise_ubyte >= 55)
seg2=(denoise_ubyte>55) &(denoise_ubyte<=110)
seg3=(denoise_ubyte>110) & (denoise_ubye<=210)
seg4=(denoise_ubyte>210)

all_seg=np.zeros((denoise_ubyte.shape[0],denoise_ubyte.shape[1],3))

all_seg[seg1]={1,0,0}
all_seg[seg2]={0,1,0}
all_seg[seg1]={0,0,1}
all_seg[seg2]={1,1,0}


seg1_open =nd.binary_opening(seg1,np.ones((3,3)))
seg1_close =nd.binary_closing(seg1_open,np.ones((3,3)))
seg2_open =nd.binary_opening(seg2,np.ones((3,3)))
seg2_close =nd.binary_closing(seg2_open,np.ones((3,3)))
seg3_open =nd.binary_opening(seg3,np.ones((3,3)))
seg3_close =nd.binary_closing(seg3_open,np.ones((3,3)))
seg4_open =nd.binary_opening(seg4,np.ones((3,3)))
seg4_close =nd.binary_closing(seg4_open,np.ones((3,3)))

all_seg_cleaned=np.zeros(denoise_ubyte.shape[0],denoise_ubyte.shape[1],3)
all_seg_cleaned[seg1_close]={1,0,0}
all_seg_cleaned[seg2_close]={0,1,0}
all_seg_cleaned[seg1_close]={0,0,1}
all_seg_cleaned[seg2_close]={1,1,0}

ply.imshow(all_seg_cleaned)

                #RANDOM WALKER

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma
from scipy import ndimage as nd
from skimage import exposure

img = img_as_float(io.imread("rand_walk.png"))

sigma_est = np.mean(estimate_sigma(noisy, multichannel=True))

patch_kw = dict(patch_size=5,      
                patch_distance=6, 
                multichannel=True)

# slow algorithm
denoise_img = denoise_nl_means(noisy, h=1.15 * sigma_est, fast_mode=True,
                           **patch_kw)
eq_img=exposure.equalize_adapthist(denoise_img)

markers=np.zeros(img.shape,dtype=np.uint)

markers[(eq_img<0.6) & (eq_img>0.3)] =1
markers[(eq_img>0.8) & (eq_img<0.99)] =2

from skimage.segmentation import random_walker
labels=random_walker(eq_img,markers,beta=10,mode='bf')

segm1=(labels==1)
segm2=(labels==2)

all_seg=np.zeros(eq_img.shape[0],eq_img.shape[1],3)

all_seg[segm1]={1,0,0}
all_seg[segm2]={0,1,0}

plt.imshow(all_seg)

plt.hist(img.flat,bins=100,range=(0,1))

		#Denoising

import numpy as np
import cv2
img=cv2.imread("blur1.jpg",1)
kernel=np.ones((3,3),np.float32)/9

filt_2D=cv2.filter2D(img ,-1 ,kernel)
cv2.imshow("Filtered",g_filt_2D)
cv2.waitKey()
cv2.destroyAllWindows()

		#Blruing

import numpy as np
import cv2
img=cv2.imread("blur1.jpg",1)
kernel=np.ones((3,3),np.float32)/9

filt_2D=cv2.filter2D(img ,-1 ,kernel)
bl = cv2.blur(img,(3,3))
g_blur= cv2.GaussianBlur(img , (5,5),0)

cv2.imshow("Gaussian Filtered",g_blur)
cv2.waitKey()
cv2.destroyAllWindows()from PIL import Image
import numpy as np
import cv2
img=cv2.imread("blur1.jpg",1)
kernel=np.ones((3,3),np.float32)/9

filt_2D=cv2.filter2D(img ,-1 ,kernel)
bl = cv2.blur(img,(3,3))
g_blur= cv2.GaussianBlur(img , (5,5),0)
m_filt=cv2.medianBlur(img ,3)

cv2.imshow("Filtered",m_filt)
cv2.waitKey()
cv2.destroyAllWindows()


		#Thresholding

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread("blur1.jpg",0)

kernel=np.ones((3,3),np.uint8)
ret , th = cv2.threshold(img , 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
er=cv2.erode(img,kernel,iterations=1)
di=cv2.dilate(er,kernel,iterations=1)

#plt.hist(img.flat , bins=100 ,range=(0,255))

cv2.imshow("Original ",img)
cv2.imshow("erosion",er)
cv2.imshow("Dilated",di)
cv2.waitKey()
cv2.destroyAllWindows()

		#Histogram Equilisation

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread("testimg.jpg",0)

eqimg=cv2.equalizeHist(img)
clahe=cv2.createCLAHE(clipLimit=2.0 , tileGridSize=(5,5))
cl_img=clahe.apply(img)
plt.hist(cl_img.flat , bins=100 ,range=(0,255))
ret,thresh1=cv2.threshold(cl_img,190,150,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(cl_img,190,255,cv2.THRESH_BINARY_INV)

ret2,thresh3=cv2.threshold(cl_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("T1",thresh1)
cv2.imshow("T3",thresh3)
cv2.imshow("clache image",cl_img)
