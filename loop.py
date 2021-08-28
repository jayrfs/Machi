#from frames_stitcher import frames_stitcher
import os
import time
from scripts.frames_stitcher import stitchy_code

#log start time
start_time = time.perf_counter()

#add paths
inputPath = ".//input//"
outputPath = ".//output//"
extension = ".png"

#get chapter
list_of_files = os.listdir(inputPath)
print('''   



_|      _|                      _|        _|  
_|_|  _|_|    _|_|_|    _|_|_|  _|_|_|        
_|  _|  _|  _|    _|  _|        _|    _|  _|  
_|      _|  _|    _|  _|        _|    _|  _|  
_|      _|    _|_|_|    _|_|_|  _|    _|  _|  
''')
print("\nDetected folders in .\input:\n")
print("\t[+] - Input")
print("\t | ")
for files in list_of_files:
    print(f"\t └ {files}")
chapter = (input(f"\nChoose a folder to stitch or press enter to stitch all: "))

if chapter != "":
    try:
        stitchy_code(chapter)
    except:
        print('interation failed! skipping...')
        pass
else:
    for files in list_of_files:
        try:
            stitchy_code(int(files[:2]))
        except Exception as e:
            print(f'interation failed! skipping...\n{e}')
            pass

print(f"\nProcess completed in {time.perf_counter()-start_time} seconds.")
input('\nPress ENTER to exit')