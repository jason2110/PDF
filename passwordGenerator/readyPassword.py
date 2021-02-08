from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfwriter=PdfFileWriter()
pdf=PdfFileReader("n_pass.pdf")

for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))

passw="jason"
pdfwriter.encrypt(passw)
with open('withAutomaticPassword.pdf','wb') as f:
  pdfwriter.write(f)
  f.close()