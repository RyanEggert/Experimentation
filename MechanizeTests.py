# MechanizeTests.py

import re
from mechanize import Browser

br = Browser()
br.open("http://www.google.com/")
print br.title()
print br.read()