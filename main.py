import pdfplumber
from gtts import gTTS

path = "./pdf/Grit.pdf"

all_pages = ""

with pdfplumber.open(path) as pdf:
    for i in range(0, len(pdf.pages)):
        pdf_text = pdf.pages[i].extract_text()
        all_pages += pdf_text

gtts_converter = gTTS(text=all_pages, lang="en", tld="co.uk",)
gtts_converter.save("Grit.mp3")
print("Finished")
