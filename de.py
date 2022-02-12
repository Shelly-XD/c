import re, sys

x = open(sys.argv[1]).read()
a=sorted(map(lambda x: (int(x[0]), x[1]), re.findall(r"\/\*\s+\"{}\.(?:py|pyx)\"\:([0-9]*)((.*?)|\n)\s+\*\/".format(sys.argv[1].strip('.c')),x)), key=lambda x:x[0])
dat = []
func = False
fung = []
for j, k in enumerate(a):
    val = k[1].strip().splitlines()
    for v in val:
        if v.strip().startswith('*'):
            var = (' ' + v.replance('# <<<<<<<<<<<<<','').strip()) [3:]
            if var not in dat:
                dat.append(var)
print('\n'.join(dat))
