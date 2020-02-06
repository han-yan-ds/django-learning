"""
__file__ shows the full relative path (relative to the "cd" directory)
"""

import os

print("Printing full relative path name now (WITH filename)")
print(__file__)

print("Printing full relative path name now (WITHOUT filename)")
print(os.path.dirname(__file__))

print("Printing the absolute path now (WITH filename)")
print(os.path.abspath(__file__))

print("Printing the absolute path PLUS a subfolder that I made up")
print(os.path.join(os.path.abspath(__file__), 'madeupfolder'))