from PIL import Image
imagen = Image.open("python.jpg")
imagen.thumbnail((100,100))
imagen.save("pillow03.png")