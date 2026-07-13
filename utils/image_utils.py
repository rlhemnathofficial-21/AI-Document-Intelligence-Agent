from PIL import Image
import numpy as np


def load_image(image_path):
    """
    Load image and convert to NumPy array.
    """

    image = Image.open(image_path).convert("RGB")

    return np.array(image)