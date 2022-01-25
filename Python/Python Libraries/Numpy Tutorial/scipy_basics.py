# Numpy provides a high-performance multidimensional array and basic tools to compute with and manipulate these arrays. 
# SciPy builds on this, and provides a large number of functions that operate on numpy arrays and are useful for different types of scientific and engineering applications.

"""Image operations"""
# SciPy provides some basic functions to work with images. 
# For example, it has functions to read images from disk into numpy arrays, to write numpy arrays to disk as images, and to resize images.
#  Here is a simple example that showcases these functions:

# from scipy.misc  import imread, imsave, imresize 
# PIL is python image library
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
# You can use the imshow function to show images. Here is an example
plt.imshow(image)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(resized_image)
plt.show()



""" Matlab Files"""
# The functions scipy.io.loadmat and scipy.io.savemat allow you to read and write MATLAB files. 

""" Distance between points"""
# SciPy defines some useful functions for computing distances between sets of points.
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Create the following array where each row is a point in 2D space:
# [[0 1]
#  [1 0]
#  [2 0]]
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

# Compute the Euclidean distance between all rows of x.
# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
d = squareform(pdist(x, 'euclidean'))
print(d)


""" Matplotlib"""
# Matplotlib is a plotting library. In this section give a brief introduction to the matplotlib.pyplot module, which provides a plotting system similar to that of MATLAB.
#################################################################
import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show() # You must call plt.show() to make graphics appear.

# Subplots
###############################################################
import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()




