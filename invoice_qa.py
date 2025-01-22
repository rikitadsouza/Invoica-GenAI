import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from PIL import Image
import os
import io

# Configure the API
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# model
model = genai.GenerativeModel('gemini-1.5-flash')

def process_invoice(image_file):
    return Image.open(image_file)

def get_invoice_info(image, question):
    response = model.generate_content([image, question])
    return response.text

def main():
    st.title("InvoiceScan - Invoice Information Extractor")

    uploaded_file = st.file_uploader("Upload an invoice image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        invoice_image = process_invoice(uploaded_file)
        st.image(invoice_image, caption="Uploaded Invoice", use_column_width=True)

        question = st.text_input("Ask a question about the invoice:")
        
        if st.button("Get Answer"):
            try:
                answer = get_invoice_info(invoice_image, question)
                st.write(f"Answer: {answer}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()