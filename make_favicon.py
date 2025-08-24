from PIL import Image, ImageDraw

img = Image.new("RGBA", (64,64), (53,115,246,255))  # blue background
d = ImageDraw.Draw(img)
d.ellipse((4,4,60,60), outline=(255,255,255,200), width=3)
d.text((16,18), "UA", fill=(255,255,255,255))
img.save("static/favicon.ico", format="ICO")
print("saved -> static/favicon.ico")




