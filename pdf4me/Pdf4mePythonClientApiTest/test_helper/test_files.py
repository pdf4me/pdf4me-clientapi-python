import os

from pdf4me.helper.file_reader import FileReader


class TestFiles(object):

    file_reader = FileReader()

    def __init__(self):

        self.pdf_name = 'pdf1.pdf'
        self.pdf_path = os.getcwd() + '/../pdf1.pdf'
        self.pdf_data = self.file_reader.get_file_data(self.pdf_path)
        self.pdf_length = len(self.pdf_data)

        self.pdf_name_2 = 'pdf2.pdf'
        self.pdf_path_2 = os.getcwd() + '/../pdf2.pdf'
        self.pdf_data_2 = self.file_reader.get_file_data(self.pdf_path_2)
        self.pdf_length_2 = len(self.pdf_data_2)

        self.text_name = 'txt.txt'
        self.text_path = os.getcwd() + '/../txt.txt'
        self.text_data = self.file_reader.get_file_data(self.text_path)
        self.text_length = len(self.text_data)

        self.word_name = 'wordDoc.docx'
        self.word_path = os.getcwd() + '/../wordDoc.docx'
        self.word_data = self.file_reader.get_file_data(self.word_path)
        self.word_length = len(self.word_data)

        self.excel_name = 'excel.xlsx'
        self.excel_path = os.getcwd() + '/../excel.xlsx'
        self.excel_data = self.file_reader.get_file_data(self.excel_path)
        self.excel_length = len(self.excel_data)

        self.eml_name = 'email.eml'
        self.eml_path = os.getcwd() + '/../email.eml'
        self.eml_data = self.file_reader.get_file_data(self.eml_path)
        self.eml_length = len(self.eml_data)

        self.msg_name = 'email.msg'
        self.msg_path = os.getcwd() + '/../email.msg'
        self.msg_data = self.file_reader.get_file_data(self.msg_path)
        self.msg_length = len(self.msg_data)

        self.jpg_name = 'picture.jpg'
        self.jpg_path = os.getcwd() + '/../picture.jpg'
        self.jpg_data = self.file_reader.get_file_data(self.jpg_path)
        self.jpg_length = len(self.jpg_data)

        self.zip_name = 'zip.zip'
        self.zip_path = os.getcwd() + '/../zip.zip'
        self.zip_data = self.file_reader.get_file_data(self.zip_path)
        self.zip_length = len(self.zip_data)
