import PyPDF2
import pandas as pd
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


def convert_text_to_csv(text, csv_path):
    # Process 'text' to structure data appropriately
    # ...

    # Example: Split text into lines and create a DataFrame
    lines = text.split('\n')
    data = [line.split(',') for line in lines]
    print(data)
    df = pd.DataFrame(data, columns=['CRNumber','Description','Victim','Reported','Location'])  # Adjust column names

    # Save DataFrame to CSV
    df.to_csv(csv_path, index=False)

def  main():
    pdf_path = 'Page2.pdf'
    csv_path = 'web_scrape_datapy.csv'

    pdf_text = extract_text_from_pdf(pdf_path)
    convert_text_to_csv(pdf_text, csv_path)

if __name__ == "__main__":   
    main()