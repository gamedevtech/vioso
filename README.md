# vioso

The idea behind vioso is to turn your make your vim sessions (and in the future, coding session) musical.  I was inspired by touchpianist.com as seen on reddit.  Imagine it like a generic, high-level guitar hero for programming.  In theory, I suppose that you could use this tool to improve your flow... though I don't know how my brain will respond to pauses in the song



This is just a prototype to see how it feels to "make music" while I code.


## current implementation

The current implementation uses selenium to open up touchpianist.com and reads continuously from a file called provided as argument to vioso.py  Future implementation will use habit vim to continuously update the logfile.

## dependencies
    
* selenium
    
    pip install selenium

