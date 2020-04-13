import imutils
import cv2
import argparse

# count the nuber of tetris block (tetris_block.png)

# Along the way we’ll be:

# Learning how to convert images to grayscale with OpenCV
# Performing edge detection
# Thresholding a grayscale image
# Finding, counting, and drawing contours
# Conducting erosion and dilation
# Masking an image

# create a cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to input image')
agrs = vars(ap.parse_args())

# load image
image = cv2.imread(agrs['image'])
cv2.imshow('Image', image)
cv2.waitKey(0)

# convert image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)

# edge detection

# Using the popular Canny algorithm (developed by John F. Canny in 1986), we can find the edges in the image.
edged = cv2.Canny(gray, 30,150)
cv2.imshow('Edges', edged)
cv2.waitKey(0)

# threshold
# image greater than 225 and setting them to 0 (black) which corresponds to the background of the image
# Setting pixel vales less than 225 to 255 (white) which corresponds to the foreground of the image (i.e., the Tetris blocks themselves).
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)

# draw outline

# find contours of the foreground objects in the thresh img
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
        
# draw text based on object found
text = '{} object found'.format(len(cnts))
cv2.putText(output, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

cv2.imshow('Countours', output)
cv2.waitKey(0)

# erosions and dilations (mengecilkan dan membesarkan)
# based on number of iterations given
mask = thresh.copy()

# erosion
mask1 = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask1)
cv2.waitKey(0)

# dilataions
mask2 = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask2)
cv2.waitKey(0)

# Masking and bitwise operations
# Masking akan menghilangkan bagian dari gambar yang kita tidak inginkan
mask = thresh.copy()
masking = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masking", masking)
cv2.waitKey(0)