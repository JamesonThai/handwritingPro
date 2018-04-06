import numpy as np
import cv2
from PIL import Image, ImageDraw


def output():
    # im=cv2.imread('pure_image/outputDom.png',cv2.IMREAD_GRAYSCALE)
    # 2,3,4,5,6,7,9 doesn't work well commonly picking out 8
    # im=cv2.imread('pure_image/1.png',cv2.COLOR_BGR2GRAY)
    # im[np.where((im == [52, 34, 16, 0]).all(axis = 2))] = [0,33,166]
    # print(type(im))
    # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # new = np.unique(im.reshape(-1, im.shape[2]), axis=0)
    # new=[[[255%j,255%j, j+100] for j in i] for i in im]
    # new=[[[255%j,255%j,j] for j in i] for i in im] alright one
    # dt = np.dtype('f8')
    # new=np.array(new,dtype=dt)
    # new = im[np.where(im == [52, 34, 16, 0])]
    # cv2.imwrite('pure_image/outputFinal.png', new)

    picture = Image.open("pure_image/9.png")
    width,height = picture.size
    print(width, " : ", height)

def get_colors(infile, outfile, numcolors=10, swatchsize=20, resize=150):

    image = Image.open(infile)
    image = image.resize((resize, resize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize*resize)

    # Save colors to file

    pal = Image.new('RGB', (swatchsize*numcolors, swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for count, col in colors:
        draw.rectangle([posx, 0, posx+swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize
        print(col)
    del draw
    pal.save(outfile, "PNG")

if __name__ == '__main__':
    get_colors('pure_image/9.png', 'pure_image/outputDom.png')
    output()
