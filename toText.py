from pdftext import extract_text_from_pdf
from docToText import extract_text_from_doc


def text(path):
    if '.doc' in path:
        return extract_text_from_doc(path)
    if '.pdf' in path:
        return extract_text_from_pdf(path)
