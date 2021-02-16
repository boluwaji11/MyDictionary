import pickle
import os

eof = False

path = "names_files.dat"

outfile = open("names_files.dat", "ab")
infile = open("names_files.dat", "rb")

print(os.path.getsize(path))

input()

if os.path.getsize(path) > 0:
    names = pickle.load(infile)
    name = input("Add a name: ")
    names.append(name)
else:
    names = []
    name = input("Add a name: ")
    names.append(name)

pickle.dump(names, outfile)
outfile.close()

print(names)