class gamer:
    def __init__(self, gname,gage,fgame):
        self.name = gname
        self.age=gage
        self.game=fgame
        print(f"Name of the gamer is {self.name}, age is {self.age} and favourite game is {self.game}.")
    def sentence(self):
        return f"I am {self.name} aged {self.age} and I love {self.game} very much!"
print(ryo.sentence())    
ryo = gamer("Ryo", 18, "Pokemon")
            