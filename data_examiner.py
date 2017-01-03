# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:40:13 2016

@author: RKupyn
"""

import re
import os


def datareader(datalist):
    possformats = []
#    lengths = []
    BEST = re.compile("^-?\d*\.?\d*$"),"BEST" #Starting off with a giant pile of regular expressions, each part of a tuple that also contains the offical name of the informat
    BINARY = re.compile("^[0|1]*$"),"BINARY"
    CHAR = re.compile(".*"),"CHAR"
    HEX = re.compile("^[\d|A-F]*$"),"HEX"
    OCTAL = re.compile("^[0-7]*$"),"OCTAL"
    N8601B_DUR_1 = re.compile("^P\d{4}-\d{2}-\d{2}T\d{1,2}:\d{1,2}:\d{1,2}\.?\d*$"),"N8601B"
    N8601B_DUR_2 = re.compile("^P\d{4}\d{2}\d{2}T\d{1,2}\d{1,2}\d{1,2}$"),"N8601B"
    N8601B_DUR_3 = re.compile("^P\d{1,4}y\d{1,2}m\d{1,2}dT\d{1,2}h\d{1,2}m\d{1,2}\.?\d*s$"),"N8601B"
    N8601B_DUR_4 = re.compile("^P\d+W$"),"N8601B"
    N8601B_INT_1 = re.compile("^\d{4}-\d{2}-\d{2}T\d{1,2}:\d{1,2}:\d{1,2}\/\d{4}-\d{2}-\d{2}T\d{1,2}:\d{1,2}:\d{1,2}$"),"N8601B"
    N8601B_INT_2 = re.compile("^\d{8}T\d{6,}\/\d{8}T\d{6,}$"),"N8601B"
    N8601B_INT_3 = re.compile("^P\d{1,4}y\d{1,2}M\d{1,2}dT\d{1,2}h\d{1,2}m\d{1,2}\.?\d*s\/\d{1,4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}\.?\d*$"),"N8601B"
    N8601B_INT_4 = re.compile("^\d{1,4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}\.?\d*\/P\d{1,4}y\d{1,2}M\d{1,2}dT\d{1,2}h\d{1,2}m\d{1,2}\.?\d*s$"),"N8601B"
    N8601B_DT_1 = re.compile("^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.?\d*$"),"N8601B"
    N8601B_DT_2 = re.compile("^\d{4}\d{2}\d{2}T\d{2}\d{2}\d{2}\.?\d*$"),"N8601B"
    MDYAMPM = re.compile("^[0-1]?[0-9]\/[0-3]?[0-9]\/[12]?[0-9]?[0-9][0-9].\d{1,2}:\d{1,2}:\d{1,2}.*$"),"MDYAMPM"
    MMDDYY = re.compile("^[0-1]?[0-9]\/[0-3]?[0-9]\/[12]?[0-9]?[0-9][0-9]$"),"MMDDYY"
    """ #Not every regular expression is done, as you can see, but I'm working on it
    ANYDTDTE = re.compile("")
    ANYDTDTM = re.compile("")
    ANYDTTME = re.compile("")
    B8601DA = re.compile("")
    B8601DN = re.compile("")
    B8601DT = re.compile("")
    B8601DZ = re.compile("")
    B8601TM = re.compile("")
    B8601TZ = re.compile("")
    DATE = re.compile("")
    DATETIME = re.compile("")
    DDMMYY = re.compile("")
    E8601DA = re.compile("")
    E8601DN = re.compile("")
    E8601DT = re.compile("")
    E8601DZ = re.compile("")
    E8601LZ = re.compile("")
    E8601TM = re.compile("")
    E8601TZ = re.compile("")
    JULIAN = re.compile("")
    MONYY = re.compile("")
    MSEC = re.compile("")
    PDJULG = re.compile("")
    PDJULI = re.compile("")
    PDTIME = re.compile("")
    RMFDUR = re.compile("")
    RMFSTAMP = re.compile("")
    SHRSTAMP = re.compile("")
    SMFSTAMP = re.compile("")
    STIMER = re.compile("")
    TIME = re.compile("")
    TODSTAMP = re.compile("")
    TU = re.compile("")
    WEEKU = re.compile("")
    WEEKV = re.compile("")
    WEEKW = re.compile("")
    YMDDTTM = re.compile("")
    YYMMDD = re.compile("")
    YYMMN = re.compile("")
    YYQ = re.compile("")
    N8601B = re.compile("")
    N8601E = re.compile("")
    B8601DA = re.compile("")
    B8601DN = re.compile("")
    B8601DT = re.compile("")
    B8601DZ = re.compile("")
    B8601TM = re.compile("")
    B8601TZ = re.compile("")
    E8601DA = re.compile("")
    E8601DN = re.compile("")
    E8601DT = re.compile("")
    E8601DZ = re.compile("")
    E8601LZ = re.compile("")
    E8601TM = re.compile("")
    E8601TZ = re.compile("")
    BINARY = re.compile("")
    BITS = re.compile("")
    BZ = re.compile("")
    COMMA = re.compile("")
    COMMAX = re.compile("")
    E = re.compile("")
    FLOAT = re.compile("")
    HEX = re.compile("")
    IB = re.compile("")
    IBR = re.compile("")
    IEEE = re.compile("")
    NUMX = re.compile("")
    OCTAL = re.compile("")
    PD = re.compile("")
    PERCENT = re.compile("")
    PIB = re.compile("")
    PIBR = re.compile("")
    PK = re.compile("")
    RB = re.compile("")
    S370FF = re.compile("")
    S370FIB = re.compile("")
    S370FIBU = re.compile("")
    S370FPD = re.compile("")
    S370FPDU = re.compile("")
    S370FPIB = re.compile("")
    S370FRB = re.compile("")
    S370FZD = re.compile("")
    S370FZDL = re.compile("")
    S370FZDS = re.compile("")
    S370FZDT = re.compile("")
    S370FZDU = re.compile("")
    TRAILSGN = re.compile("")
    VAXRB = re.compile("")
    VMSZN = re.compile("")
    ZD = re.compile("")
    ZDB = re.compile("")
    ZDV = re.compile("")
    """
    regexlist = [BEST,BINARY,CHAR,HEX,OCTAL,N8601B_DUR_1,N8601B_DUR_2,N8601B_DUR_3,N8601B_DUR_4,N8601B_INT_1,N8601B_INT_2,N8601B_INT_3,N8601B_INT_4,N8601B_DT_1,N8601B_DT_2,MDYAMPM,MMDDYY]
    for variable in datalist:
        matches = regexlist
        longestlen = 0
        for entry in variable: #looping through the entire variable, steadily winnowing down the list of possible formats that match. Thankfully in most cases we end up with just one or two matching regexes after the first few rows, so things go quite swiftly
            if entry != "": #Figuring out how to handle entirely blank colums was challenging for me, but creating the marker of
                longestlen = max(longestlen,len(entry))
                tempmatch = []
                for regex in matches:
                    if regex[0].match(entry):
                        tempmatch.append(regex)
                matches = tempmatch
        namematch = [] #creating a new list which only has the names of the formats and also folds in the lengths - too be appended to "matches"
        for regex in matches:
            namematch.append(regex[1])
        withlen = [namematch,str(longestlen)]
        possformats.append(withlen)
#        lengths.append(longestlen)
    return possformats


def format_selector(possformats): #This function turns our list of possible formats for each variable into an output-ready list of one sas format
    chosenformats = []
    for variable in possformats:
        if variable[1] == "0":
            chosenformats.append("$CHAR10.")
        elif "MDYAMPM" in variable[0]:
            chosenformats.append("MDYAMPM.")
        elif "MMDDYY" in variable[0]:
            chosenformats.append("MMDDYY.")
        elif "N8601B" in variable[0]:
            chosenformats.append("N8601B.")
        elif "BEST" in variable[0]:
            chosenformats.append("BEST.")
        elif "HEX" in variable[0]:
            chosenformats.append("HEX.")
        elif "OCTAL" in variable[0]:
            chosenformats.append("OCTAL.")
        elif "BINARY" in variable[0]:
            chosenformats.append("BINARY.")
        elif "CHAR" in variable[0]:
            chosenformats.append("$CHAR"+variable[1]+".")
    return chosenformats

def variable_creator(variable_list):
    SASnames = []
    for name in enumerate(variable_list):
        if name[1] == "" or name[1] in ["_NULL_","_DATA_","_LAST_"]:
            tempname = "VAR"+str(name[0])
        else:
            tempname = name[1][:32]
            tempname = tempname.replace(" ", "_") #This section marks the agonizing process of removing prohibited characters from filenames
            tempname = tempname.replace("!", "_")
            tempname = tempname.replace("@", "_")
            tempname = tempname.replace("#", "_")
            tempname = tempname.replace("$", "_")
            tempname = tempname.replace("%", "_")
            tempname = tempname.replace("^", "_")
            tempname = tempname.replace("&", "_")
            tempname = tempname.replace("*", "_")
            tempname = tempname.replace("(", "_")
            tempname = tempname.replace(")", "_")
            tempname = tempname.replace("-", "_")
            tempname = tempname.replace("+", "_")
            tempname = tempname.replace("=", "_")
            tempname = tempname.replace("\\", "_")
            tempname = tempname.replace("|", "_")
            tempname = tempname.replace("}", "_")
            tempname = tempname.replace("{", "_")
            tempname = tempname.replace("]", "_")
            tempname = tempname.replace("[", "_")
            tempname = tempname.replace("'", "_")
            tempname = tempname.replace("\"", "_")
            tempname = tempname.replace(";", "_")
            tempname = tempname.replace(":", "_")
            tempname = tempname.replace("?", "_")
            tempname = tempname.replace("/", "_")
            tempname = tempname.replace(".", "_")
            tempname = tempname.replace(",", "_")
            tempname = tempname.replace(">", "_")
            tempname = tempname.replace("<", "_")
            tempname = tempname.replace("   ", "_")
        try:
            int(tempname[0])
            tempname = "_" + tempname[1:]
        except ValueError:
            tempname = tempname
        if tempname in SASnames:
            tempname = tempname[:31] + str(name[0])
        SASnames.append(tempname)
    return SASnames

def filepathcreator(origfile): #This unfortunately only works on Windows filesystems. Considering that SAS only runs on Windows, though, I'm not too torn up over that.
    base = "F:\\casework\\"
    case = origfile.split("casework\\",1)[1]
    casename = case.split("\\",)[0]
    if not os.path.exists(base + casename + "\\SAS"):
        os.makedirs(base + casename + "\\SAS")
    if not os.path.exists(base + casename + "\\SAS\\Data"):
        os.makedirs(base + casename + "\\SAS\\Data")
    if not os.path.exists(base + casename + "\\SAS\\Programs"):
        os.makedirs(base + casename + "\\SAS\\Programs")
    if not os.path.exists(base + casename + "\\SAS\\Output"):
        os.makedirs(base + casename + "\\SAS\\Output")
    savelocation = base + casename + "\\SAS\\Programs"
    liblocation = base + casename + "\\SAS\\Data"
    datasetname = origfile.split("\\")[-1]
    datasetname = datasetname.split(".")[0]
    tempname = datasetname[:32]
    tempname = tempname.replace(" ", "_")
    tempname = tempname.replace("!", "_")
    tempname = tempname.replace("@", "_")
    tempname = tempname.replace("#", "_")
    tempname = tempname.replace("$", "_")
    tempname = tempname.replace("%", "_")
    tempname = tempname.replace("^", "_")
    tempname = tempname.replace("&", "_")
    tempname = tempname.replace("*", "_")
    tempname = tempname.replace("(", "_")
    tempname = tempname.replace(")", "_")
    tempname = tempname.replace("-", "_")
    tempname = tempname.replace("+", "_")
    tempname = tempname.replace("=", "_")
    tempname = tempname.replace("\\", "_")
    tempname = tempname.replace("|", "_")
    tempname = tempname.replace("}", "_")
    tempname = tempname.replace("{", "_")
    tempname = tempname.replace("]", "_")
    tempname = tempname.replace("[", "_")
    tempname = tempname.replace("'", "_")
    tempname = tempname.replace("\"", "_")
    tempname = tempname.replace(";", "_")
    tempname = tempname.replace(":", "_")
    tempname = tempname.replace("?", "_")
    tempname = tempname.replace("/", "_")
    tempname = tempname.replace(".", "_")
    tempname = tempname.replace(",", "_")
    tempname = tempname.replace(">", "_")
    tempname = tempname.replace("<", "_")
    tempname = tempname.replace("   ", "_")
    datasetname = tempname
    return casename, savelocation, datasetname, liblocation