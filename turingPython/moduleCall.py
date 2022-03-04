"""
This script is for practicing module calls from classModule.py script
"""


import sys
sys.path.append('~/techGit/turingPython')

from classModule import Animal
animal = Animal('dog', "wang...")
animal.greet()