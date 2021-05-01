A small animation i made with my girlfrierd after having watched the last episode of The Mandalorian.
Masks made in illustrator, animation made in python3.



if you want to run or reuse some parts of the code: 
- first of all, u need these three useful dudes

$ pip3 install pygame
$ pip3 install opencv-python
$ pip3 install moviepy

- once u got these three requirements
--first launch this (you need pygame for this)

$ python3 animate.py
 
   this will create a frame sequence in "snaps" directory
   the hard job is pretty much done entirely here:
   -blit
   -alphas
   -transitions
   each image can be converted in a pygame sprite, so we also can use 
   pygame as a very rude real time animation driver

   please note that we can choose to obtain an effect by playin on three different levels
   1: real time effects: effect must be pretty light, in order to be processed in 
      your frame rate window
   2: post production: since the output is a list of frames, you can always process the images 
      one by one in a second time
   3: you can also run the pygame movie in simulated (or even distorted) time. just change the clock value
      assigment to a fictious clock     

--then launch this (you need opencv and moviepy for this)

$ python3 generate.py

  this is merely a snaps2video subroutine. we generate a mute movie with opencv
  (maybe vwe can cut out opencv from this pipe, once and if i get better with moviepy)
  then we join a soundtrack with moviepy

may the force be with you

  

