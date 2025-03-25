#def defines DNA
def complement(DNA):
    complement_DNA = ''
    #Assigns strings to a different string
    for nucleotide in DNA:
        if nucleotide == 'A':
            complement_DNA=complement_DNA+'T'
        elif nucleotide=='T':
            complement_DNA=complement_DNA+'A'
        elif nucleotide=='C':
            complement_DNA=complement_DNA+'G'
        elif nucleotide=='G':
            complement_DNA=complement_DNA+'C'
    return complement_DNA
complement('ACTG')
def reverse_complement(DNA):
    #::-1 slices the string and has to go through from the start to end of the list
    DNA=DNA[::-1]
    result=complement(DNA)
    return result
reverse_complement('ACTG')


    

