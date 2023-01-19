# og format:
# @article{
#   mullard2016biotech,
#   title={Biotech R\&D spend jumps by more than 15\%},
#   author={Mullard, Asher},
#   journal={Nature Reviews Drug Discovery},
#   volume={15},
#   number={7},
#   pages={447--448},
#   year={2016},
#   publisher={Nature Publishing Group}
# }
# }

# resultant format:
# \bibitem[Author1(year)]{ref-journal}
# Author 1, T. The title of the cited article. {\em Journal Abbreviation} {\bf 2008}, {\em 10}, 142--149.
import re
from pprint import pprint
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

inputFile=open("./data.txt","r")
file=inputFile.read()
inputFile.close()
file=re.split("@article",file,flags=re.IGNORECASE)
file.pop(0);
file=[re.sub('[{}\t:,]','',x.rstrip("\n")[1:-2]).split("\n") for x in file]
for x in range(len(file)):
    tempDict={}
    tempDict["refTitle"]=file[x][0]
    for y in range(len(file[x])):        
        file[x][y]=file[x][y].strip()
        file[x][y]=file[x][y].split("=")
        file[x][y]=[t.strip() for t in file[x][y]]
        # print(file[x][y])        
        if len(file[x][y])>1:
            tempDict[file[x][y][0].lower()]=file[x][y][1]
    file[x]=tempDict
    # check if key exists and add empty key if it doesnt
    if "refTitle" not in file[x].keys():
        file[x]["refTitle"]=""
    if "author" not in file[x].keys():
        file[x]["author"]=""
    if "title" not in file[x].keys():
        file[x]["title"]=""
    if "journal" not in file[x].keys():
        file[x]["journal"]=""
    if "year" not in file[x].keys():
        file[x]["year"]=""
    if "volume" not in file[x].keys():
        file[x]["volume"]=""
    if "pages" not in file[x].keys():
        file[x]["pages"]=""    
output=""
for i in range(len(file)):
    output+=r"\bibitem[{}({})]{{{}{}}}".format(file[i]["refTitle"][:-4],file[i]["year"],file[i]["refTitle"][:-4],file[i]["year"])+"\n"+r"{}, T. {}. {{\em {}}} {{\bf {}}}, {{\em {}}}, {}".format(file[i]["author"],file[i]["title"],file[i]["journal"],file[i]["year"],file[i]["volume"],file[i]["pages"],)+"\n\n"
outputFile=open("output.txt","w+")
outputFile.write(output)
outputFile.close()
