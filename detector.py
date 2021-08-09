from PIL import Image
from pd2image import convert_from_path

def detector(path):
    img = Image.open(path)
    px = img.load()
    width, height = img.size
    colors = []
    for x in range(width):
        for y in range(height):
            if px[x,y] not in colors:
                colors.append(px[x,y])
    return print(colors)


detector(r"C:\Users\Flavio\Documents\Orders - Printing and Converting-20210726T191931Z-001\Orders - Printing and Converting\4755 Ahold 3ct-22oz Rom Hts Zip\15298 Ahold 3ct Rom.pdf")