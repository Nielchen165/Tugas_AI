#----------------BG Coba-coba------------------#
"""
import cv2 as cv 
import numpy as np 
 
def rescale(frame, scale=0.45): 
    dimension = (int(frame.shape[1]*scale),int(frame.shape[0]*scale)) 
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA)  
 
#Untuk memilih data image yang akan dibaca
imageBase = cv.imread('Dataset/Kemangi/001.jpg') 

#Untuk print info image dalam array 
print(imageBase)

#Untuk menampilkan resolusi image h x w 
print(imageBase.shape)
 
#Untuk crop image
im_crop = imageBase[400:300,1200:900] 
cv.imshow('crop',im_crop) 
cv.waitKey(0) 
print(im_crop.shape) 

#Untuk mengcopy image dan edit contras
imageCopy = imageBase.copy() 
editContrast = cv.addWeighted(imageCopy,2,np.zeros(imageCopy.shape,imageCopy.dtype),0,-100) 
renderEdge = cv.Canny(editContrast, 100,200) 

#Untuk menampilkan hasil image
cv.imshow('Kemangi', rescale(imageBase)) 
# cv.imshow('Kemangi copy', rescale(editContrast)) 
cv.imshow('Kemangi copy', rescale(renderEdge)) 
cv.waitKey(0) 
cv.destroyAllWindows()
"""

#----------------BG Eksekusi------------------#

import cv2 as cv
import numpy as np
import glob

def rescale(frame, scale=0.45):
    dimension = (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA) 

imdir = 'Dataset/Kemangi/'
ext = ['jpg']
files = []
[files.extend(glob.glob(imdir+'*.'+e))for e in ext]
images = [cv.imread(file)for file in files]
i = 1
for img in images :
    if (i <= 50):
        print(img)#print image information as array
        print(img.shape)#show image resolution h x w
        imageCopy = img.copy()
        editContrast = cv.addWeighted(imageCopy,2.5,np.zeros(imageCopy.shape,imageCopy.dtype),0,-100)
        im_gray = cv.cvtColor(imageCopy,cv.COLOR_BGR2GRAY)
        renderEdge = cv.Canny(im_gray, 100,200)
        """
        cv.imshow(str(i), rescale(img))
        # cv.imshow('nangka copy', rescale(editContrast))
        cv.imshow(str(i) + ' edge', rescale(renderEdge))
        """
        im_name = "Dataset/Kemangi_edge/" + str(i) + ".jpg"
        cv.imwrite(im_name, renderEdge)
    else:
        break     
    # im_kon = cv.addWeighted(img,1.5,np.zeros(img.shape,img.dtype),0,-100)
    # im_name = "dataset/pepaya_kon/" + str(i) + ".png"
    # cv.imwrite(im_name, im_kon)
    i+=1
cv.waitKey(0)
cv.destroyAllWindows()  