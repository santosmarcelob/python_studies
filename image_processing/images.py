from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_image = img.convert('L')

filtered_image.save("sharpen.png", 'png')

filtered_image.show()