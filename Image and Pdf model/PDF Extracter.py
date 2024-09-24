import pdfplumber
import spacy

# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Parameters:
    pdf_path (str): The path to the PDF file.

    Returns:
    str: The extracted text from the PDF.
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Step 2: Use spaCy's Pre-trained Model to Extract Named Entities
nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    """
    Extracts named entities from the provided text using spaCy.

    Parameters:
    text (str): The text from which to extract entities.

    Returns:
    list: A list of tuples containing the entity text and its label.
    """
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))  # Append the entity and its label
    return entities

# Step 3: Combine PDF Text Extraction with Entity Recognition
def extract_data_from_pdf(pdf_path):
    """
    Extracts data from a PDF file, including text and named entities.

    Parameters:
    pdf_path (str): The path to the PDF file.

    Returns:
    list: A list of tuples containing the extracted entities and their labels.
    """
    pdf_text = extract_text_from_pdf(pdf_path)  # Extract text from the PDF
    entities = extract_entities(pdf_text)  # Extract entities from the text
    return entities

# Function to format extracted entities into a clear explanation
def format_extracted_data(extracted_entities):
    """
    Formats the extracted entities into a readable explanation.

    Parameters:
    extracted_entities (list): The list of extracted entities and labels.

    Returns:
    str: A formatted string explaining the extracted details.
    """
    formatted_data = []
    for entity, label in extracted_entities:
        if label == 'CARDINAL':
            formatted_data.append(f"Value: {entity}")
        elif label == 'ORG':
            formatted_data.append(f"Organization: {entity}")
        elif label == 'TIME':
            formatted_data.append(f"Time: {entity}")
        elif label == 'WORK_OF_ART':
            formatted_data.append(f"Event/Art: {entity}")
        elif label == 'PERSON':
            formatted_data.append(f"Reference: {entity}")
        elif label == 'ORDINAL':
            formatted_data.append(f"Order: {entity}")

    return "\n".join(formatted_data)

# Example Usage
pdf_path = "example.pdf"
extracted_entities = extract_data_from_pdf(pdf_path)

# Formatting and printing the extracted data
formatted_output = format_extracted_data(extracted_entities)
print("Extracted Details from Hackathon Document:\n")
print(formatted_output)
