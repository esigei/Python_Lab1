import numpy as np
# using numpy module to load file using the np loadtxt function with data type U25
f1 = np.loadtxt('file1.txt', dtype='U25')
f2 = np.loadtxt('file2.txt', dtype='U25')
# create a list comprehension to iterate through the two files and remove words that are in f2 from f1 and populate these words into list c
c = [i for i in f1 if not i in np.char.capitalize(f2) and not i in f2]
# if np.char.capitalize(f2) is not used in above the capitalized 'In' at the beginning of the second sentence is not removed
# c = [i for i in f1 if not i in f2]
# unpack the list using the * constructor
print (*c)