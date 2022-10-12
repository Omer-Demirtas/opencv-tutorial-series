import cv2

img = cv2.imread("../images/image.jpg")

# Get number of pixel horizontally and vertically.
(height, width) = img.shape[:2]

# Specify the size of image along with interploation methods.
# cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
# is used for zooming.
scale = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

#cv2.imshow("resize", res)


M = cv2.getRotationMatrix2D((width / 2, height / 2), 10, 1)
res = cv2.warpAffine(img, M, (width, height))

cv2.imshow("image", img)
cv2.imshow("res", res)
cv2.imshow("Scale", scale)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
