import os
from pathlib import Path

def calcArea(left: int, top: int, width: int, height: int) -> str:
    """
    Calculate the area parameter for a style string based on 
    initial left and top position, and the height and width of the area.
    """
    return f"area: {left}px, {top}px, {left+width}px, {top+height}px; "

class Area:
    left = 0
    top = 0
    width = 0
    height = 0
    relative_left = 0
    relative_top = 0

    def __init__(self, left = 0, top = 0, width = 10, height = 10):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def as_style(self) -> str:
        """
        Gets the style string representing this area.
        E.g. 'area: 10px, 20px, 100px, 50px' would represent a box with a left bound of 10 pixels, 
        a top bound of 20 pixels, a right bound at 100 pixels, and a bottom bound at 50 pixes.
        """
        return calcArea(self.left + self.relative_left, self.top + self.relative_top, self.width, self.height)
    
    def set_relative_to(self, parent):
        """
        Change the position of the area to be relative to another area.
        Useful for nested GUI elements.
        """
        self.relative_left = parent.left
        self.relative_top = parent.top

def buildArea(left: int, top: int, width: int, height: int) -> Area:
    a = Area(left, top, width, height)
    return a
def getPath()->str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path
def getFullPath(mission_dir,rel_path)->str:
    p = os.path.join(mission_dir,rel_path)
    return p
def toAbsPath(path:str)->str:
    return os.path.abspath(path)
def checkFile(file:str) -> bool:
    return os.path.exists(os.path.abspath(file))
def getRelPath(file,folder):
    return os.path.relpath(folder,file)
