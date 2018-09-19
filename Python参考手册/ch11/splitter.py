def split(line, types=None, delimiter=None):
    """ Slits a line of text and optionally performs type conversions.
        ...
    """
    fields = line.split(delimiter)
    if types:
        fields = [ ty(val) for ty,val in zip(types,fields) ]
    return fields