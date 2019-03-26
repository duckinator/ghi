# pluralize(0, 'awoo')         #=> "0 awoos"
# pluralize(1, 'awoo')         #=> "1 awoo"
# pluralize(2, 'awoo')         #=> "2 awoos"
# pluralize(1, 'box', 'boxen') #=> "1 box"
# pluralize(2, 'box', 'boxen') #=> "2 boxen"
def pluralize(n, singular, plural=None):
    if plural is None:
        plural = singular + 's'

    if n == 1:
        ret = singular
    else:
        ret = plural

    return '{} {}'.format(n, ret)
