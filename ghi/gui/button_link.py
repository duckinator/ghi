import tkinter
import webbrowser

class ButtonLink(tkinter.Button):
    def __init__(self, root, text=None, href=None):
        super().__init__(
            root,
            text=text,
            command=self.callback
        )
        self.href = href

    def callback(self):
        webbrowser.open_new_tab(self.href)
