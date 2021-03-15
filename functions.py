def splittext(text, length=200):
    n = len(text)
    tokens = [' ', '\n']
    if n<length: 
        return text
    temp = numpy.array([(i, i//length) for i, c in enumerate(text) if c in tokens])
    return temp