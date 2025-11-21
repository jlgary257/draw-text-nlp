from PIL import Image
import numpy as np
import pytesseract

filename = 'image.png'

img1 = np.array(Image.open(filename))
if not filename:
    print("No file")
else:
    print("File present")
    text = pytesseract.image_to_string(img1)
    print('Result: ', text)