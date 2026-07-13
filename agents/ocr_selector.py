import os

from ocr.easyocr_engine import EasyOCREngine
from ocr.rapidocr_engine import RapidOCREngine
from ocr.doctr_engine import DocTREngine


class OCRSelector:

    def __init__(self):

        self.engines = [
            DocTREngine(),
            RapidOCREngine(),
            EasyOCREngine()
        ]

    def select_engine(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":

            print("AI Agent Selected : docTR")

            return DocTREngine()

        file_size = os.path.getsize(file_path)

        if file_size < 1024 * 1024:

            print("AI Agent Selected : RapidOCR")

            return RapidOCREngine()

        print("AI Agent Selected : EasyOCR")

        return EasyOCREngine()

    def fallback_engines(self):

        return self.engines