# import packages
from matplotlib import pyplot as plt
from skimage import io


# read the image
def import_data(filename):
    data = io.imread(filename)
    return data

# plot histogram
def plot_histogram(data):
    fig, ax = plt.subplots(1,1)
    ax.hist(cell.ravel(), bins=40, range = [0, 256])
    plt.show()

# apply threshold
def apply_threshold(data, threshold):
    data_segmented = data > threshold
    return data_segmented

# display data
def display_data(data, colormap):
    plt.imshow(data, cmap=colormap)
    plt.show()


# set the path
filename = '../../data/image4045.tif'

# import data
cell = import_data(filename)
display_data(cell, 'viridis')

# plot_histogram(cell)

# define threshold
threshold = 60 # select threshold based on histogram

# apply threshold
segmented_cell = apply_threshold(cell, threshold)

display_data(segmented_cell, 'gray')
