from PIL import Image
import numpy as np
from dataclasses import dataclass
from array import array
#class pixels stores intensity values for the 3 color channels red, green,blue
@dataclass
class Pixel:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

#open the input image
img=Image.open('image.png','r')
#create a kernel, a 3X3 matrix, the sum of the elements being 1 // TO CHANGE IT INTO GAUSSIAN DISTRIBUTION
kernel=np.ones((3,3),dtype=float)/9;
#in pixelValues, we gather information about every pixel of the input image
pixelValues=list(img.getdata())
#added manually for the moment, to be made universal
width=256
height=256

pixelArray=list()
#for every pixel, we have a list [i1, i2,i3,i4], of which we keep i1,i2,and i4
for x in pixelValues:
    k=0
    for i in x:
        if k==0:
            r=i
        if k==1:
            g=i
        if k==3:
            b=i
        k+=1
    p=Pixel(r,g,b)  # create a Pixel-type object using the 3 instances r,g,b
    pixelArray.append(p) #and create an array of Pixel-type objects
shape=(width,height)
x=np.asarray(pixelArray)
final=x.reshape(shape) #reshape the array from above to a width*height matrix
red=list()  #a list of values for each color channel
green=list()
blue=list()
for i in range(width):  #the gaussian blur happens here: to be described later
    for j in range(height):
        if i!=0 and j!=0 and i!=width and j!=height:
            if i!=1 and j!=1 and i!=width-1 and j!=height-1:
                weight=kernel[0][0]*final[i-1][j-1].r+kernel[0][1]*final[i-1][j].r+kernel[0][2]*final[i-1][j+1].r+kernel[1][0]*final[i][j-1].r+kernel[1][1]*final[i][j].r+kernel[1][2]*final[i][j+1].r+kernel[2][0]*final[i+1][j-1].r +kernel[2][1]*final[i+1][j].r+kernel[2][2]*final[i+1][j+1].r
                weight/=9
                red.append(weight)

                weight = kernel[0][0] * final[i - 1][j - 1].g + kernel[0][1] * final[i - 1][j].g + kernel[0][2] * final[i - 1][j + 1].g + kernel[1][0] * final[i][j - 1].g + kernel[1][1] * final[i][j].g + kernel[1][2] * final[i][j + 1].g + kernel[2][0] * final[i + 1][j - 1].g + kernel[2][1] * final[i + 1][j].g + kernel[2][2] * final[i + 1][j + 1].g
                weight/=9
                green.append(weight)

                weight = kernel[0][0] * final[i - 1][j - 1].b + kernel[0][1] * final[i - 1][j].b + kernel[0][2] * final[i - 1][j + 1].b + kernel[1][0] * final[i][j - 1].b + kernel[1][1] * final[i][j].b + kernel[1][2] * final[i][j + 1].b + kernel[2][0] * final[i + 1][j - 1].b + kernel[2][1] * final[i + 1][j].b + kernel[2][2] * final[i + 1][j + 1].b
                weight/=9
                blue.append(weight)
            else:
                red.append(final[i][j].r)
                green.append(final[i][j].g)
                blue.append(final[i][j].b)
        else:
            red.append(final[i][j].r)
            green.append(final[i][j].g)
            blue.append(final[i][j].b)




#shape=(width,height)
#pixelValues.reshape(shape)
#in list pixelValues, we store groups of 4 elements for each pixel of the picture (i1,i2,i3,i4)
#where
#array=np.array(int)
#for x in pixelValues:
 #   sum=0
  #  for i in x:
   #     sum+=i
    #array.__add__(sum)
#shape=(width,height)
#array.reshape(shape)
#print(array)

#toPrint=list()
#for i in final:
#    for j in i:
 #       toPrint.append([j.r,j.g,j.b])


ared=np.array(red,float)
agreen=np.array(green,float)
ablue=np.array(blue,float)
for a in ared:
    a=(a*255)/np.max(ared)
for b in agreen:
    b=(b*255)/np.max(agreen)
for c in ablue:
    c=(c*255)/np.max(ablue)
#print(len(ared))
#here 3 images (correspondent to the three color channels) are being created, after having been "blurred"
bred=ared.reshape(width,height)
bgreen=agreen.reshape(width,height)
bblue=ablue.reshape(width,height)
imr=Image.fromarray(np.uint8(bred))
img=Image.fromarray(np.uint8(bgreen))
imb=Image.fromarray(np.uint8(bblue))
merged=Image.merge("RGB",(imr,img,imb))  #the 3 images are merged into an only one
merged.save('newImage.png') #and saved locally







