from pathlib import Path
import os
currentPath = Path('.').cwd()
print("-" * 50)


print("Show me all files and folders :- 1")
print("Create an new file :- 2")
print("Read a file :- 3")
print("Update a file :- 4")
print("Delete a file :- 5")
userInp = int(input("Type here what you want :- "))


# show all file and folder login
def showAllFileAndFolderfunction():
    print("\033[31m" + "-" * 100 + "\033[0m") 
    for item in currentPath.iterdir():
        if item.is_file():
            print("FILE :" , item.name)
            print("PATH :" , item.resolve())
            print()

        elif item.is_dir():
            print("FOLDER :", item.name)
            print("PATH :", item.resolve)
            print()
# end here

# file create logic
def createFile(fileName , filePath):
       fileContent = input( "What do you want to write? Press ENTER to skip: " ) 
       if filePath: fullPath = Path(filePath) / fileName 
       else: fullPath = Path.cwd() / fileName

       with open(fullPath , "w") as file:
           if fileContent:
               file.write(fileContent)
           print(f"File created at: {fullPath.resolve()}")
# end here

# read file conten logic
def readFile(fileName):
    try:
        with open(fileName , "r") as file:
            content = file.read()
            print(content)
    except:
        print(f"Error: The file '{fileName}' does not exist.")
# end here 

def updateFileContent(fileName):
    with open(fileName , "w") as file:
        fileContent = input("type here your new content : ")
        file.write(fileContent)

def deleteFile(fileName):
    os.remove(fileName)
    print("File delete successfully")


if userInp == 1:
    showAllFileAndFolderfunction()
elif userInp == 2:
    fileName = input("Please tell your file name : ")
    filePath = input("Please tell your file path press ENTER for current repositorie : ")
    createFile(fileName , filePath)
elif userInp == 3:
    fileName = input("Enter your file name : ")
    readFile(fileName)
elif userInp == 4:
    fileName = input("file name for updating content : ")
    updateFileContent(fileName)
elif userInp == 5:
    fileName = input("please enter your file name for deleting a file : ")
    deleteFile(fileName)