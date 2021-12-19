import cv2


imgg = cv2.imread('img/tekst1.jpg')
print(type(imgg))
print(imgg.shape)

# cv2.imshow('imae', imgg)
# cv2.waitKey(0)
#
img_convert = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img_convert', img_convert)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'H:\Program Files\Tesseract-OCR\tesseract'

# print(pytesseract.image_to_string(Image.open('img/tekst1.jpg')))

# print(pytesseract.image_to_string(imgg))
# print(pytesseract.image_to_string(img_convert))

converted_img1 = cv2.threshold(cv2.GaussianBlur(img_convert, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
converted_img2 = cv2.threshold(cv2.bilateralFilter(img_convert, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
converted_img3 = cv2.threshold(cv2.medianBlur(img_convert, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
converted_img4 = cv2.adaptiveThreshold(cv2.GaussianBlur(img_convert, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
converted_img5 = cv2.adaptiveThreshold(cv2.bilateralFilter(img_convert, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
converted_img6 = cv2.adaptiveThreshold(cv2.medianBlur(img_convert, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

cv2.imshow('test4', converted_img1)
cv2.waitKey(0)
cv2.imshow('test4', converted_img2)
cv2.waitKey(0)
cv2.imshow('test4', converted_img3)
cv2.waitKey(0)
cv2.imshow('test4', converted_img4)
cv2.waitKey(0)
cv2.imshow('test4', converted_img5)
cv2.waitKey(0)
cv2.imshow('test4', converted_img6)
cv2.waitKey(0)

cv2.destroyAllWindows()

# print(pytesseract.image_to_string(converted_img1))
# print(pytesseract.image_to_string(converted_img2))
# print(pytesseract.image_to_string(converted_img3))
print(pytesseract.image_to_string(converted_img4))
print(pytesseract.image_to_string(converted_img5))
print(pytesseract.image_to_string(converted_img6))
