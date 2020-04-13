import imutils
import cv2

# load image
image = cv2.imread('jp.png')
(h, w, d) = image.shape # extract (height, width, and depth.)

# display img to screen
cv2.imshow('image', image)
cv2.waitKey(0)  # Try to hold windows (important)

# access individual pixel
# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B,G,R) = image[100, 50] #image[height, width]
print("R={}, G={}, B={}".format(R, G, B))

# array slicing and cropping for extract face (Regions of interest)
# image[startY:endY, startX:endX]
roi = image[60:160, 320:420]
cv2.imshow('roi', roi)
cv2.waitKey(0)

# Resizing image (ignore aspect ratio)
resized = cv2.resize(image, (200,200)) # resize img to 200x200 px
cv2.imshow('resized', resized)
cv2.waitKey(0)

# Resizing image (heed aspect ratio)
# resize the width to be 300px
r = 300 / w
dim = (300, int(h * r))
resized1 = cv2.resize(image, dim)
cv2.imshow('resized1', resized1)
cv2.waitKey(0)

# or using imutils module (easier)
resized2 = imutils.resize(image, width=300)
cv2.imshow('resized2', resized2)
cv2.waitKey(0)

# rotating image 45 degree clockwise
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M,(w,h))
cv2.imshow('rotated', rotated)
cv2.waitKey(0)

# rorating image using imutils (easier)
rotated1 = imutils.rotate(image, -45)
cv2.imshow('rotated1', rotated1)
cv2.waitKey(0)

# if you want the image doesnt clipped, you can use rotate_bound func
rotated2 = imutils.rotate_bound(image, 45)
cv2.imshow('rotated2', rotated2)
cv2.waitKey(0)

# smooting an image (blur)
blurred = cv2.GaussianBlur(image, (11,11), 0) # use 11x11 kernel blur
cv2.imshow('blurred', blurred)
cv2.waitKey(0)

# draw on an image 
# it will replace the original img, so we need to make a copy so as 
# not to eliminate the original image

# rectangle
imgcopy = image.copy()
cv2.rectangle(imgcopy, (320, 60), (420, 160), (0,0,255), 2) # pt1(top,left). pt2(bottom,right)
cv2.imshow("Rectangle", imgcopy)
cv2.waitKey(0)

# circle
imgcopy1 = image.copy()
cv2.circle(imgcopy1, (300,150), 20, (255,0,0), -1) #  negative value of thickness make the circle is solid/filled in.
cv2.imshow("Circle", imgcopy1)
cv2.waitKey(0)

# line
# draw a 5px thick red line from x=60,y=20 to x=400,y=200
imgcopy2 = image.copy()
cv2.line(imgcopy2, (60, 20), (400, 200), (0, 255, 0), 5)
cv2.imshow("Line", imgcopy2)
cv2.waitKey(0)

# text
imgcopy3 = image.copy()
cv2.putText(imgcopy3, 'Have Fun!', (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
cv2.imshow("Text", imgcopy3)
cv2.waitKey(0)






