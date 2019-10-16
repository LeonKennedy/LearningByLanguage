#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: pdftools.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:  create pdf file
# @Create: 2019-10-15 17:46
# @Last Modified: 2019-10-15 17:46

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from reportlab.lib.colors import magenta, pink, blue, green
from reportlab.pdfgen import canvas


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        num_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}:
    
    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of pages: {num_of_pages}
    """

    print(txt)
    return info


def create_pdf(content):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage("dsafasfda")
    with open('jief.pdf', 'wb') as o:
        pdf_writer.write(o)


def merge_pdf():
    pdf_merge = PdfFileMerger()
    pdf_merge.append("aaaa" * 12)
    with open('jief.pdf', 'wb') as o:
        pdf_merge.write(o)


# -----  other  -----

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))


def create():
    c = canvas.Canvas('simple_form.pdf')
    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Employment Form')
    c.setFont("STSong-Light", 14)
    form = c.acroForm

    c.drawString(10, 650, 'First Name:')
    form.textfield(name='fname', tooltip='First Name',
                   x=110, y=635, borderStyle='inset',
                   borderColor=magenta, fillColor=pink,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 600, 'Last Name:')
    form.textfield(name='lname', tooltip='Last Name',
                   x=110, y=585, borderStyle='inset',
                   borderColor=green, fillColor=magenta,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 550, 'Address:')
    form.textfield(name='address', tooltip='Address',
                   x=110, y=535, borderStyle='inset',
                   width=400, forceBorder=True)

    c.drawString(10, 500, 'City:')
    form.textfield(name='city', tooltip='City',
                   x=110, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(250, 500, '你好:')
    form.textfield(name='state', tooltip='State',
                   x=350, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 450, 'Zip Code:')
    form.textfield(name='zip_code', tooltip='Zip Code',
                   x=110, y=435, borderStyle='inset',
                   forceBorder=True)

    c.save()


if __name__ == '__main__':
    # path = "/Users/coffee/Documents/test_form.pdf"
    # extract_information(path)
    create()
