def setup():
    global terminal
    size(800,1000)
    terminal = Terminal("Welcome.\n", width, height)

def draw():
    # Waiting for user input
    if terminal.doingInput:
        return
    
def keyPressed():
    global terminal
    if key == ENTER:
        terminal.submit()
    elif key == BACKSPACE:
        terminal.backspace()
    elif type(key) == str:
        terminal.addChar(key)
            
    

class Terminal:
    
    def __init__(self, initText, w, h):
        self.lines = [initText]
        self.width = w
        self.height = h
        self.doingInput = False
        self.timer = 0
        
    # just like regular print
    def print(self, string):
        # Add input string as the last line of initText

    # Types a character on the current line
    def addChar(self, char):
        # Add a character to the last line.
        
    def backspace(self):
        # Get rid of last character in the last line
        
    def draw(self):
        self.timer += 1

        # The caret thing you see all the time lol
        if (self.timer % 60 < 30):
            displayText = self.lines[-1] + chr(-1)
        else:
            displayText = self.lines[-1]
            
        text(displayText,10,10,w,h)
        
    def submit(self):
        answer = function        
        print(answer)
