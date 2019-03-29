def pluralize(number, singular, plural=None):
    """Helper function for getting the appropriate singular or plural
    variant of a word or phrase.

    pluralize(0, 'awoo')         #=> "0 awoos"
    pluralize(1, 'awoo')         #=> "1 awoo"
    pluralize(2, 'awoo')         #=> "2 awoos"
    pluralize(1, 'box', 'boxen') #=> "1 box"
    pluralize(2, 'box', 'boxen') #=> "2 boxen"
    """
    if plural is None:
        plural = singular + 's'

    if number == 1:
        ret = singular
    else:
        ret = plural

    return '{} {}'.format(number, ret)


def listbox_width(items, max_width=30):
    """Calculate the width for a listbox, based on a list of strings and a
    maximum width.

    listbox_width(["foo", "bar", "asdf"], 10)       #=> 4 ("asdf")
    listbox_width(["foo", "asdf", "beep boop"], 5)  #=> 5 (max_width)
    """
    max_item_width = max(map(len, items))
    return min(max_width, max_item_width)
