from ocr.easyocr_engine import EasyOCREngine

ocr = EasyOCREngine()

print("=" * 60)
print("TESTING IMAGE")
print("=" * 60)

image_text = ocr.extract_text("data/invoices/sample_invoice.jpg")

print(image_text)

print("\n")

print("=" * 60)
print("TESTING PDF")
print("=" * 60)

pdf_text = ocr.extract_text("data/invoices/sample_invoice.pdf")

print(pdf_text)