# Import the os module, for the os.walk function
import sys  
reload(sys)  
sys.setdefaultencoding('iso-8859-1')
import os
from collections import OrderedDict
import json
import string
from subprocess import check_output
websettingPath = 'webpage-settings.yml'
# Set the directory you want to start from
rootDir = 'ITAME'
json_file = []
systemFileDictonnary = OrderedDict([])
dirNameList = []
subdirListList = []
fileListList = []
for dirName, subdirList, fileList in os.walk(rootDir):
    systemFileDictonnary[dirName] = subdirList
    
def generatePreambuleJSON() :
    scholdoc_command = []
    scholdoc_command.append('scholdoc ')
    scholdoc_command.append(websettingPath)
    scholdoc_command.append(' ')
    scholdoc_command.append('\"')
    scholdoc_command.append('preambule.md')
    scholdoc_command.append('\"')
    scholdoc_command.append(' --citeproc --bibliography resources/biblio.bib --csl resources/plos.csl --to=html')
    scholdoc_command.append(' --output=')
    scholdoc_command.append('\"')
    scholdoc_command.append('preambule.html')
    scholdoc_command.append('\"')
    check_output(''.join(scholdoc_command), shell=False).encode('iso-8859-1')
    print 'préambule OK !'
    
def generateDefaultJSON() :
    scholdoc_command = []
    scholdoc_command.append('scholdoc ')
    scholdoc_command.append(websettingPath)
    scholdoc_command.append(' ')
    scholdoc_command.append('\"')
    scholdoc_command.append('default.md')
    scholdoc_command.append('\"')
    scholdoc_command.append(' --citeproc --bibliography resources/biblio.bib --csl resources/plos.csl --to=html')
    scholdoc_command.append(' --output=')
    scholdoc_command.append('\"')
    scholdoc_command.append('default.html')
    scholdoc_command.append('\"')
    check_output(''.join(scholdoc_command), shell=False).encode('iso-8859-1')
    print 'default OK !'
    
def generateJSON(parent, root) :
    
    root_data = OrderedDict([])
    root_data["name"] = root.split('\\')[-1]
    root_data["parent"] = parent.split('\\')[-1]
    root_data["html"] = string.replace(root+'\\'+root_data["name"]+".html", '\\', '/') 
    children_data = []
    for child in systemFileDictonnary[root]:
        children_data.append(generateJSON(root,root+'\\'+child));
    if len(children_data)>0:
        root_data["_children"] = children_data
    scholdoc_command = []
    scholdoc_command.append('scholdoc ')
    scholdoc_command.append(websettingPath)
    scholdoc_command.append(' ')
    scholdoc_command.append('\"')
    scholdoc_command.append(root)
    scholdoc_command.append('\\')
    scholdoc_command.append(root_data["name"])
    scholdoc_command.append('.md')
    scholdoc_command.append('\"')
    scholdoc_command.append(' --citeproc --bibliography resources/biblio.bib --csl resources/plos.csl --to=html')
    scholdoc_command.append(' --output=')
    scholdoc_command.append('\"')
    scholdoc_command.append(root)
    scholdoc_command.append('\\')
    scholdoc_command.append(root_data["name"])
    scholdoc_command.append('.html')
    scholdoc_command.append('\"')
    check_output(''.join(scholdoc_command), shell=False).encode('iso-8859-1')
    print '%s OK !' %root
    return root_data;

generatePreambuleJSON();
generateDefaultJSON();
data = generateJSON('null',rootDir)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, encoding='iso-8859-1', indent=4)    
