import os

import cv2

image_path = os.path.join('.', 'data', 'bird.jpg')
#reading from path ./data with name bird.jpg
# ./ path is current program dirrectory

# Converting image "bird.jpg" to numpy array and storing that array to object "img"
img = cv2.imread(image_path)

# number of bands denote number of colour palets used. Ex color images have 3, B&W has 1
# every pixel in a image/frame is associated with set of number(s) with (number of bands) elements.
# These number signify the intensity of color in the image and are between 0 to 255 (for 8 bit images). for binary images it 0,1 or 0,255 , 0 for black an 1 white
# prints (width,hieght,number of color bands)
print(img.shape)

cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img) 
# writing to path ./data with name bird_out.jpg

# visualize image
cv2.imshow('image', img) #new window called "image" pops up
cv2.waitKey(0)        # 0 denote the number of miliseconds window is shown, 0 means forever
