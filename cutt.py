from PyPDF2 import PdfFileWriter, PdfFileReader

def cutpdf(name):

    with open(name+'.pdf', "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output = PdfFileWriter()
        numPages = input1.getNumPages()
        for i in range(numPages):
            page = input1.getPage(i)
            page.trimBox.lowerLeft = (25, 25)
            page.trimBox.upperRight = (800,800)
            page.cropBox.lowerLeft = (0,600)
            page.cropBox.upperRight = (612,792)
            output.addPage(page)

        with open(name+'cut'+'.pdf', "wb") as out_f:
            output.write(out_f)
    return name+'cut'

def new(name):
    inputpdf = PdfFileReader(open(name+'.pdf', "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(name+'%s.pdf' % str(i+1), "wb") as outputStream:
            output.write(outputStream)

