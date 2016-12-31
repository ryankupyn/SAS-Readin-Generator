import csv

def csvreader(filepath):
    result = []
    with open(filepath) as readin:
        readfile = csv.reader(readin,delimiter=",",quotechar='"') #Note: I would like to make these options autodetectable in a later verion (perhaps read in as raw text initially, delimiter is most common character out of tab/comma and quote is most common out of single/double quote/bar
        for entry in next(readfile): #Beware! This program only works with files that have headers and where the relevant data starts on the second line. No fancypants formatting
            result.append([])
        for row in readfile:
            for entry in row:
                entrynum = row.index(entry)
                result[entrynum].append(entry)
    return result