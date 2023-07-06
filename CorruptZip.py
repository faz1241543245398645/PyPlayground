import sys
import zipfile

def test_zip_file(zip_file):
    print("Testing zip file: %s" % zip_file)
    try:
        ret = zipfile.ZipFile(zip_file).testzip()
        if ret is not None:
            print("First bad file in zip: %s" % ret)
            return False
    except Exception as ex:
        print("Exception:", ex)
        return False
    return True
if __name__ == "__main__":
    zip_file_path = str("")
    if test_zip_file(zip_file_path):
        print("Zip file is good")
