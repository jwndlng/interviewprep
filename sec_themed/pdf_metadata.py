

from PyPDF2 import PdfFileReader
from pathlib import Path


base_dir = Path(__file__).parent.absolute()


file = open(base_dir.joinpath('sample.pdf'), 'rb')
pdf = PdfFileReader(file)
m_data = pdf.getDocumentInfo()

for metadata in m_data:
    print(f"{metadata}: {m_data[metadata]}")

