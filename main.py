import data_examiner
import csv_reader
import SAS_Printer

filepath = input("Please enter the filepath of the CSV you want to read in:")

print("Reading data")
data, varnames = csv_reader.csvreader(filepath)

print("Assigning formats to data columns")
formats = data_examiner.datareader(data)

print("Sifting through plausible data formats")
chosenformats = data_examiner.format_selector(formats)

print("Assigning names to variables")
SASnames = data_examiner.variable_creator(varnames)

print("Determining appropriate save location for data")
casename, savelocation, filename, datasetname, liblocation = data_examiner.filepathcreator(filepath)

print("Writing SAS program")
SAS_Printer.programprinter(chosenformats, SASnames, casename, savelocation, datasetname, liblocation, filepath)

print("Done! Hopefully.")
print("SAS program located in " + savelocation)