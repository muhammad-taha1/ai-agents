from pypdf import PdfReader
import os
class PdfExtractor:
    def extract_pdf_text_from_file(self, file_path):
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            page_text.strip()
            # page_text = page_text.encode('ascii', errors='ignore').decode()

            if len(page_text) > 10:
                text += page_text
                text += "\n\n"

        return text

    def extract_pdf_text_from_directory(self, directory_path):
        files = []
        obj = os.scandir(directory_path)
        for entry in obj:
            if entry.is_file():
                if entry.name.endswith(".pdf"):
                    files.append(self.extract_pdf_text_from_file(entry.path))

        return files
            

if __name__ == "__main__":
    # print(extract_pdf_text_from_file("./docs/user_manuals/QSG_AG_Harvest-2018_020819_WEB_1.pdf"))
    PdfExtractor().extract_pdf_text_from_directory("./docs/user_manuals")