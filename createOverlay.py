from PIL import Image

width, height = 3000, 3000

img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
imgin = Image.open('merged.png').convert('RGBA')
pixels = img.load()
pixelsin = imgin.load()
for y in range(height):
    for x in range(width):
        if x%3 == 1 and y%3==1:
            pixels[x, y] = pixelsin[x,y]

img.save('overlay.png')
