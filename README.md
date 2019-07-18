# apply_converter

For this question you need to define two procedures: 

make_converter(match, replacement)
Takes as input two strings and returns a converter. It doesn't have to make a specific type of thing. It can return anything you would find useful in apply_converter.

apply_converter(converter, string)
Takes as input a converter (produced by make_converter), and a string, and returns the result of applying the converter to the input string. This replaces all occurrences of the match used to build the converter, with the replacement. It keeps doing replacements until there are no more opportunities for replacements.
