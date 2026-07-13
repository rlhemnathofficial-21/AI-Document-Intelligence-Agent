from doctr.io import DocumentFile
from doctr.models import ocr_predictor


class DocTREngine:
    def __init__(self):
        """
        Initialize the docTR OCR model.
        """
        self.model = ocr_predictor(pretrained=True)

    def extract_text(self, file_path):
        """
        Extract text from a PDF or image using docTR.
        """

        # Load document
        if file_path.lower().endswith(".pdf"):
            document = DocumentFile.from_pdf(file_path)
        else:
            document = DocumentFile.from_images(file_path)

        # Perform OCR
        result = self.model(document)

        extracted_text = []

        # Read text from all pages
        for page in result.pages:
            for block in page.blocks:
                for line in block.lines:
                    line_text = " ".join(word.value for word in line.words)
                    extracted_text.append(line_text)

        return "\n".join(extracted_text)