import google.generativeai as genai
from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Configure the API
genai.configure(api_key='AIzaSyDePPKzsXffHpD1STr3zOIBzCp5SbRYIzI')

# Load and prepare the model
model = genai.GenerativeModel('gemini-1.5-flash')

def process_invoice(image_path):
    image = Image.open(image_path)
    return image

def get_invoice_info(image, question):
    response = model.generate_content([image, question])
    return response.text

def main():
    invoice_path = input("Enter the path to your invoice image: ")
    invoice_image = process_invoice(invoice_path)
    
    while True:
        question = input("Ask a question about the invoice (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        
        try:
            answer = get_invoice_info(invoice_image, question)
            print(f"Answer: {answer}\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()