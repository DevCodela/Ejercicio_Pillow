from PIL import Image
imagen = Image.open("python.jpg")
imagen = imagen.rotate(45)
imagen = imagen.resize( (500,500) )
imagen.save("pillow05.png")