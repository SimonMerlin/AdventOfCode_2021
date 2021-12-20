import sys
import os
import re
import math
from Scanner import Scanner
from Beacon import Beacon

f = open(os.path.join(sys.path[0], './data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

scanners = []
rotations = [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]
permutations = [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]

def parseScanners():
    declareScannerRegex = r"--- scanner \d+ ---"
    scanner = None
    for i in range(len(lines)):
        if re.match(declareScannerRegex, lines[i]) != None:
            id = int(re.findall(r"\d+", lines[i])[0])
            if id == 0:
                scanner = Scanner(id,0,0,0)
            else:
                scanner = Scanner(id)
        elif lines[i] != "":
            line = lines[i].split(',')
            b = Beacon(int(line[0]), int(line[1]), int(line[2]))
            scanner.addBeacon(b)
        else:
            scanners.append(scanner)
            scanner = None
    scanners.append(scanner)
    return scanners

def getPossibleOriginFromscannerAndBeacon(scanner, bReference, bTest, rot):
    originX = rot[0]*bTest.x - (bReference.x - scanner.x)
    originY = rot[1]*bTest.y - (bReference.y - scanner.y)
    originZ = rot[2]*bTest.z - (bReference.z - scanner.z)
    return originX, originY, originZ

def getBeaconPermutation(b, perm):
    if perm == (0,1,2):
        return b
    elif perm == (1,0,2):
        return Beacon(b.y, b.x, b.z)
    elif perm == (2,1,0):
        return Beacon(b.z, b.y, b.x)
    elif perm == (0,2,1):
        return Beacon(b.x, b.z, b.y)
    elif perm == (1,2,0):
        return Beacon(b.y, b.z, b.x)
    elif perm == (2,0,1):
        return Beacon(b.z, b.x, b.y)
    

def getVectors(scanner1, scanner2):
    if scanner1.x == None and scanner1.y == None:
        raise Exception("Don't know scanner1 coordinates")
    translationVector = None
    for perm in permutations:
        for rot in rotations:
            beaconsCoordinatesMap = dict()
            originPointMapping = dict()
            for bReference in scanner1.beacons:
                for b in scanner2.beacons:
                    bPrime = getBeaconPermutation(b, perm)
                    origin = getPossibleOriginFromscannerAndBeacon(scanner1, bReference, bPrime, rot)
                    l = originPointMapping.get(origin, [[], []])
                    l[0].append(bReference)
                    l[1].append(b)
                    originPointMapping[origin] = l
                    beaconsCoordinatesMap[origin] = beaconsCoordinatesMap.get(origin, 0) + 1
            for key in beaconsCoordinatesMap.keys():
                if beaconsCoordinatesMap[key] >=12:
                    translationVector = (key[0]*-1, key[1]*-1, key[2]*-1)
                    return (translationVector, rot, perm)
    return None

def transformBeaconFromVector(scanner, vector, rot, permutation):
    for b in scanner.beacons:
        bPrime = getBeaconPermutation(b, permutation)
        b.x = (bPrime.x * rot[0]) + vector[0]
        b.y = (bPrime.y * rot[1]) + vector[1]
        b.z = (bPrime.z * rot[2]) + vector[2]

def getManhattanDistance(scanner1, scanner2):
    return math.fabs(scanner1.posx - scanner2.posx) + math.fabs(scanner1.posy - scanner2.posy) + math.fabs(scanner1.posz - scanner2.posz)


scanners= parseScanners()
scanner0 = None

unknowReferenceScanner = []
for s in scanners:
    if s.id == 0:
        scanner0 = s
    else:
        unknowReferenceScanner.append(s)

scanner0.setTranslationVector((0,0,0))
scanner0.setPosition((0,0,0))
scanner0.setRotationVector((1,1,1))
scanner0.setPermutationVector((0,1,2))
referenceScanners = [scanner0]

while len(unknowReferenceScanner) > 0:
    for rc in referenceScanners:
        for scanner in unknowReferenceScanner:
            vectors = getVectors(rc, scanner)
            if vectors != None:
                translation, rotation, permutation = vectors
                print("Scanner {} : {} ; {}".format(scanner.id, translation, rotation))
                transformBeaconFromVector(scanner, translation, rotation, permutation)
                scanner.setOriginToZero()
                scanner.setTranslationVector((0,0,0))
                scanner.setPosition(translation)
                scanner.setRotationVector((1,1,1))
                scanner.setPermutationVector((0,1,2))
                referenceScanners.append(scanner)
                unknowReferenceScanner = [s for s in unknowReferenceScanner if s.id != scanner.id]

maxDistance = 0
for s1 in referenceScanners:
    for s2 in referenceScanners:
        if s1.id != s2.id:
            distance = getManhattanDistance(s1, s2)
            if distance > maxDistance:
                maxDistance = distance
print("Max distance : {}".format(maxDistance))


            
