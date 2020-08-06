#!/usr/bin/python

import copy
import json
from os import listdir
from os.path import isfile, isdir, join, expanduser
import re

new_list = list()
new_file_dict = {
    "uid": "",
    "path": "",
    "title": "",
    "subtitle": "",
    "arg": "",
    "match": "",
    "icon": {
        "path": "./vscode.png"
    }
}

myPath = "~/TargetCodeDirectory/"
realPath = expanduser(myPath)

# onlyFiles = [myPath + f for f in listdir(realPath) if isfile(join(realPath, f)) and f.find(".code-workspace") != -1]
onlyDirs = [myPath + f for f in listdir(realPath)]

arr = {
    "items": []
}
i=0
for filename in onlyDirs:

    new_list = copy.deepcopy(new_file_dict)
    name = filename.replace(myPath, "").replace(".code-workspace", "")

    new_list['uid'] = filename
    new_list['path'] = filename
    new_list['title'] = name
    new_list['subtitle'] = filename
    new_list['arg'] = filename
    # Split out any upper case words:
    upperWords = re.sub( r"([A-Z])", r" \1", name).split()
    new_list['match'] = " ".join(upperWords) + " " + name.replace("-", " ").replace("_", " ")
    arr['items'].append(new_list)

print(json.dumps(arr))