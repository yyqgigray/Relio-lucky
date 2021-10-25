# -*- coding: utf-8 -*-
# author:xl
import docx
import filetype


def importFile(filedialog):
    filePath = filedialog.askopenfilename()
    file = docx.Document(filePath,encodings='UTF-8')
    fileContent = file.read()
    return fileContent

