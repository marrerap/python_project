class Start:
    def __init__(self, start):
       self.start = start
       


    def start(self):
        if self.start == "n" or self.start  == "N":
            return (f"Welp, if you never try, you never fail right?")
        elif self.start == "y" or self.start == "Y":
            return intro()
