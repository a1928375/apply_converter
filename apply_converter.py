def make_converter(match, replacement):
    return [match, replacement]

def apply_converter(converter, string):
    while string.find(converter[0])!=(-1):
        start=string.find(converter[0])
        end=start+len(converter[0])
        string=string[:start]+converter[1]+string[end:]
        
    return string

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
