import pathlib


# - prints the home directory
print("The Home Directory is: ", pathlib.Path.home())


# - getting the current working directory
print("The current working directory is: ", pathlib.Path.cwd())


# - get the file extension from a filename
path = pathlib.Path.cwd() / 'text_file.txt'
print("The suffix of {} is: ".format(path.stem), path.suffix)


# - read and write text files
print("File Contents: ", path.read_text())
path.write_text("This is a line written through the program.")
print("File Contents after writing: ", path.read_text())


# - Delete files
try:
    path2 = pathlib.Path.cwd() / 'text_file2.txt'  # Deleting another file
    path2.unlink()
except Exception as e:
    print(e)
finally:
    print("The file has either been already deleted or does not exist :(")


# - Copy files from one directory to another
source = pathlib.Path.cwd() / 'text_file.txt'
destination = pathlib.Path.cwd() / 'text_file3.txt'
destination.write_bytes(source.read_bytes())
