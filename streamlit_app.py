import streamlit as st
import requests
import time

st.set_page_config(
    page_title="AI Document Intelligence Agent",
    page_icon="📄",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/extract"

st.title("📄 AI Document Intelligence Agent")
st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Invoice",
    type=["pdf", "jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.success("Invoice Uploaded Successfully")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Invoice Details")
        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**File Size:** {round(uploaded_file.size/1024,2)} KB")
        st.write(f"**File Type:** {uploaded_file.type}")

    if st.button("Extract Invoice Information"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        start = time.time()

        try:

            with st.spinner("🤖 AI Agent Processing Invoice..."):

                response = requests.post(
                    API_URL,
                    files=files,
                    timeout=300
                )

            end = time.time()

            if response.status_code == 200:

                result = response.json()

                st.markdown("---")

                st.subheader("🤖 AI Agent Decision")

                st.success(
                    f"OCR Engine Selected : {result.get('ocr_engine','Unknown')}"
                )

                st.metric(
                    "Processing Time",
                    f"{round(end-start,2)} sec"
                )

                st.markdown("---")

                st.subheader("📄 OCR Extracted Text")

                st.text_area(
                    "",
                    result.get("ocr_text",""),
                    height=300
                )

                st.markdown("---")

                st.subheader("📦 Structured JSON")

                st.json(result.get("structured_json",{}))

            else:

                st.error(f"HTTP {response.status_code}")

                try:
                    st.json(response.json())
                except Exception:
                    st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error("❌ Cannot connect to FastAPI server.")
            st.info("Make sure uvicorn is running.")

        except requests.exceptions.Timeout:

            st.error("❌ Request timed out.")

        except Exception as e:

            st.exception(e)