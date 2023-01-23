# output format:
# \midrule
# \multirow[m]{1}{*}
# {VAE}	
# & SMILES
# & ZINC		
# & \cite{Jaechang2018}
# \\

# input format:
# VAE  & SMILES  & ZINC   &  \cite{Jaechang2018} \\ \hline 

import re 
from pprint import pprint 
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

inputFile=open("./table.txt","r")
file=inputFile.read()
inputFile.close()
file=file.split("\n")
file=[x.rstrip(" ").removesuffix("\\\\ \\hline").rstrip(" ") for x in file]
file=[i.split("&") for i in file]
file=[[j.strip(" \t") for j in i] for i in file]
pprint(file[1])
output=""
for i in file:
    output+="\\midrule\n\\multirow[m]{1}{*}\n"+"{{{}}}\n& {}\n& {}\n& {} \\\\".format(i[0],i[1],i[2],i[3])+"\n\n"
outputFile=open("TableOutput.txt","w+")
outputFile.write(output)
outputFile.close()


