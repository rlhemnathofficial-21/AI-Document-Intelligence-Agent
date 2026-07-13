AI Document Intelligence Agent


Overview


The AI Document Intelligence Agent is an intelligent invoice processing system that extracts structured information from invoice PDF and image documents using a multi-agent AI architecture. The system automatically selects the most suitable OCR engine, evaluates OCR quality, extracts invoice details using a Large Language Model (Llama 3.2 running locally through Ollama), performs post-processing and validation, and produces clean, structured JSON output.
Unlike traditional OCR-based extraction systems that rely on fixed templates, this project dynamically understands invoice layouts and extracts only the information available in each document, making it adaptable to invoices from different vendors and formats.
The project was developed using Python, FastAPI, Streamlit, and multiple OCR engines to demonstrate a complete AI-powered document processing workflow suitable for real-world business applications.



Key Features


Multi-Agent AI Architecture
Intelligent OCR Engine Selection
Multiple OCR Engines
RapidOCR
EasyOCR
docTR
OCR Quality Evaluation
Invoice Item Extraction
Prompt Optimization
Local LLM Processing using Llama 3.2 (Ollama)
Automatic Post-Processing
Invoice Data Validation
Dynamic JSON Output
PDF and Image Invoice Support
Interactive Streamlit Dashboard
FastAPI REST API Backend



Technologies Used


Programming Language
Python 3.14
Backend
FastAPI
Frontend
Streamlit
Large Language Model
Llama 3.2
Ollama
OCR Engines
RapidOCR
EasyOCR
docTR
Libraries
OpenCV
Pillow
NumPy
Uvicorn
Pydantic
Development Environment
Visual Studio Code
Git
GitHub
macOS


Project Objective


The primary objective of this project is to build an AI-powered document intelligence system capable of accurately extracting structured invoice information from unstructured business documents.
Instead of depending on predefined templates, the system combines OCR technology with Large Language Models and multiple intelligent agents to understand invoice content, validate extracted information, and generate clean JSON suitable for downstream automation.



Business Applications


Invoice Processing Automation
Accounts Payable Automation
Financial Data Digitization
ERP Integration
Intelligent Document Processing (IDP)
Business Process Automation
Digital Transformation


Project Highlights


Intelligent OCR engine selection
Multi-agent workflow
Local LLM inference (No cloud dependency)
Dynamic invoice understanding
Automatic data validation
Clean structured JSON output
Modular and scalable architecture
Professional FastAPI backend
User-friendly Streamlit interface

Repository Topics

python
fastapi
streamlit
ocr
easyocr
rapidocr
doctr
ollama
llama
llama3
document-intelligence
invoice-processing
invoice-extraction
json
artificial-intelligence
machine-learning
computer-vision
automation
idp
multi-agent