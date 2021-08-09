from PIL import Image

def detector(path):

    img = Image.open(path)
    px = img.load()
    width, height = img.size
    colors = []
    for x in range(width):
        for y in range(height):
            if px[x,y] not in colors:
                print(px[x,y])
                colors.append(px[x,y])
    return colors



colors_list = detector(r"C:\Users\Flavio\Pictures\logo.png")

colors_list_2 = []
for row in colors_list:
    colors_list_2.append(f'rgb{row}')

print(colors_list_2)
