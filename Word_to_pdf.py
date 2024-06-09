import os
from docx import Document
from docx2pdf import convert

def create_word_file(text: str, filename: str) -> None:
    """
    Create a Word file with the given text.
    
    Args:
        text (str): The text to write into the Word file.
        filename (str): The name of the Word file to create.
    """
    try:
        document = Document()
        document.add_paragraph(text)
        document.save(filename)
        print(f"Word file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating Word file: {e}")

def convert_to_pdf(word_filename: str) -> None:
    """
    Convert a Word file to PDF.
    
    Args:
        word_filename (str): The name of the Word file to convert.
    """
    try:
        pdf_filename, _ = os.path.splitext(word_filename)
        pdf_filename += '.pdf'
        convert(word_filename, pdf_filename)
        print(f"Word file '{word_filename}' converted to PDF '{pdf_filename}'.")
    except Exception as e:
        print(f"Error converting Word file to PDF: {e}")

def main():
    text = input("Enter the text: ")
    word_filename = "output.docx"
    
    create_word_file(text, word_filename)
    convert_to_pdf(word_filename)

if __name__ == "__main__":
    main()
