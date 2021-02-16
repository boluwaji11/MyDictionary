import pickle

outfile = open("names_pickle_file_write.dat", "ab")

names = []
# for i in range(0, 4):
name = input("Add a name to the list: ")
names.append(name)
# print(names)

pickle.dump(names, outfile)

outfile.close()
