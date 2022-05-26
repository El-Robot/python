from copy import copy
import os
import sys
from pathlib import Path

def main():

    args = sys.argv

    cancelationComment = "qqq" # string
    copyFromDir = Path(args[1]) # directory to copy from

    copyDictionary = {} 

    # copy 
    for copytFromFile in copyFromDir.iterdir(): # for each file in dir
        if copytFromFile.is_file():
            with open(copytFromFile, 'r') as f:
                copyThis = ""
                currLine = ""
                while cancelationComment not in currLine : # at each line copy until cancelation
                    currLine = f.readline()
                    copyThis += currLine

                    if currLine == "": # in case there is no comment, do not copy
                        copyThis = "NO COMMENT"
                        break

                if copyThis != "NO COMMENT":
                    copyDictionary[copytFromFile.name] = copyThis

                print(f"{copytFromFile.name}:\n{copyThis}")

    # replacements
    index = 2
    while index < len(args):
        copyIntoDir = Path(args[index]) # directoy to copy into

        for copyIntoFile in copyIntoDir.iterdir(): # for each file in dir
            # find last #include
            lastInclude = 0
            if copyIntoFile.is_file() and copyIntoFile.name in copyDictionary:
                with open(copyIntoFile, 'r+') as f:
                    currLine = ""
                    lineNumber = 1
                    for line in f.readlines():
                        if "#include" in line:
                            lastInclude = lineNumber
                        lineNumber += 1

                    # remove old
                    lines = f.readlines()
                    print(lines)
                    f.seek(0)
                    f.truncate()
                    f.writelines(lines[lastInclude:])
                    print(lines[lastInclude:])

                    # paste
                    oldInfo = f.read()
                    f.write(copyDictionary[copyIntoFile.name] + oldInfo)

        index += 1


if __name__ == "__main__":
    main()
