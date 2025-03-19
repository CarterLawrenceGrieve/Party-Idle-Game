import Party
#Not implemented until I can get a CMD working, but here are ideas

#Spawn rate and despawn rate can be fucked with
def SpawnRateUp(myParty):
    myParty.set_SpawnTime((myParty.get_SpawnTime())/1.5);

def SpawnRateDown(myParty):
    myParty.set_SpawnTime((myParty.get_SpawnTime())*1.5);

def DeSpawnRateDown(myParty):
    myParty.set_DeSpawnTime((myParty.getDeSpawnTime())*1.5);

def DeSpawnRateUp(myParty):
    myParty.set_DeSpawnTime((myParty.getDeSpawnTime())/1.5);

#Why did I code these as seperate functions?  Tank 1 type's population and points for a big ol' type point boost
def HentaiWatchalong(myParty):
    myParty.set_WeebPts(myParty.get_WeebPts()+1000);
    myParty.set_PrepPop(0);
    myParty.set_PrepPts(0);

def McrKaroke(myParty):
    myParty.set_GothPts(myParty.get_GothPts()+1000);
    myParty.set_WeebPop(0);
    myParty.set_WeebPts(0);

def PoloShirtFashionShow(myParty):
    myParty.set_PrepPts(myParty.get_PrepPts()+1000);
    myParty.set_GothPop(0);
    myParty.set_GothPts(0);

#Increase chances of spawning and decrease chances of despawning a certain type
def SpawnModUp(myParty,type):
    match type:
        case 'Goth':
            myParty.set_GothMod(myParty.get_GothMod()+.5);
        case 'Prep':
            myParty.set_PrepMod(myParty.get_PrepMod()+.5);
        case 'Weeb':
            myParty.set_WeebMod(myParty.get_WeebMod()+.5);

#For use in Party because I need this for some stupid reason
def MakeZeroIfNeg(num):
    if num<0:
        return 0;
    else:
        return num;