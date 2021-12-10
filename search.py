# import
import shutil
import os
import os.path
import pathlib
import xml.etree.ElementTree as ET
import codecs


# searchedterms = []


# ### get input ###
print("please enter the full exact path of the directory to search (no spaces)")
path = input("> ")

# usertag = ""

# print("if you want to add tags to search for, enter them here. otherwise leave this blank and press enter")


# def tag():
#     usertag = input("> ")
#     if usertag:
#         tag()
#     else:
#         return usertag


# ### execute ###
# tag()
print("enter the phrase you want to find")
text = input("> ")

flag = 0
for path, dir, files in os.walk(path):
    for file in files:
        if not file.endswith(".xml"):
            pass
        else:
            file = path + "/" + file
            # for (j, i) in ET.iterparse(file):
            #     tag = i.tag
            #     tag2 = tag.replace(
            #         r"{http://www.oracle.com/obis/repository}", "")
            #     searchedterms.append(tag2)
            #     searchedterms.sort()
            index = 0
            with open(file, "r") as openfile:
                for line in openfile:
                    index += 1
                    # for tag in searchedterms:
                    #     if usertag != tag or usertag is not tag:
                    #         searchedterms.remove(tag)
                    # for i in searchedterms:
                    if text.lower().strip() in line.lower().strip():
                        flag += 1
                        print("success at line {} in {}".format(
                            index, file))


if flag == 0:
    print("found nothing")
