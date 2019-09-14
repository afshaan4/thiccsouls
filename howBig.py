'''
A scale ruler for a camera

distance values are read from an arduino with an ultrasonic rangefinder

I assume that the cameras resolution is 600X480 for drawing the line, change
the arguments to cv2.line() to fit your cameras resolution
'''

import cv2
import sys
import serial

class App:
    def __init__(self, videoSrc, serialPort, baudRate = 9600):
        self.cam = cv2.VideoCapture(int(videoSrc))
        # for talking to the arduino
        self.arduino = serial.Serial(str(serialPort), int(baudRate), timeout=.1)
        # camera parameters
        self.length = 10 # size of length in cm
        self.focalLen = 0.6
        self.pixelsPerCM = 1950


    # USE ONE UNIT FOR ALL ARGS, cm in this case
    def calculateImageSize(self, size, f, dist):
        # image size = object size * focal length / distance to object
        if dist < 1:
            return 0
        else:
            return (size * f / dist)


    def run(self):
        calculatedLength = 0
        distance = 0
        running = True
        while running:
            ret, frame = self.cam.read()
            distance = self.arduino.readline()[:-2]

            if distance:
                # only want the numbers
                distance = str(distance)
                distance = distance.split('\'')
                print(distance[1])

                # calculate the length of the line
                calculatedLength = self.calculateImageSize(self.length, self.focalLen, int(distance[1]))
                # convert the lines length to pixels
                calculatedLength *= self.pixelsPerCM
                print(calculatedLength)

            # draw the line
            cv2.line(frame, (10, 470), (10 + int(calculatedLength), 470), (55, 12, 255), 2) # image ,start, end, color, width
            cv2.imshow("BRUH", frame)
            k = cv2.waitKey(30)
            if k == 27:
                running = False


def main():
    try:
        videoSrc = sys.argv[1]
        serialPort = sys.argv[2]
    except:
        videoSrc = 0
        print('WARNING: serial port not specified')
            
    App(videoSrc, serialPort).run()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()