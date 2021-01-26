"""This one is somewhat buggy, i'm lazy to fix it
but one day i may be back"""

from fpdf import FPDF
# from PIL import Image
import os

directory = r""


def makePdf(pdfFileName, listPages, dir=''):
    print("Starting...")
    if (dir):
        dir += "/"
    # cover = Image.open(dir + str(listPages[0]))  # this is for cover img
    # it can be handy in sometimes
    width, height = (800, 1200)  # size of the image, you can set a A4 size
    # print(cover.size)

    print("Setting up parameters...")
    pdf = FPDF(unit="pt", format=[width, height])

    i = 0
    for page in listPages:
        print(page)
        i += 1
        percent = i * 100 / len(listPages)

        # print(type(page))
        # change the code below for each manga
        if page != "undefined.jpg":
            # this is for manga converter
            pdf.add_page()
            pdf.image(dir + str(page), 0, 0)
            print(f"Page {page} =========== {percent:.1f}% completed")

    print("Adding images...")
    pdf.output(dir + pdfFileName + ".pdf", "F")


listPages = os.listdir(directory)


makePdf("", listPages, dir=directory)
