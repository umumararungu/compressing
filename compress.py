import os.path
from datetime import datetime
import zipfile
import tarfile

def compressFile(filePath, compressType):
    try:

        fileNameBefore  = os.path.basename(filePath)
        currentDate = datetime.now().strftime("%Y_%m_%d")
        fileNameAfter = f"{fileNameBefore}_{currentDate}.{compressType}"

        if compressType == "zip":
            with zipfile.ZipFile(fileNameAfter,"w") as zipf:
                for root, dirs, files in os.walk(filePath):
                    for file in files:
                        zipf.write(os.path.join(root, file),
                                   arcname=os.path.relpath(
                                       os.path.join(root, file), filePath))

        elif compressType == "tgz":
            with tarfile.open(f"{fileNameAfter}.gz", "w:gz") as tar:
                tar.add(filePath, arcname=os.path.basename(filePath))  

        elif compressType == "tar":
            with tarfile.open(fileNameAfter, "w") as tar:
                tar.add(filePath, arcname=os.path.basename(filePath))

    except Exception as e:
        print(f"Compression has failed: {e}")

def main():
    filePath = input("Enter the folder path to compress: ")
    compressType = ["zip", "tar", "tgz", "rar", "mint"]
    
    print("Available compressed file types:")
    for index, type in enumerate(compressType, start=1):
        print(f"{index}. {type}")
    
    try:
        option = int(input("Enter the  number according to the options."))
        if 1 <= option <= len(compressType):
            compressType = compressType[option - 1]
            compressFile(filePath, compressType)
        else:
            print("Try again by entering number according to the options.")
    except ValueError:
        print("Please enter a number.")

if __name__ == "__main__":
    main()
