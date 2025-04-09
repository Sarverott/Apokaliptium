import tokenize
import re

with tokenize.open('readme.txt') as f:
    print(", ".join(set([x.string for x in tokenize.generate_tokens(f.readline) if  re.match('^[\w\d]+$', x.string)])))