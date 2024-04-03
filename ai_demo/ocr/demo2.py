from manga_ocr import MangaOcr

mocr = MangaOcr()
text = mocr('ocr_recognition.png')
print(text)