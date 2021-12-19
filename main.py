import cv2


img = cv2.imread('img/tekst1.jpg')
print(type(img))
print(img.shape)

# cv2.imshow('imae', img)
# cv2.waitKey(0)
#
img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
print(pytesseract.image_to_string(img))
print(pytesseract.image_to_string(img_convert))
