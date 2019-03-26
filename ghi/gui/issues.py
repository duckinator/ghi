import tkinter

from .button_link import ButtonLink
from .utils import pluralize

class Issues(tkinter.Frame):
    def __init__(self, root, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.ghi = ghi

