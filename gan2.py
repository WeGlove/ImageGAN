from PIL import Image
from numpy import asarray
import numpy as np
import os

# load the image


def load_data():
    paths = [os.path.join("data", x) for x in [
        '2011-07-25_11.47.24.png',
        '2011-07-25_11.47.42.png'
    ]]
    images = [asarray(Image.open(path)) for path in paths]

    # convert image to numpy array

    data = np.array(images)
    return data

if __name__ == "__main__":
    load_data()