import os

from PIL import Image, ImageFilter

cwd = os.getcwd()
print(cwd)
img = Image.open('../pokedocx/pikachu.jpg')
filtered_imag = img.filter(ImageFilter.BLUR)
filtered_imag1 = img.filter(ImageFilter.SMOOTH)
filtered_imag.save('blur.png', 'png')
filtered_imag1.save('smooth.png', 'png')
# filtered_imag1.show()
crooked = filtered_imag.rotate(90)
crooked.save('crook.png', 'jpeg')
resize = filtered_imag.resize((200, 300))
resize.save('smaller.png', 'png')
print(filtered_imag)
print(img)
print(img.format)
print(img.size)
print(dir(img))


# =========================================================================================================
#
image = Image.open('./Korea.jpg')
image.thumbnail((400, 400))
# thumbnail gives us the aspect ratio
image.save('small-korea.png', 'png')

