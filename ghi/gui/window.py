from .. import config

def load_state(root):
    if config.exists('window_state.json'):
        geometry = config.load('window_state.json')['geometry']
    else:
        geometry = center_geometry(root)

    root.geometry(geometry)
    root.update_idletasks()


def save_state(root):
    config.save('window_state.json', {'geometry': root.geometry()})


def center_geometry(root, width=600, height=400):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the required positions to center the window.
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    return '%dx%d+%d+%d' % (width, height, x, y)
