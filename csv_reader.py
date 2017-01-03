import csv

def csvreader(filepath): #This takes a filepath to a CSV and outputs a list-of-lists (one sublist per column) of data and a list of variable names - as of right now it only works for the most plain-vanilla of csvs (header on the top row, data in orderly lines below that). The occasional blank variable name isn't a problem though - they just show up as VAR(column number)
    result = []
    varnames = []
    with open(filepath) as readin:
        readfile = csv.reader(readin,delimiter=",",quotechar='"') #Note: I would like to make these options autodetectable in a later verion (perhaps read in as raw text initially, delimiter is most common character out of tab/comma and quote is most common out of single/double quote/bar
        for entry in next(readfile): #Beware! This program only works with files that have headers and where the relevant data starts on the second line. No fancypants formatting
            result.append([])
            varnames.append(entry)
        for row in readfile:
            for entry in row:
                entrynum = row.index(entry)
                result[entrynum].append(entry)
    return result, varnames

