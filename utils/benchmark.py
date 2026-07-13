import time


class OCRBenchmark:

    def evaluate(self, engine, file_path):

        start = time.time()

        text = engine.extract_text(file_path)

        end = time.time()

        return {
            "processing_time": round(end-start,2),
            "characters": len(text),
            "words": len(text.split())
        }