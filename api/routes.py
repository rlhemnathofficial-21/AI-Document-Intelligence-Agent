from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import time
import traceback

from agents.ocr_selector import OCRSelector
from agents.quality_agent import QualityAgent
from agents.item_agent import ItemAgent
from agents.prompt_agent import PromptAgent
from agents.postprocess_agent import PostProcessAgent
from agents.recovery_agent import RecoveryAgent
from agents.validation_agent import ValidationAgent

from llm_service.llama_service import LlamaService

router = APIRouter()

UPLOAD_FOLDER = "data/invoices"


@router.post("/extract")
async def extract_invoice(file: UploadFile = File(...)):

    try:

        start_time = time.time()

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ==========================================
        # OCR Selection
        # ==========================================

        selector = OCRSelector()

        ocr_engine = selector.select_engine(file_path)

        selected_name = ocr_engine.__class__.__name__

        extracted_text = ocr_engine.extract_text(file_path)

        # ==========================================
        # OCR Quality Check
        # ==========================================

        quality = QualityAgent()

        extracted_text = quality.clean_text(extracted_text)

        if not quality.evaluate(extracted_text):

            raise Exception(
                "Poor OCR quality. Please upload a clearer invoice."
            )

        # ==========================================
        # Item Extraction
        # ==========================================

        item_agent = ItemAgent()

        extracted_items = item_agent.extract_items(
            extracted_text
        )

        # ==========================================
        # Prompt Generation
        # ==========================================

        prompt_agent = PromptAgent()

        prompt = prompt_agent.build_prompt(
            extracted_text,
            extracted_items
        )

        # ==========================================
        # LLM Extraction
        # ==========================================

        llm = LlamaService()

        structured_json = llm.extract_json(prompt)

        if not isinstance(structured_json, dict):

            raise Exception(
                "LLM returned invalid JSON."
            )

        if structured_json.get("status") == "error":

            raise Exception(
                structured_json.get("message")
            )

        # ==========================================
        # Post Processing
        # ==========================================

        postprocess = PostProcessAgent()

        structured_json = postprocess.clean(
            structured_json
        )

        # ==========================================
        # Recover Missing Fields
        # ==========================================

        recovery = RecoveryAgent()

        structured_json = recovery.recover(
            structured_json,
            extracted_text
        )

        # ==========================================
        # Remove Empty Fields
        # ==========================================

        structured_json = remove_empty_fields(
            structured_json
        )

        # ==========================================
        # Validation
        # ==========================================

        validator = ValidationAgent()

        validation = validator.validate(
            structured_json
        )

        processing_time = round(
            time.time() - start_time,
            2
        )

        return {

            "status": "success",

            "ocr_engine": selected_name,

            "processing_time": processing_time,

            "ocr_text": extracted_text,

            "parsed_items": extracted_items,

            "structured_json": structured_json,

            "validation": validation

        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# Remove Empty Fields Recursively
# =====================================================

def remove_empty_fields(data):

    if isinstance(data, dict):

        cleaned = {}

        for key, value in data.items():

            value = remove_empty_fields(value)

            if value not in (
                None,
                "",
                [],
                {}
            ):

                cleaned[key] = value

        return cleaned

    elif isinstance(data, list):

        cleaned_list = []

        for item in data:

            item = remove_empty_fields(item)

            if item not in (
                None,
                "",
                [],
                {}
            ):

                cleaned_list.append(item)

        return cleaned_list

    return data