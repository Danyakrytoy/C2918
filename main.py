import cv2
from PIL import Image

image_path = "cat.png"

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)

cat_face = cat_face_cascade.detectMultiScale(image)

cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open("glasses.png")
hat = Image.open("hat.png")
hat = hat.convert("RGBA")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for(x, y, w, h) in cat_face:
    hat = hat.resize((w, int(h/3)))
    cat.paste(hat, (x, int(y + h - 250)), hat)
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h / 4)), glasses)
    cat.save("cat_with_glasses_hat.png")
    cat_with_glasses_hat = cv2.imread("cat_with_glasses_hat.png")
    cv2.imshow("Cat_with_glasses_hat", cat_with_glasses_hat)

