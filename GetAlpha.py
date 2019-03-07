
from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image

image=Image.open('plot_data2.jpg')
image = image.convert('RGBA')	
# # First create the image with alpha channel
# rgba = cv2.cvtColor(rgb_data, cv2.COLOR_RGB2RGBA)

# # Then assign the mask to the last channel of the image
# rgba[:, :, 3] = alpha_data

data = np.array(image)
im2 = Image.fromarray(data)
im2.save("plot_data2(rgba).png")