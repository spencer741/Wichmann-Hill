'''
<Wichmann_Hill finished=true/>
<notes>
    Consists of three linear congruential generators with different prime moduli, 
    each of which is used to produce a uniformly distributed number between 0 and 1.
    These are summed, modulo 1, to produce the result.

    This function is a direct derivative of the original AS 183 generator by Wichmann and Hill.
    
    Here is a great article... https://jamesmccaffrey.wordpress.com/2016/05/14/the-wichmann-hill-random-number-algorithm/
    
    Previous issue:
        seed1, seed2, seed3 should be random from 1 to 30,000? -> answer from Wichmann Hill Fortran Code 
        INTEGER ARITHMETIC UP TO 30323 IS REQUIRED
        ... so I am assuming it can be over 30,000.
</notes>
'''
def Wichmann_Hill(seedlst, listlength):
    seed1 = seedlst[0]
    seed2 = seedlst[1]
    seed3 = seedlst[2]
    
    numlist = []
    for i in range(listlength):
       
        seed1 = 171 * seed1 % 30269
        seed2 = 172 * seed2 % 30307
        seed3 = 170 * seed3 % 30323

        numlist.append((float(seed1)/30269.0 + float(seed2)/30307.0 + float(seed3)/30323.0) % 1.0)
    #print(numlist[0:50])
    return numlist
