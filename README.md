# Web-UI-For-Bedroom-Control
This app will eventually be the main user interface for my raspberry pi bedroom control and monitoring system. 

### Features(some of these may not be added for SEG2105, or just not added altogether):
- modify RoomMate notification system (Add remove or rearrange members)
- get temperature of bedroom (arduino temp sensor)
- Humidity of bedroom
- Is computer on?
- Is computer booted to windows or linux? (useful to know if I can use Teamviewer to access my computer)
- button that has the rasp pi play a motivational quote
- history of people that walked in or out the door and their height (arduino ultrasonic sensor tests the height of everyone that walks in)
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
- settings(door history such as people that walked in or out the door, reset button, disable/enable tracking(for privacy), )
- Computer info (shows info about my desktop)
- Control Panel (lights on/off, fan on/off, computer on/off)
- Motivational quote page


