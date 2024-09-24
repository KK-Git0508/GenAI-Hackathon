import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path based on your system

# Function to load an image
def load_image(image_path):
    """
    Loads an image from the specified file path.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    PIL.Image: The loaded image.
    """
    image = Image.open(image_path)  # Open the image using PIL
    return image

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image):
    """
    Extracts text from the provided image using Tesseract OCR.

    Parameters:
    image (PIL.Image): The image from which to extract text.

    Returns:
    str: The extracted text from the image.
    """
    text = pytesseract.image_to_string(image)  # Extract text using Tesseract
    return text

# Function to combine image loading and text extraction
def extract_data_from_image(image_path):
    """
    Extracts text data from an image file.

    Parameters:
    image_key (str): The path to the image file.

    Returns:
    str: The extracted text from the image.
    """
    image = load_image(image_path)  # Load the image
    text = extract_text_from_image(image)  # Extract text from the image
    return text

# Function to format the extracted text
def format_extracted_text(extracted_text):
    """
    Formats the extracted text into a more readable format.

    Parameters:
    extracted_text (str): The raw text extracted from the image.

    Returns:
    str: A formatted string of the extracted text.
    """
    formatted_text = extracted_text.strip()  # Strip whitespace from the text
    return formatted_text

# Placeholder for your Gemini API key
# Replace with your actual API key before running the code
api_key = "AIzaSyB1mUu9LHLd-xk3J0FpmWHmDDVwNuErJpQ"  # Replace with your actual API key

# Function to send text to Gemini and return generated text (commented out)
def process_text_with_gemini(text, api_key, model_name, prompt=None):
    """
    Sends the extracted text to the Gemini API for further processing.

    Parameters:
    text (str): The extracted text from the image.
    api_key (str): Your Gemini API key.
    model_name (str): The name of the Gemini model to use (e.g., "gemini-1.5-pro-latest").
    prompt (str, optional): An additional prompt to provide context (default: None).

    Returns:
    str: The generated text from Gemini or an error message.
    """

# Example Usage
image_path = "image.jfif"
extracted_text = extract_data_from_image(image_path)

# Optionally format the extracted text
formatted_text = format_extracted_text(extracted_text)

# Print the extracted text
print("Extracted Text from Image:\n")
print(formatted_text)

# Commented out Gemini processing section (uncomment if needed)
#