import colorsys
from PIL import Image
from PIL import Image, ImageDraw

from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

img.show()
# width = 500
# height = 500
#
# img = Image.new('RGB', (width, height))
#
# draw = ImageDraw.Draw(img)
#
#
# # the origin (0, 0) is at the top-left corner
#
# draw.rectangle(((0, 0), (width, height)), fill="white")
#
# # draw a rectangle from x0, y0 to x1, y1
# # draw.rectangle(((100, 100), (300, 300)), fill="lightblue")
#
# # draw a line from x0, y0, x1, y1
# # using the color pink
# color = (2148, 24, 230)  # purp
# draw.line((250, 150, 250, 350), fill=color)
# draw.line((250, 350, 175, 450 ), fill=color)
# draw.line((250, 350, 325, 450), fill=color)
# draw.line((150, 175, 350, 175), fill=color)
#
# circle_x = width/2
# circle_y = height/2
# circle_radius = 50
# draw.ellipse((circle_x-circle_radius, 50, circle_x+circle_radius, 150), fill=color)
#
# circle_x = width/2
# circle_y = height/2
# circle_radius = 20
# draw.ellipse((230, 80, 240, 90), fill='black')
#
# circle_x = width/2
# circle_y = height/2
# circle_radius = 20
# draw.ellipse((260, 80, 270, 90), fill='black')
#
# img.show()

#
# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         # your code here
#
#         # y = round(0.299*r + 0.587*g + 0.114*b)
#         # colorsys uses colors in the range [0, 1]
#
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
#
#         h += .5
#         if h > 1:
#             h -= 1
#
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#
#         # convert back to [0, 255]
#
#         r = int(r * 255)
#         g = int(g * 255)
#         b = int(b * 255)
#
#         pixels[i, j] = (r, g, b)
#
# img.show()