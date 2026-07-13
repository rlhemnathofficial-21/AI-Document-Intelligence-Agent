from rapidocr_onnxruntime import RapidOCR


class RapidOCREngine:

    def __init__(self):
        self.engine = RapidOCR()

    def extract_text(self, image_path):

        result, _ = self.engine(image_path)

        if result is None:
            return ""

        lines = []

        for item in result:
            text = item[1]
            lines.append(text)

        return "\n".join(lines)