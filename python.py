from pathlib import Path
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
# close here

if userInp == 1:
    showAllFileAndFolderfunction()



