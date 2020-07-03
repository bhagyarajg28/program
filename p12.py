import PyPDF2
k=1
pdfFileObj = open('C:\\Users\\Vaishnavi\\Desktop\\The_Living_World.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
a=pdfReader.numPages
for i in range(0,a):
    pageObj = pdfReader.getPage(i)
    b=pageObj.extractText()
    l=b.splitlines()[7::] 
    for j in l:
        print(j)
