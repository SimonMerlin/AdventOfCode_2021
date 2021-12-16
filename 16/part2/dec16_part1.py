import sys
import os
f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

binary = bin(int(lines[0], 16))[2:].zfill(len(lines[0])*4)
vCpt = 0

def decode(binary, parsingIndex, isSubPacket):
    packetValue = None
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
        return int(packetValue, 2), parsingIndex
    else:
        lengthTypeId = binary[parsingIndex:parsingIndex+1]
        parsingIndex += 1
        if lengthTypeId == '0': # next 15 bits are length of subpacket
            lengthSubpacket = int(binary[parsingIndex:parsingIndex+15], 2)
            parsingIndex += 15
            startSubpacketIndex = parsingIndex
            while parsingIndex-startSubpacketIndex < lengthSubpacket:
                subPacketValue, subParsingIndex = decode(binary, parsingIndex, True)
                packetValue = compute(t, subPacketValue, packetValue)
                parsingIndex = subParsingIndex
        else: # next 11 bits are the number of subpackets
            nbSubpackets = int(binary[parsingIndex:parsingIndex+11], 2)
            parsingIndex += 11
            for _ in range(nbSubpackets):
                subPacketValue, subParsingIndex = decode(binary, parsingIndex, True)
                packetValue = compute(t, subPacketValue, packetValue)
                parsingIndex = subParsingIndex
        if(not isSubPacket):
            trailingZero = 0 if (parsingIndex-startParse)%4 == 0 else 4 - ((parsingIndex-startParse)%4)
            parsingIndex += trailingZero -1
        return packetValue, subParsingIndex

def compute(opType, value, acc):
    if opType == 0:
        return acc + value if acc != None else value
    elif opType == 1:
        return acc * value if acc != None else value
    elif opType == 2:
        return min(acc, value) if acc != None else value
    elif opType == 3:
        return max(acc, value) if acc != None else value
    elif opType == 5:
        if acc == None:
            return value
        else:
            return 1 if acc > value else 0
    elif opType == 6:
        if acc == None:
            return value
        else:
            return 1 if acc < value else 0
    elif opType == 7:
        if acc == None:
            return value
        else:
            return 1 if acc == value else 0
    else:
        raise Exception("Unknown operation type : " + opType)


print(decode(binary, 0, False)[0])

