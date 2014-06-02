from PIL import Image
imagen = Image.open("python.jpg")
tamanio = imagen.size
punto_x = imagen.size[0] / 3
punto_y = imagen.size[1] / 3
coordenada = (punto_x, punto_y)
color_pixel = imagen.getpixel(coordenada)
print color_pixel
nueva = Image.new("RGB", tamanio, color_pixel)
nueva.save("pillow06.png")
