#!/usr/bin/env python
import numpy as np
from PIL import Image

def img_open( name ):
    image = Image.open(name)
    img_array = np.asarray(image)
    img_array.setflags(write=True)
    return img_array

def img_save( img_array, name ):
    Image.fromarray(img_array).save(name)

def img_info( img_array ):
    print img_array
    print img_array.shape

def glitch( img_array ):
    img_array -= 20
    w,h,channels = img_array.shape

    # insert black bands
    for x in xrange(0,h,20):
        img_array[:, x:x+5,:3] = 0

    # swap square slices of image
    """
    for i in xrange(0, w-20, 20):
        for j in xrange(0, h-20, 20):
            img_array[i:i+10,j:j+10,:] = img_array[i+10:i+20, j+10:j+20,:]
    """
    return img_array

def alpha( img_array ):
    alpha_band = img_array[:,:,3]
    return alpha_band

def invert( img_array ):
    img_array[ img_array<255 ] = 0 # make it white
    img_array[ img_array==255 ] = 100 # white to temp
    img_array[ img_array==0 ] = 255 # black to white
    img_array[ img_array==100 ] = 0 # temp to black
    return img_array
    

if __name__ == '__main__':
    orig = img_open( 'test_image2.png' )

