import os
import PyPDF2
import slate3k as slate
import re

def get_file_name_info(folder_path):
    list_files = os.listdir(folder_path)
    index_list = []
    name_list = []
    for file in list_files:
        index = file.split(".")[0]
        name = get_names(index)
        index_list.append(index)
        name_list.append(name)
    return index_list, name_list, list_files


def get_names(index):
    name = index.split("_")[2:]
    name = ' '.join(name)
    return name


def get_email(file_path):
    # open the pdf file
    object = PyPDF2.PdfFileReader(file_path)

    # get number of pages
    NumPages = object.getNumPages()

    # define keyterms
    text_file =[]
    with open(file_path, 'rb') as f:
        extracted_text = slate.PDF(f)
    for p in range(NumPages):
        text_file.append(extracted_text[p])
    x =("").join(text_file)
    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', x)
    email_address = match.group(0)
    return email_address



