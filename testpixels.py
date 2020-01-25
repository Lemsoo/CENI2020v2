from PIL import Image
im = Image.open("lien_de_l'image").convert('L')
couleur = 66 # code rgb
pixels = []
x, y = im.size
for i in range(x):
    for j in range(y):
        if im.getpixel((i, j)) == couleur:
            pixels.append((i, j))
for pixel in pixels:
    print (pixel)
