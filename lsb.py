from PIL import Image
i=0
data = "0110001101111001011000100011001101110010011001110011010001100001011000100111001101111011001101000011001101101110011100110011000101100011011100110101111100110001011110100101111100110011011110100111100101111101"
with Image.open("source.png") as img:
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0,3):
                if(i < len(data)):
                    pixel[n] = pixel[n] & ~1 | int(data[i])
                    i+=1
            img.putpixel((x,y), tuple(pixel))
    img.save("chall.png", "PNG")
#https://pastebin.com/GtEzr2xY