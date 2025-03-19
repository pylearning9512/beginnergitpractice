import os as os

def NamingFuction():
    i=0
    path = input("Enter the path of the directory: ")
    for filename in os.listdir(path):
        my_dest = "uwu" + str(i) + ".pdf"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
if __name__ == '__main__':
    NamingFuction()
# This code is a mass renamer that renames all the files in a directory to "uwu" + a number + ".pdf"