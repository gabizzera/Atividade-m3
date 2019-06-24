import cv2
img = cv2.imread("bob_esponja.jpg"   , cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
enhance = cv2.detailEnhance(img)
cv2.imshow('BOB', enhance)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("bob_result.jpg", img)
