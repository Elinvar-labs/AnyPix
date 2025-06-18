from PIL import Image
from itertools import chain
from math import sqrt
class Engine:
    def __init__(self):
        pass
    
    def pixelize(self, filename, outname, palette_name="NES", power=8, colors=256):
        self.filename = filename
        self.outname = outname
        with Image.open(self.filename) as self.img:
            self.img.load()
        self.img = self.img.resize((self.img.width//power, self.img.height//power), Image.NEAREST)
        # self.img = self.img.resize((self.img.width//16, self.img.height//16), Image.NEAREST)
        palette = self.get_palette(palette_name)
        self.img = self.img.quantize(colors=colors, method=None, kmeans=0)
        self.img = self.set_palette(palette, self.img)
        # self.img = self.img.resize((self.img.width*16, self.img.height*16), Image.NEAREST)
        self.img = self.img.resize((self.img.width*power, self.img.height*power), Image.NEAREST)
        if isinstance(self.img, Image.Image):
            self.img.show()
        self.img.save(outname)
        
    def choose_closest_color(self, rgb, pal):
        r, g, b = rgb
        color_diffs = []
        for color in pal:
            cr, cg, cb = color
            color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
            color_diffs.append((color_diff, color))
        return min(color_diffs)[1]    
        
    def set_palette(self, palette, img):
        img = self.img.convert('RGB')

        width = img.size[0] 
        height = img.size[1]
        progress = 0
        for i in range(0,width):
            for j in range(0,height):
                progress += 1                    
                data = img.getpixel((i,j))
                closest_color = self.choose_closest_color(data, palette)                                    
                img.putpixel((i,j), tuple(closest_color))
                self.print_progress("Progress::"+self.toFixed(progress/(width*height)*100, 2))
        print("\nDone.\n")
        return img    
                    
    def get_palette(self, name):
        if name == "NES":
            with Image.open("palettes/NES.png") as nes:
                nes.load()
            print("loading nes palette")
            pal = nes.getcolors()
            output_pal = []
            temp = []
            for i in pal:
                for j in i:
                    temp = []
                    if type(j) is tuple:
                        for k in j:
                            temp.append(k)
                output_pal.append(temp)   
            output_pal.sort()
            return output_pal
        if name == "SEGA":
            with Image.open("palettes/SEGA.png") as sega:
                sega.load()
            print("loading sega palette")
            pal = sega.getcolors()
            output_pal = []
            temp = []
            for i in pal:
                for j in i:
                    temp = []
                    if type(j) is tuple:
                        for k in j:
                            temp.append(k)
                output_pal.append(temp)
            output_pal.sort() 
            return output_pal
        
    def toFixed(self, numObj, digits=0):
        return f"{numObj:.{digits}f}"
    
    def print_progress(self, percents):
        print(f"\r{percents}%", end="", flush=True)
