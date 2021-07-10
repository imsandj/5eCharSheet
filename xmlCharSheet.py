## https://github.com/imsandj/5eCharSheet.git

import PyPDF2 as pypdf
import xml.etree.ElementTree as ET

sourcePdf = 'CharSheet.pdf'
userName = "Joe"
fileName = "dataSheet"

# source for files :: Directory
filepath = "D:\\OneDrive\\Documents\\Projects\\Python\\DnD5e\\"

# xml file
tree = ET.parse(filepath + 'char_export.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.text)


# pdf source/template and pdf output/final
pdfFile = open(filepath + sourcePdf,'rb')
output = filepath + fileName + userName + '.pdf'

read_pdf = pypdf.PdfFileReader(pdfFile)

num_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
# print(num_of_pages, page_content)

# function to map xml file tags to pdf content fields
# def mapValues2Fields():
#     pass

# save pdf with new content from xml data 