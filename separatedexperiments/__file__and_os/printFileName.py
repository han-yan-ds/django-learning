"""
__file__ shows the full relative path (relative to the "cd" directory)
"""

import os

print("Printing full relative path name now (WITH filename)")
print(__file__)

print("Printing full relative path name now (WITHOUT filename)")
print(os.path.dirname(__file__))