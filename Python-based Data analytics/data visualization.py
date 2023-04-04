# @Author: Qingyuan Zheng, Ruijie Huang

import re

# Initialize the list
records = []

with open('expenses.txt', 'r') as f:
    record_list = f.readlines()

for entry in record_list:
    records.append(entry[:-1])

# 1a

pat = r'D'
for line in records:
     if re.search(pat, line) != None:
        print(line)

# 1b
pat = r'\''
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1c
pat = r'\"'
for line in records:
     if re.search(pat, line) != None:
        print(line)

# 1d
pat = r'^7'
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1e
pat = r'[rt]$'
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1f
pat = r'\.'
for line in records:
     if re.search(pat, line) != None:
        print(line)

# 1g
pat = r'r.*g'
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1h
pat = r'[A-Z][A-Z]'
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1i
pat = r','
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1j
pat = r',.*,.*,.*'
for line in records:
     if re.search(pat, line) != None:
         print(line)

# 1k
pat = r'[^vwxyz]'
for line in records:
     if re.search(pat, line) != None:
         print(line)

#1l
print ("                     ")
pat = r'^[1-9][0-9]+\.+[0-9][0-9]'
for line in records:
     if re.search(pat, line) != None:
         print(line)

#1m
print ("                     ")
pat = r'^[^,\n]*((,[^,\n]*){3}$)'
for line in records:
     if re.search(pat, line) != None:
         print(line)

#1n

print ("                     ")
pat = r'\('
for line in records:
     if re.search(pat, line) != None:
         print(line)
#1O

print ("                     ")
pat = r'^.*[1-9][0-9][0-9]\.[0-9][0-9]'
for line in records:
     if re.search(pat, line) != None:
         print(line)
#1p

print ("                     ")
pat = r'^.*\:[a-z]{4}\:.*$'
for line in records:
     if re.search(pat, line) != None:
         print(line)
#1q
print ("                     ")
pat = r"201703"
for line in records:
     if re.search(pat, line) != None:
         print(line)
#1r
print ("                     ")
pat = r'a.*b.*c'
for line in records:
     if re.search(pat, line) != None:
         print(line)

#1s

print ("                     ")
pat = r'(..).*\1.*\1.*\1'
for line in records:
     if re.search(pat, line) != None:
         print(line)
#1T
pat= r'[0-9](.*)a|a(.*)[0-9]'
for line in records:
     if re.search(pat, line) != None:
         print(line)
#1U
print ("                     ")
pat = r'^[^A-Z]*$'
for line in records:
     if re.search(pat, line) != None:
         print(line)

#1V
print ("                     ")
pat = r'd[a-z]i'
for line in records:
     if re.search(pat, line) != None:
         print(line)
 