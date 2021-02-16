import pickle

outfile = open("names_file.dat", "wb")

names = []
name = input("Add a name to the list: ")
names.append(name)

pickle.dump(names, outfile)

outfile.close()