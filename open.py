"""
21. open Function
open opens a file. Pretty simple, eh?
But much of the time, it is not used correctly.
"""

### Nieve Usage
f = open('photo.jpg', 'r+')
jpgdata = f.read()
f.close()

#: problem: f.close is only called if no errors are encountered.

### Improved Version
with open('photo.jpg', 'r+') as f:
    jpgdata = f.read()

### Modes
# r = read the file
# r+ = read and write to the file
# w = overwrite the file
# a = append to the file

### Mode Modifiers
# <mode>b = open the file in binary mode
# <mode>t = open the file in text mode

### EXAMPLE ###########################################################

import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))