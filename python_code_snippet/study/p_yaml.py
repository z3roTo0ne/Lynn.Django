import yaml
import json

with open("test.yml") as fd:
    try:
        dataMap = yaml.load(fd)
        print dataMap
    except yaml.YAMLError:
        print "ERROR"


