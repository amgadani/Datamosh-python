import code
import random
import argparse
import ntpath

def combine(iMovieTitle, pMovieTitle):
    f = open(iMovieTitle, 'r')
    g = open(pMovieTitle, 'r')

    firstVid = ntpath.splitext(ntpath.basename(iMovieTitle))[0]
    secondVid = ntpath.splitext(ntpath.basename(pMovieTitle))[0]
    outTitle = firstVid + "-" + secondVid + ".avi"
    outFile = open(outTitle, 'w')

    iFrameList = f.read().split('00dc')
    pFrameList = g.read().split('00dc')

    iframe = '0001b0'.decode('hex')
    iframes = []
    pframes = []

    firstPassed = False
    for index, frame in enumerate(iFrameList):
        if firstPassed == False:
            outFile.write(frame + '00dc')
            if frame[5:8] == iframe:
                firstPassed = True
        else: 
            if frame[5:8] == iframe:
                iframes.append(frame)

    firstPassed = False
    for index, frame in enumerate(pFrameList):
        if firstPassed == False:
            if frame[5:8] == iframe:
                firstPassed = True
        else:
            if frame[5:8] != iframe:
                pframes.append(frame)

    for index in range(min(len(iframes), len(pframes))):
        outFile.write(iframes[index] + '00dc')

        if len(pframes) > len(iframes):
            spacing = len(pframes)/len(iframes)
            for i in range(spacing):
                outFile.write(pframes[index*spacing+i] + '00dc')
        else:
            for i in range(15):
                outFile.write(pframes[index] + '00dc')

    outFile.close()

if __name__ == "__main__":
    iMovieTitle = '/Users/aashish/Documents/Programming/sources/videos/output.avi'
    pMovieTitle = '/Users/aashish/Documents/Programming/sources/videos/0001-0120.avi'


    parser = argparse.ArgumentParser()
    parser.add_argument("movieTitleA")
    parser.add_argument("movieTitleB")
    args = parser.parse_args()
    combine(args.movieTitleA, args.movieTitleB)
    combine(args.movieTitleB, args.movieTitleA)


