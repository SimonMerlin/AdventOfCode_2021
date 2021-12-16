import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

binary = bin(int(lines[0], 16))[2:].zfill(len(lines[0])*4)

vCpt = 0

def decode(binary, parsingIndex, isSubPacket):
    startParse = parsingIndex
    v = int(binary[parsingIndex:parsingIndex+3], 2)
    t = int(binary[parsingIndex+3:parsingIndex+6], 2)
    parsingIndex += 6
    if t == 4: #literal value
        endPacket = False
        packetValue = ''
        valueCpt = 0
        while not endPacket:
            nextSlice = binary[parsingIndex:parsingIndex+5]
            if nextSlice[0] == '1': # not the last slice
                packetValue += nextSlice[1:]
            else:
                endPacket = True
                packetValue += nextSlice[1:]
            valueCpt += 1
            parsingIndex += 5
        if(not isSubPacket):
            trailingZero = 0 if (parsingIndex-startParse)%4 == 0 else 4 - ((parsingIndex-startParse)%4)
            parsingIndex += trailingZero -1
        return v, parsingIndex
    else:
        lengthTypeId = binary[parsingIndex:parsingIndex+1]
        parsingIndex += 1
        if lengthTypeId == '0': # next 15 bits are length of subpacket
            lengthSubpacket = int(binary[parsingIndex:parsingIndex+15], 2)
            parsingIndex += 15
            startSubpacketIndex = parsingIndex
            while parsingIndex-startSubpacketIndex < lengthSubpacket:
                subV, subParsingIndex = decode(binary, parsingIndex, True)
                v += subV
                parsingIndex = subParsingIndex
        else: # next 11 bits are the number of subpackets
            nbSubpackets = int(binary[parsingIndex:parsingIndex+11], 2)
            parsingIndex += 11
            for _ in range(nbSubpackets):
                subV, subParsingIndex = decode(binary, parsingIndex, True)
                v += subV
                parsingIndex = subParsingIndex
        if(not isSubPacket):
            trailingZero = 0 if (parsingIndex-startParse)%4 == 0 else 4 - ((parsingIndex-startParse)%4)
            parsingIndex += trailingZero -1
        return v, parsingIndex


print(decode(binary, 0, False)[0])

