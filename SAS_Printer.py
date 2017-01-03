def programprinter(chosenformats, SASnames, casename, savelocation, datasetname, liblocation, filepath):
    sasprogram = open(savelocation + "//Read in " + datasetname +".sas","w")
    sasprogram.write("libname data \"" +liblocation+"\";\n")
    sasprogram.write("title1 \"" + casename + "\";\n")
    sasprogram.write("footnote \"DRAFT -- Confidential Attorney Work Product\";\n")
    sasprogram.write("proc datasets lib = work nolist kill; quit; options error = 5 nonumber nodate nolabel mergenoby = warn msglevel = imprint;\n")
    sasprogram.write("\n")
    sasprogram.write("data " + datasetname + ";\n")
    sasprogram.write("  infile \"" + filepath + "\" LRECL = 32767 DLM = ',' DSD MISSOVER FIRSTOBS = 2;\n")
    sasprogram.write("  informat\n")
    for column in enumerate(SASnames):
        sasprogram.write("    "+ SASnames[1] + " " +  chosenformats[sasnames[0]]+"\n")
    sasprogram.write("  ;\n")
    sasprogram.write("  format\n")
    for column in enumerate(SASnames):
        sasprogram.write("    "+ SASnames[1] + " " +  chosenformats[sasnames[0]]+"\n")
    sasprogram.write("  ;\n")
    sasprogram.write("  input\n")
    for column in enumerate(SASnames):
        linestr = "    "+ SASnames[1] + " "
        if "CHAR" in chosenformats[sasnames[0]]:
            linestr += "$"
        sasprogram.write(linestr+"\n")
    sasprogram.write("  ;\n")
    sasprogram.write("\n")
    sasprogram.write("\\*\n")
    sasprogram.write("data data." + datasetname +";\n")
    sasprogram.write("  set " + datasetname + ";\n")
    sasprogram.write("run;\n")
    sasprogram.write("*\\\n")

    sasprogram.close()



    input
        CASE_ID $
        ACCIDENT_YEAR $
        PROC_DATE
        JURIS $
        COLLISION_DATE
    ;
run;

/*
data data.collisions;
	set collisions;

run;
*/