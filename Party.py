import random as rand
from Purchases import MakeZeroIfNeg
# Money functions are down past endless getters and setters
class Party:
    def __init__(self, GothPts=0, PrepPts=0, WeebPts=0,SpawnTime=3,GothPop=0,PrepPop=0,WeebPop=0,TotPop=0,DeSpawnTime=8,GothMod=1,PrepMod=1,WeebMod=1,Bucks=20):
        self.GothPts=GothPts;
        self.PrepPts=PrepPts;
        self.WeebPts=WeebPts;
        self.SpawnTime=SpawnTime;
        self.GothPop=GothPop;
        self.PrepPop=PrepPop;
        self.WeebPop=WeebPop;
        self.TotPop=TotPop;
        self.DeSpawnTime=DeSpawnTime;
        self.GothMod=GothMod;
        self.PrepMod=PrepMod;
        self.WeebMod=WeebMod;
        self.Bucks=Bucks;

    def get_Bucks(self):
        return self.Bucks

    def set_Bucks(self, value):
        self.Bucks = value

    def get_GothMod(self):
        return self.GothMod

    def set_GothMod(self, value):
        self.GothMod = value

    def get_PrepMod(self):
        return self.PrepMod

    def set_PrepMod(self, value):
        self.PrepMod = value

    def get_WeebMod(self):
        return self.WeebMod

    def set_WeebMod(self, value):
        self.WeebMod = value

    def get_GothPts(self):
        return self.GothPts

    def set_GothPts(self, value):
        self.GothPts = value

    def get_PrepPts(self):
        return self.PrepPts

    def set_PrepPts(self, value):
        self.PrepPts = value

    def get_WeebPts(self):
        return self.WeebPts

    def set_WeebPts(self, value):
        self.WeebPts = value

    def get_SpawnTime(self):
        return self.SpawnTime

    def set_SpawnTime(self, value):
        self.SpawnTime = value

    def get_GothPop(self):
        return self.GothPop

    def set_GothPop(self, value):
        self.GothPop = value

    def get_PrepPop(self):
        return self.PrepPop

    def set_PrepPop(self, value):
        self.PrepPop = value

    def get_WeebPop(self):
        return self.WeebPop

    def set_WeebPop(self, value):
        self.WeebPop = value

    def get_TotPop(self):
        return self.TotPop

    def set_TotPop(self, value):
        self.TotPop = value

    def get_DeSpawnTime(self):
        return self.DeSpawnTime

    def set_DeSpawnTime(self, value):
        self.DeSpawnTime = value
    
#Select functions that are biased based on points and modifier - determine spawn and despawn types.  Should implement an enum for guest types, but didn't.

    def SelectPos(self):
        seq="Goth","Prep","Weeb";
        x=rand.choices(seq,weights=[1+(self.GothPts/10)*self.GothMod,1+(self.PrepPts/10)*self.PrepMod,1+(self.WeebPts/10)*self.WeebMod]);
        return x;
#I cannot believe I needed a helper function to solve this problem - func in purchases for now.  Python said no to making it here.
    def SelectNeg(self):
        seq="Goth","Prep","Weeb";
        x=rand.choices(seq,weights=[MakeZeroIfNeg(100-(self.GothPts/10)) ,MakeZeroIfNeg(100-(self.PrepPts/10)),MakeZeroIfNeg(100-(self.WeebPts/10))]);
        return x;
    
    def __str__(self):
        return f"Total Population: {self.TotPop}\nGoth, Prep and Weeb Populations: {self.GothPop}, {self.PrepPop}, {self.WeebPop}\nGoth, Prep, and Weeb Points: {self.GothPts}, {self.PrepPts}, {self.WeebPts}\nYou got {self.Bucks:.2f} bucks, bitch";

#Spawning and Despawning - Spawning gives points (increasing by type population) and despawning gives money (increasing on party's type points)

    def Add(self,Added):
        self.TotPop+=1;
        match Added:
            case ["Goth"]:
                self.GothPop+=1;
                self.GothPts+=self.GothPop;
            case ["Prep"]:
                self.PrepPop+=1;
                self.PrepPts+=self.PrepPop;
            case ["Weeb"]:
                self.WeebPop+=1;
                self.WeebPts+=self.WeebPop;
        return None;
                
    def Ditch(self, Ditched):
        match Ditched:
            case ["Goth"]:
                if self.GothPts<rand.randint(0,self.TotPop) and self.GothPop>0:
                    self.GothPop-=1;
                    self.TotPop-=1;
                    self.Bucks+=(1+((self.GothPts)/10));
            case ["Prep"]:
                if self.PrepPts<rand.randint(0,self.TotPop) and self.PrepPop>0:
                    self.PrepPop-=1;
                    self.TotPop-=1;
                    self.Bucks+=(1+((self.PrepPts)/10));
            case ["Weeb"]:
                if self.WeebPts<rand.randint(0,self.TotPop) and self.WeebPop>0:
                    self.WeebPop-=1;
                    self.TotPop-=1;
                    self.Bucks+=(1+((self.WeebPts)/10));
        return None;