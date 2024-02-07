#!/usr/bin/python
from os.path import expanduser
import datetime

print("Executed at " + str(datetime.datetime.now()) )
file = open('/home/uhalpern/Desktop/HERE.txt', 'a')
file.write("It worked!\n" + str(datetime.datetime.now()))
file.close()