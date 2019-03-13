# OpenCV-Projects
*1.Changing the resolution-<br/>
Use res-change.py to change the resolution of the webcam.<br/>
Available resolutions  are 480p,720p and 1080p.<br/>
There is also an option to change to desired resolution despendingon the capabitlities of the hardware.


*2.Seamless Cloning-<br/>
Use seamlessClone.py to clone two images seamlessly.<br/>
For demo purposes, code uses images of airplane and sky to clone.


*3.ALpha Blending-<br/>
Use alphaBlend.py to blend foreground and background images using alpha as mask.<br/>
For demo purposes, code uses foreGroundAsset.png and backGround.jpg as foreground and background images.<br/>
Note- Make sure the image has 4 channels(R,G,B,A).

*4.Getting AlphaMask-<br/>
Use GetAlpha.py to get alpha channel for your image.<br/>
Note- The code uses PIL library.

*5.Grabcut-<br/>
Use GrabCut.py to grab only the foreground part of the image.

*6.Object Size Finder-<br/>
Use object_size.py to find the size of any object simlar to the reference object.<br/>
Note- Please give the size of reference object in inches. Also,make sure both the reference object and target object are in the same image. For Demo puproses, 1.jpg can be used.

*7.Distance To Camera-<br/>
Use distance_to_camera.py to determine the distance from a known object in an image to our camera.<br/>
Note - Prior to using the application, the marker's width and the distance to the camera should be known. The code was tested for 2ft.jpg as the marker image.

*8.Eye Detector-<br/>
Use eye_detector.py to detect location of the human eye in an image.<br/>
The loacton of the eye is represented as a rectangle.

*9.Record From Webcam-<br/>
Use record-video.py to record a video in your desired format and resolution.<br/>
Currently, supported versions are .avi and.mp4.
