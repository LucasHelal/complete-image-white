from scipy.misc import imread, imsave
import numpy as np
import glob
import os


base_dir = '/Users/lucas/Desktop/mestrado/Bases - Lucas/Base_BFL_CVL_QUWI/CVL_Textura/*'

for path in glob.iglob(base_dir, recursive=True):

  filename = os.path.basename(path)
 

  old_image = imread(path)
  old_image = old_image[:256, :2304]

  new_image = np.ones((256, 2304), np.uint8)
  new_image = new_image*255
  new_image[:old_image.shape[0], :old_image.shape[1]] = old_image

  imsave('CVL-NEW/' + filename, new_image)