# thiccsouls

A scale ruler like on google maps but for a camera.

Thats a scale ruler:

![scale ruler](https://user-images.githubusercontent.com/20749736/64703783-bcf27780-d4ca-11e9-80a7-e58286589bbf.jpg)

# The maths

To be able to calculate the size of something in an image you need:
* the things distance from the camera
* the things actual size
* the focal length of your camera
* use ONE UNIT for all that so cm or mm or m or whatever

Then the size of a thing in the image is:
```
thing in image size = size * focal length / distance
```

But to be able to draw a scale ruler we need to know the size of the thing in 
*pixels*, to do that just multiply the result of the previous formula with the
`pixels-per-unit` of you camera, so if your measurements are in cm `pixels-per-cm`.

So then the size of the thing in the image is:
```
image size * pixels-per-cm
```

# How it works

My code draws a line that would be 10cm long in the image.

* You load up `rangefinder.ino` onto an arduino with an ultrasonic rangefinder wired
  to it then connect the arduino to one of your computers usb ports, this is how
  I get distance values.

* connect a webcam to you computer

* open up `howBig.py` and change the focal length to your cameras focal length.

* stick the arduino and rangefinder to the camera so they both are the same distance
  from the thing you point the camera at.

* run howBig.py with these arguments: 
  ``` bash
  python3 howBig.py <camera number> <serial port of arduino>
  # itll look like:
  python3 howBig.py 2 /dev/ttyACM0
  ```