def make_class(name):
    if name == "pdf":

        class PdfFile:
            pass

        return PdfFile
    else:

        class TxtFile:
            pass

        return TxtFile


PdfFile = make_class("pdf")
print(PdfFile)
print(PdfFile())


<class '__main__.make_class.<locals>.PdfFile'>
<__main__.make_class.<locals>.PdfFile object at 0x105654240>