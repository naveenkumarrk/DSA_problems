strs = ['flower', 'flow', 'flight']
strs1= ['ase','asdte','ere']

# horizontal Scannning
def prefixFinder(strs):
    base = strs[0]
    for i in range(1, len(strs)):
        while base != strs[i][0:len(base)]:
            base = base[0: len(base)-1]
        if base == "":
            return ""   
    return base

prefixFinder(strs1)

# vertical Scanning
strs = ['flower', 'flow', 'flight']
def prefixFinderV(strs):
    if strs == "":
        return ""
    for i in range(len(strs[0])):
        base = strs[0][i]
        for j in range(len(strs)):
            if i == len(strs[j]) or base != strs[j][i]:
                return strs[0][0:i]
    return strs[0]
prefixFinderV(strs)


#using string slicing 
def longestCommonPrefix(strs):
    strs = sorted(strs)
    ans = ""
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans+= first[i]            
    return ans
