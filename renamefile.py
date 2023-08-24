import pathlib,os,glob
dir = os.getcwd()
new_file_name = "newfilename.docx"

for path in pathlib.Path(dir).glob("*.docx"):
    folder = path.stem #return list?
    os.mkdir(folder)
    new_path = pathlib.Path(dir,folder,new_file_name)
    path.rename(new_path)
