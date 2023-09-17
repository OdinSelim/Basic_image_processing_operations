import cv2

img = cv2.imread('indir.jpg', 0)

#print(img)

cv2.imshow('image_title', img)
k = cv2.waitKey(5000)

if k == 27: # 27 stands for the ESC button
    cv2.destroyAllWindows()
elif k == ord('s'): # s stands for the s button
    cv2.imwrite('apple_pic.png', img)
    cv2.destroyAllWindows()