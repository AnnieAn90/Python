from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt

# Read an JPEG image into a numpy array
image = Image.open("cat.jpg")
width, height = image.size
image.show()

new_size = (int(width/2),int(height/2))

resized_image = image.resize(new_size)
new_width, new_height = resized_image.size
resized_image.show()

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(image)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(resized_image)
plt.show()