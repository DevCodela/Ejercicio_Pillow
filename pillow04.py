from PIL import Image, ImageFilter
imagen = Image.open("python.jpg")
imagen = imagen.filter(ImageFilter.BLUR)
imagen.save("pillow04.png")