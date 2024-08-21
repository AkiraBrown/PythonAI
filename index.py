import os
from datetime import datetime
from PIL import Image
# import PIL
import math

import PIL.Image

# file_location = input("Please provide a file: ") 
stats = os.stat("./test.txt")

def handleDate(timeStamp):
    targetTime = math.trunc(timeStamp)
    print(targetTime)
    date = targetTime
    altDate =  datetime.fromtimestamp(date)
    return altDate
    

modifyDate = handleDate(stats.st_mtime)
createdDate = handleDate(stats.st_ctime)

img = Image.open("./abstract_tree.png")
print(img._getexif())

print(modifyDate, createdDate)


print(list(stats))
print(stats.st_creator)
