# Demo of MultiLevel Inheritance
class GFather:
    no_of_game = 3
class Father(GFather):
    # no_of_game = 4
    dance = 1
    def isDance(self):
        return f"Yes father can dance {self.dance}"
    def isNoofGame(self):
        return f"Father can dance {self.no_of_game}"
class Son(Father):
    # no_of_game = 5
    dance = 2
    # def isDance(self):
    # return f"Grand son dance {self.dance}"
    def isNoofGame(self):
        return f"Grand son dance {self.no_of_game}"
gf=GFather()
f=Father()
s=Son()
print(s.no_of_game)
print(s.isDance())