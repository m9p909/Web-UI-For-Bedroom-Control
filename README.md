# Web-UI-For-Bedroom-Control
This app will eventually be the main user interface for my raspberry pi bedroom control and monitoring system. 

### Features(some of these may not be added for SEG2105, or just not added altogether):
- modify RoomMate notification system (Add remove or rearrange members)
- get temperature of bedroom (arduino temp sensor)
- Humidity of bedroom
- Is computer on?
- Is computer booted to windows or linux? (useful to know if I can use Teamviewer to access my computer)
- button that has the rasp pi play a motivational quote
- is anyone in the bedroom (arduino ultrasonic sensor tests the height of everyone that walks in)
- am I in my bedroom (I am unusually tall, if someone around my height walks in becomes true) (state machine?)
- play spotify on rasp pi
- Fan on or off switch
- Light switch
- jazz button, dims the lights and plays jazz (Chill button)
- party button, makes rainbow lights and plays electro music
- maybe other mood buttons, sad, angry, happy etc. 
- somehow integrating https://mycroft.ai/, this one is a little iffy
- light content in room(photoresistor, or something else depending on whats available)
- test if door is open
- panic button, available in the menu that does the same thing as the chill button

### UI Requirements v1
- front page lists the temperature, humidity, light content, is door open
- Need to be able to set whether I'm in the room since errors will be common unless a better testing method is determined
- motivational quote button should also display a quote in case I'm not in my room
- is computer on indicator
- windows or linux indicator
- fan on or off switch
- page with mood buttons
- Light switch
- Simulation for all these elements, maybe prints to web console

list of tabs:
- Main(displays temp, humidity, light content, is my room empty, is door open) 
- mood page (list of moods and buttons that change the mood), 
- settings(shows if I'm in the room, reset button, disable/enable tracking(for privacy), set myself to in or out of the room)
- Computer info (shows info about my desktop)
- Control Panel (lights on/off, fan on/off, computer on/off)
- Motivational quote page


