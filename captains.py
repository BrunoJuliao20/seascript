#NPC
import random
import datetime
Settings.MoveMouseDelay = 0.25
Settings.ObserveScanRate = 1
REG_SEA = Region(501,329,293,440)

# IMAGES
IMG_STOP = Pattern("IMG_CAPTAIN.png").similar(0.60)
IMG_STOPBLUE = "IMG_STOPBLUE.png"

# SIMILARITY
SIM_IMG_STOP = 0.8
SIM_IMG_STOPBLUE = 0.8
# HOW LONG TO RUN THE BOT
RUNNING_HOURS = 2
BUSY = False
ARRIVED = False


def autoclicker():
    global BUSY
    global ARRIVED
    while 1:
        click(Location(1200, 725))
        wait(0.5)


def craftar():
    global BUSY
    global ARRIVED
    while 1:
        click(Location(700, 725))
        click(Location(1200, 700))
        click(Location(950, 750))
        wait(0.5)
        click(Location(700, 675))
        click(Location(1200, 700))
        click(Location(950, 750))
        wait(0.2)
        click(Location(700, 750))
        click(Location(1200, 700))
        click(Location(950, 750))
        wait(0.2)
        click(Location(700, 750))
        click(Location(1200, 700))
        click(Location(950, 750))
        wait(0.2)
        click(Location(700, 750))
        click(Location(1200, 700))
        click(Location(950, 750))
        if REG_SEA.exists(Pattern(IMG_STOPBLUE).similar(SIM_IMG_STOPBLUE)):
            print("Azul")
            exit(0)
        else:
            craftar()


def amuleto():
    global BUSY
    global ARRIVED
    while(1):
        type("4")
        wait(1)
        type("6")
        wait(50)
      

def main():
    global NPC_WAIT
    global ARRIVED
    
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    autoclicker()
    #craftar()
    #amuleto()
    if datetime.datetime.now() > finish_at:
        finished = True
        REG_SEA.stopObserver()
        run("cmd /C shutdown /s")

#configure(5)
main()