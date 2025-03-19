from Party import Party
import time
import multiprocessing
from multiprocessing.managers import BaseManager
import Purchases
import sys

#Summary: spawning increments type populations and total populations, plus increases type points by the type population.  
#Despawning deincrements type pop and total pop but increments money proportional to type points.
#Type chosen for each is random, but influenced by type points and type modifier
#Purchases will cost some combination of bucks and type points
#TO-DO: taking input and actual gameplay.  Maybe implement an ENUM type or a "person" class for more sophisticated behavior

def Spawn(myParty):
    while True:
        myParty.Add(myParty.SelectPos());
        time.sleep(myParty.get_SpawnTime());

def Despawn(myParty):
    while True:
        myParty.Ditch(myParty.SelectNeg());
        time.sleep(myParty.get_DeSpawnTime());

# Stats to output every .5 seconds.  Yes, there is a more elegant way to do this than moving the cursor back to start again and again.  No, I have not found one.
def Display(myParty):
    print("\n\n\n");
    while True:
        sys.stdout.write(u"\u001b[1000D"+u"\u001b[3A" + f"Total Population: {myParty.get_TotPop()}\nGoth, Prep and Weeb Populations: {myParty.get_GothPop()}, {myParty.get_PrepPop()}, {myParty.get_WeebPop()}\nGoth, Prep, and Weeb Points: {myParty.get_GothPts()}, {myParty.get_PrepPts()}, {myParty.get_WeebPts()}\nYou got {myParty.get_Bucks():.2f} bucks, bitch");
        sys.stdout.flush();
        time.sleep(.5);

#Unused as of yet - could not get both refreshing display AND user input working
def Input(myParty):
    Flag=True;
    while Flag:
        try:
            char=input("Q to quit, S to store");
            if char=="Q" or "q":
                sys.exit(); #Shut off program
            elif char=="S" or "s":
                #Go to store
                print("Wow this print statement could be a store if I made one")
            else:
                print("The fuck you say to me");
        except:
            Display(myParty);

#Multiprocessing was unlikely to be the move here - gonna try multithreading instead and see if that makes implementation of CMD via "Display" function easier

if __name__=='__main__':
    BaseManager.register('Party', Party);
    manager=BaseManager();
    manager.start();
    theirParty=Party();
    inst=manager.Party();

    Spawning=multiprocessing.Process(target=Spawn,args=[inst]);
    Despawning=multiprocessing.Process(target=Despawn,args=[inst]);
    Displaying=multiprocessing.Process(target=Display,args=[inst]);


    Spawning.start();
    Despawning.start();
    Displaying.start();


    Spawning.join();
    Despawning.join();
    Displaying.join();
    
#Trying and failing to make input happen
'''while True:
        char=input("Q to quit, D for Display");
        if char=="Q" or "q":
            sys.exit();
        if char=='D' or 'd':
            Display.join();
            char=input("Q to quit");
            if char=='q' or "Q":
                Display.Terminate();'''