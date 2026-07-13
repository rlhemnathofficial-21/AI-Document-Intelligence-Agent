import easyocr
import fitz  # PyMuPDF
import numpy as np
from PIL import Image


class EasyOCREngine:

    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, file_path):

        # ---------- IMAGE ----------
        if file_path.lower().endswith((".jpg", ".jpeg", ".png")):

            result = self.reader.readtext(file_path, detail=0)

            return "\n".join(result)

        # ---------- PDF ----------
        elif file_path.lower().endswith(".pdf"):

            document = fitz.open(file_path)

            full_text = ""

            for page in document:

                pix = page.get_pixmap(dpi=300)

                image = Image.frombytes(
                    "RGB",
                    [pix.width, pix.height],
                    pix.samples
                )

                image_np = np.array(image)

                result = self.reader.readtext(image_np, detail=0)

                full_text += "\n".join(result)
                full_text += "\n"

            return full_text

        else:

            raise ValueError("Unsupported file format.")