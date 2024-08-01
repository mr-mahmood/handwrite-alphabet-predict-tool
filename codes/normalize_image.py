from PIL import Image, ImageFilter, ImageOps
import numpy as np
# My own codes import
import directory

def reduce_noise(img):
    #Apply filters to reduce noise in the image.

    # Apply a median filter to reduce noise
    filtered_img = img.filter(ImageFilter.MedianFilter(size=3))

    return filtered_img

def __normal(img_get):
    
    if img_get == 0 :
        
        address = directory.add()
        img = Image.open(address + directory.alphabet_temp_img)
            
        # Convert the image to grayscale so it would be only white and black and color between this two
        img = img.convert('L')
        a = img.size
        img = reduce_noise(img)
        
    else:
        
        img = img_get
        # Convert the image to grayscale so it would be only white and black and color between this two
        img = img.convert('L')
        img = reduce_noise(img)

    # Normalize the pixel values from 0(black) to 1(white) base on color, after that flatten it to be 1D
    #divide by 255 because grayscale image is range from 0(black) to 255(white)
    
    img = np.array(img) / 255.0 #0(black) to 1(white)
    img_flattened = img.flatten()
    img_flattened = img_flattened.tolist()
    return img_flattened
    

def main(img_get):
    a = __normal(img_get)
    return a
