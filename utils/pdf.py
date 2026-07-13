import fitz
from PIL import Image
import numpy as np


def pdf_to_images(pdf_path, dpi=300):
    """
    Convert a PDF into a list of NumPy images.
    """

    document = fitz.open(pdf_path)

    images = []

    for page in document:

        pix = page.get_pixmap(dpi=dpi)

        image = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples,
        )

        images.append(np.array(image))

    return images