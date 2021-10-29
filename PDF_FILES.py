import os
from PyPDF2 import PdfFileMerger

Dir="C:\\Users\\rezafta\\Desktop\\SPF\\SoftWare"
Files=os.listdir(Dir)
pdf=PdfFileMerger()

for i in Files:
    pdf.append(Dir+"\\"+i);

pdf.write("C:\\Users\\rezafta\\Desktop\\Software.pdf")
pdf.close()