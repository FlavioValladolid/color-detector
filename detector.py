from PIL import Image

def detector(path):

    img = Image.open(path)
    px = img.load()
    width, height = img.size
    pixel_color = ()
    colors = []
    colors_2 = []
    for x in range(width):
        for y in range(height):
            if px[x,y] not in colors:
                print(round(x/width*100,2),'%')
                pixel_color = px[x,y]
                colors.append(pixel_color)
                colors_2.append(f'rgb{pixel_color}')
    
    return colors, colors_2



colors_list, colors_list_rgb = detector(r"C:\Users\Flavio\Desktop\a.jpg")

print(colors_list)

with open('file.txt','w') as f:
    for color in colors_list_rgb:
        f.write(color)
        f.write('\n')