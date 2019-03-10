"""
Resize each image to a given width, or a given height, and keep the other dimension proportional to the original. Requires Pillow.
"""
import os
from PIL import Image

# change dir names to match yours
start_dir = '/Users/username/dirname1/dirname2/dirname3/originals/'
end_dir = '/Users/username/dirname1/dirname2/dirname3/resized/'

# change to 'w' for width or 'h' for height
dimension = 'w'
# change to the number of pixels you need for that dimension
base = 300

# this takes each image file in the starting folder, resizes it, and
# writes it to the ending folder you specified, with the same filename
for file in os.listdir(start_dir):
    # check if base is set
    if type(base) is not 'int' or base <= 16:
        print("Set the base to a sensible number, please!")
        break
    im = Image.open(start_dir + file)
    # check if dimension is w or h or not set
    if dimension == 'w':
        wpercent = (base / float(im.size[0]))
        hsize = int((float(im.size[1]) * float(wpercent)))
        im2 = im.resize((base, hsize), Image.ANTIALIAS)
    elif dimension == 'h':
        hpercent = (base / float(im.size[1]))
        wsize = int((float(im.size[0]) * float(hpercent)))
        im2 = im.resize((wsize, base), Image.ANTIALIAS)
    else:
        print("Set dimension to either 'w' or 'h' please!")
        break
    # save one resized image and close the original file
    im2.save(end_dir + file)
    im.close()
