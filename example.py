def complement(ds):
    cDNA ={'A':'T','C':'G','G':'C','T':'A'}
    ds = ds.upper()
    b = list(ds)
    letter = ""
    for s in b:
        if s in cDNA:
            letter = letter + cDNA[s]
        else:
            print("Invalid alphabet")
        return letter
def revComplement(ds):
    cmp = complement(ds)
    rc = ""
    i = len(ds) -1
    while(i>=0):
        rc = rc +cmp[i]
        i=i-1
    return rc
    print("Complement is:", complement(ds))
    print("reverse:", revComplement(ds))