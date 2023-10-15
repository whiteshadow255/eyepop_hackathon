# eyepop_hackathon
ChinCheck - Screen worker posture tracker

Video explanation: https://youtu.be/HzE3Nir0s9g

Code working: https://youtu.be/rQtC0SwlH-c


Raison dêtre:

People who work on screens a lot often suffer from bad posture. 

For this dev, that mostly means my chin advances forward way far, and puts a ton of strain on my neck and back muscles. 
This leads to a ton of pain which can really ruin my day. 

Using the Eyepop.ai API during their 24hr hackathon on 10-14-23, I created a simple program which uses Eyepop's ability to identify eye coordinates. 

The program starts by asking the user to set a good posture by pulling their chin back towards their neck, then setting a bad posture by pushing their chin forward. 

Then, every 10s it takes an image and compares the eye distance. If the head is advanced 75% or more of the range between the good and bad postures, it plays an audio file notifying the user that their chin is too far forward. 

Limitations:

If there's other people in the frame or an excessively busy background it probably won't work in the current implementation. 

if you change position of the laptop or majorly change your own position, you should restart the code.

This was built with a macbook using the internal camera. No idea how it will work with other rigs
