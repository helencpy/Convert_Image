#!/usr/bin/env python3
import os
from PIL import Image

directory = 'images'

# iterate over files in
# that directory
for filename in os.listdir(directory):
  f = os.path.join(directory, filename)
  # checking if it is a file
  if os.path.isfile(f) and not filename.startswith('.'):
    outfile = "/opt/icons/"+ filename + ".JPEG"
    with Image.open(f) as im:
      im.rotate(90).convert('RGB').resize((128,128)).save(outfile)
