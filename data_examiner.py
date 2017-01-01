# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:40:13 2016

@author: RKupyn
"""

import re


def datareader(datalist):
    possformats = []
    lengths = []
    best = re.compile("^\d*\.?\d*$")
    BINARY = re.compile("^[0|1]*$")
    CHAR = re.compile("*")
    HEX = re.compile("^[\d|A-F]*$")
    OCTAL = re.compile("^[0-7]*$")
    N8601B_DUR_1 = re.compile("^P\d{4}-\d{2}-\d{2}T\d{1,2}:\d{1,2}:\d{1,2}\.?\d*$")
    N8601B_DUR_2 = re.compile("^P\d{4}\d{2}\d{2}T\d{1,2}\d{1,2}\d{1,2}$")
    N8601B_DUR_3 = re.compile("^P\d{1,4}y\d{1,2}m\d{1,2}dT\d{1,2}h\d{1,2}m\d{1,2}\.?\d*s$")
    N8601B_DUR_4 = re.compile("^P\d+W$")
    N8601B_INT_1 = re.compile("^\d{4}-\d{2}-\d{2}T\d{1,2}:\d{1,2}:\d{1,2}\/\d{4}-\d{2}-\d{2}T\d{1,2}:\d{1,2}:\d{1,2}$")
    N8601B_INT_2 = re.compile("^\d{8}T\d{6,}\/\d{8}T\d{6,}$")
    N8601B_INT_3 = re.compile("^P\d{1,4}y\d{1,2}M\d{1,2}dT\d{1,2}h\d{1,2}m\d{1,2}\.?\d*s\/\d{1,4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}\.?\d*$")
    N8601B_INT_4 = re.compile("^\d{1,4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}\.?\d*\/P\d{1,4}y\d{1,2}M\d{1,2}dT\d{1,2}h\d{1,2}m\d{1,2}\.?\d*s$")
    N8601B_DT_1 = re.compile("^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.?\d*$")
    N8601B_DT_2 = re.compile("^\d{4}\d{2}\d{2}T\d{2}\d{2}\d{2}\.?\d*$")
    MDYAMPM = re.compile("^[0-1]?[0-9]\/[0-3]?[0-9]\/[12]?[0-9]?[0-9][0-9].\d{1,2}:\d{1,2}:\d{1,2}.*$")
    MMDDYY = re.compile("^[0-1]?[0-9]\/[0-3]?[0-9]\/[12]?[0-9]?[0-9][0-9]$")
    """
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
    regexlist = [best,BINARY,CHAR,HEX,OCTAL,N8601B_DUR_1,N8601B_DUR_2,N8601B_DUR_3,N8601B_DUR_4,N8601B_INT_1,N8601B_INT_2,N8601B_INT_3,N8601B_INT_4,N8601B_DT_1,N8601B_DT_2,MDYAMPM,MMDDYY]
    for variable in datalist:
        matches = regexlist
        longestlen = 0
        for entry in variable:
            if entry == "":
            else:
                longestlen = max(longestlen,len(entry))
                tempmatch = []
                for regex in matches:
                    if regex.match(entry):
                        tempmatch.append(regex)
                matches = tempmatch
        possformats.append(matches)
        lengths.append(longestlen)
    return possformats, lengths
