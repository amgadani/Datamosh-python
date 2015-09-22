import code
import random


movieTitle = '/Users/aashish/Documents/Programming/sources/videos/0001-0120.avi'
f = open(movieTitle, 'r')
outFile = open('a.avi', 'w')

inputFile = f.read()
frames = inputFile.split('00dc')

iframe = '0001b0'.decode('hex')
firstPassed = False
printedFrames = 0

for index, frame in enumerate(frames):
    #outFile.write(frame + '00dc')
    if firstPassed == False:
        outFile.write(frame + '00dc')
        printedFrames += 1
        print 'FALSE ' + str(printedFrames)

        if frame[5:8] == iframe:
            print 'FIRST ' + str(index)
            firstPassed = True
    else:
        if frame[5:8] != iframe:
            printedFrames += 1
            for i in range(15):
                outFile.write(frame + '00dc')

print 'printed frames: ' + str(printedFrames) + "  skipped frames: " + str(len(frames)-printedFrames)

outFile.close()
