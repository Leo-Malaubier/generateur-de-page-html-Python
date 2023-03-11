
import shutil #permet de copier un fichier
import os #permet de géré des fichier
import lectureCSV


def main():
    shutil.rmtree('temps')
    if not os.path.exists('temps'):
        os.makedirs('temps')
    if not os.path.exists('temps/xlsxTOcsvTemp'):
        os.makedirs('temps/xlsxTOcsvTemp')
