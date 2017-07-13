from PIL import Image

img1 = Image.open('2.jpg')
img2 = Image.open('3.jpg')
img3 = Image.open('4.jpg')
r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()
r3, g3, b3 = img3.split()
new_img = Image.merge('RGB', (g1, b1, r1))
new_img.show()
