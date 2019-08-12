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


<<<<<<< HEAD
<class '__main__.make_class.<locals>.PdfFile'>
<__main__.make_class.<locals>.PdfFile object at 0x105654240>
=======
# <class '__main__.make_class.<locals>.Daum'>
# <__main__.make_class.<locals>.Daum object at 0x104149160>
>>>>>>> 4cab2d301afc242e18f3afe2aa42502038f793dc
