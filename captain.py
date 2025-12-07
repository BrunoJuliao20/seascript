#NPC
import random
import datetime
Settings.MoveMouseDelay = 0.3
# KEEP OBSERVE SCAN RATE IN 1 TO USE LESS CPU
# INCREASE IF YOU WANT
Settings.ObserveScanRate = 1

# CONFIGURATION
# REGIONS
# REG_SEA KEEP IT IN 800X600 FOR LESS CPU USAGE
REG_SEA = Region(452,165,1015,756)
REG_CAPTAIN = Region(1135,351,246,181)

REG_RELOG = Region(959,614,188,44)

IMG_VIRGO = "IMG_VIRGO.png"
IMG_SAGI = "IMG_SAGI.png"
IMG_CANCER = "IMG_CANCER.png"
IMG_VIRGOMAP = "IMG_VIRGOMAP.png"
IMG_CARTOGRAFO = "IMG_CARTOGRAFO.png"
IMG_VIRGOFLYN = "IMG_VIRGOFLYN.png"
IMG_VIRGOARTEMIS = "IMG_VIRGOARTEMIS.png"
IMG_ENTRAR = Pattern("IMG_ENTRAR.png").similar(0.90)
IMG_RELOG = "IMG_RELOG.png"
IMG_AVANCAR = "IMG_AVANCAR.png"

# SIMILARITY
SIM_IMG_VIRGO = 0.8
SIM_IMG_SAGI = 0.8
SIM_IMG_CANCER = 0.8
SIM_IMG_VIRGOMAP = 0.8
SIM_IMG_VIRGOFLYN = 0.7
SIM_IMG_VIRGOARTEMIS = 0.7
SIM_IMG_CARTOGRAFO = 0.8
SIM_IMG_ENTRAR = 0.95
SIM_IMG_AVANCAR = 0.9
SIM_IMG_RELOG = 0.8

# GLOBALS
########### HOW LONG TO RUN THE BOT ##############
RUNNING_HOURS = 2
BUSY = False
CAPTAIN = False


def speedup(x):
    if x == 1:
        for i in range(2):
            click(Location(1055, 475))
            wait(0.5)
            mouseMove(Location(995, 505))
            doubleClick(Location(995, 505))
            wait(0.5)
            click(Location(955, 710))
        click(Location(1372, 309))
        captain_sagi()
    if x == 2:
         for i in range(2):
            click(Location(1055, 640))
            wait(0.5)
            mouseMove(Location(995, 505))
            doubleClick(Location(995, 505))
            wait(0.5)
            click(Location(955, 710))
         click(Location(1372, 309))
         captain_cancer()
    if x == 3:
        for i in range(2):
            mouseMove(Location(1055, 740))
            Mouse.wheel(WHEEL_DOWN,2)
            click(Location(1055, 740))
            wait(0.5)
            mouseMove(Location(995, 505))
            doubleClick(Location(995, 505))
            wait(0.5)
            click(Location(955, 710))
    wait(0.5)
    click(Location(1372, 309))
    type("3")
    return

def captain_virgonormal():
    global BUSY
    BUSY = True
    try:
        type("5")
        click(Location(1107, 35))
        wait(0.5)
        click(Location(1107, 91))
        wait(0.5)
        click(Location(960, 475))
        if REG_SEA.exists(Pattern(IMG_AVANCAR).similar(SIM_IMG_AVANCAR)):
            speedup(1)
            BUSY = False 
            return
        wait(0.5)
        click(Location(960, 475))
        #ate aqui clica no atribuir mapa
        click(Location(596, 380))
        mouseMove(Location(675, 450))
        #comentar a linha de baixo se o mapa virgo for dos primeiros
        Mouse.wheel(WHEEL_DOWN, 5)
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_VIRGO).similar(SIM_IMG_VIRGO)):
                match = REG_SEA.find(Pattern(IMG_VIRGO).similar(SIM_IMG_VIRGO).targetOffset(50, -20))
                location = match.getTarget()
                #clica no sagitario
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 4)
                for i in range(16):
                    if REG_CAPTAIN.exists(Pattern(IMG_VIRGOMAP).similar(SIM_IMG_VIRGOMAP)):
                        match = REG_CAPTAIN.find(Pattern(IMG_VIRGOMAP).similar(SIM_IMG_VIRGOMAP).targetOffset(-100, 0))
                        location = match.getTarget()
                        click(Location(location))
                        wait(0.5)
                        if REG_SEA.exists(Pattern(IMG_ENTRAR).similar(SIM_IMG_ENTRAR)):
                            click(Location(955,750))
                            speedup(1)
                            BUSY = False
                            return
                        else:
                            Mouse.wheel(WHEEL_DOWN, 2)
                    else:
                        Mouse.wheel(WHEEL_DOWN, 2)
                break
            else:
                Mouse.wheel(WHEEL_DOWN, 4)
        click(Location(1340, 340))
        click(Location(1372, 309))
    except:
        BUSY = False
        return
    BUSY = False

    
def captain_virgo():
    global BUSY
    global CAPTAIN
    BUSY = True
    try:
        click(Location(1107, 35))
        wait(0.5)
        click(Location(1107, 91))
        wait(0.5)
        click(Location(960, 475))
        if REG_SEA.exists(Pattern(IMG_AVANCAR).similar(SIM_IMG_AVANCAR)):
            speedup(1)
            BUSY = False 
            return
        click(Location(960, 475))
        #ate aqui clica no atribuir mapa
        click(Location(596, 380))
        mouseMove(Location(675, 450))
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_VIRGO).similar(SIM_IMG_VIRGO)):
                match = REG_SEA.find(Pattern(IMG_VIRGO).similar(SIM_IMG_VIRGO).targetOffset(50, -20))
                location = match.getTarget()
                #click no mapa virgo á esquerda
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 6)
                if CAPTAIN == False:
                    #capitaoflyn
                    for i in range(6):
                        #vai fazer com o flyn
                        if REG_SEA.exists(Pattern(IMG_VIRGOFLYN).similar(SIM_IMG_VIRGOFLYN)):
                            match = REG_SEA.find(Pattern(IMG_VIRGOFLYN).similar(SIM_IMG_VIRGOFLYN).targetOffset(30, -20))
                            location = match.getTarget()
                            click(Location(location))
                            wait(0.5)
                            click(Location(955,750))
                            BUSY = False
                            speedup(1)
                            CAPTAIN = True
                            return
                        else:
                            Mouse.wheel(WHEEL_DOWN, 4)
                else:
                    #capitaoartemis
                    for i in range(6):
                        if REG_SEA.exists(Pattern(IMG_VIRGOARTEMIS).similar(SIM_IMG_VIRGOARTEMIS)):
                            match1 = REG_SEA.find(Pattern(IMG_VIRGOARTEMIS).similar(SIM_IMG_VIRGOARTEMIS).targetOffset(40, -30))
                            location1 = match1.getTarget()
                            click(Location(location1))
                            wait(0.5)
                            click(Location(955,750))
                            BUSY = False
                            speedup(1)
                            CAPTAIN = False
                            return
                        else:
                            Mouse.wheel(WHEEL_DOWN, 4)
            else:
                Mouse.wheel(WHEEL_DOWN, 4)
        click(Location(1340, 340))
        click(Location(1372, 309))
    except:
        BUSY = False
        return
    BUSY = False


def captain_sagi():
    global BUSY
    BUSY = True
    try:
        click(Location(1107, 35))
        wait(0.5)
        click(Location(1107, 91))
        wait(0.5)
        click(Location(955, 640))
        if REG_SEA.exists(Pattern(IMG_AVANCAR).similar(SIM_IMG_AVANCAR)):
            speedup(2)
            BUSY = False 
            return
        wait(0.5)
        click(Location(955, 640))
        #ate aqui clica no atribuir mapa
        click(Location(596, 380))
        mouseMove(Location(675, 450))
        Mouse.wheel(WHEEL_DOWN, 3)
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_SAGI).similar(SIM_IMG_SAGI)):
                match = REG_SEA.find(Pattern(IMG_SAGI).similar(SIM_IMG_SAGI).targetOffset(50, -20))
                location = match.getTarget()
                #clica no sagitario
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 8)
                for i in range(15):
                    if REG_CAPTAIN.exists(Pattern(IMG_CARTOGRAFO).similar(SIM_IMG_CARTOGRAFO)):
                        match = REG_CAPTAIN.find(Pattern(IMG_CARTOGRAFO).similar(SIM_IMG_CARTOGRAFO).targetOffset(-100, 0))
                        location = match.getTarget()
                        click(Location(location))
                        if REG_SEA.exists(Pattern(IMG_ENTRAR).similar(SIM_IMG_ENTRAR)):
                            wait(0.5)
                            click(Location(955,750))
                            wait(0.5)
                            speedup(2)
                            BUSY = False
                            return
                        else:
                            Mouse.wheel(WHEEL_DOWN, 2)
                    else:
                        Mouse.wheel(WHEEL_DOWN, 2)
                break
            else:
                Mouse.wheel(WHEEL_DOWN, 4)
        click(Location(1340, 340))
        click(Location(1372, 309))
    except:
        BUSY = False
        return
    BUSY = False


def captain_cancer():
    global BUSY
    BUSY = True
    try:
        click(Location(1107, 35))
        wait(0.5)
        click(Location(1107, 91))
        wait(0.5)
        mouseMove(Location(955, 740))
        Mouse.wheel(WHEEL_DOWN,2)
        click(Location(955, 740))
        if REG_SEA.exists(Pattern(IMG_AVANCAR).similar(SIM_IMG_AVANCAR)):
            speedup(3)
            BUSY = False 
            return
        click(Location(955, 740))
        #ate aqui clica no atribuir mapa
        click(Location(596, 380))
        mouseMove(Location(675, 450))
        Mouse.wheel(WHEEL_DOWN, 8)
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_CANCER).similar(SIM_IMG_CANCER)):
                match = REG_SEA.find(Pattern(IMG_CANCER).similar(SIM_IMG_CANCER).targetOffset(50, -20))
                location = match.getTarget()
                #clica no cancer
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 13)
                for i in range(15):
                    if REG_CAPTAIN.exists(Pattern(IMG_CARTOGRAFO).similar(SIM_IMG_CARTOGRAFO)):
                        match = REG_CAPTAIN.find(Pattern(IMG_CARTOGRAFO).similar(SIM_IMG_CARTOGRAFO).targetOffset(-100, 0))
                        location = match.getTarget()
                        click(Location(location))
                        wait(0.5)
                        if REG_SEA.exists(Pattern(IMG_ENTRAR).similar(SIM_IMG_ENTRAR)):
                            click(Location(955,750))
                            speedup(3)
                            BUSY = False
                            return
                        else:
                            Mouse.wheel(WHEEL_DOWN, 2)
                    else:
                        Mouse.wheel(WHEEL_DOWN, 2)
                break
            else:
                Mouse.wheel(WHEEL_DOWN, 4)
        click(Location(1340, 340))
        click(Location(1372, 309))
    except:
        BUSY = False
        return
    BUSY = False

REG_SEA.observeInBackground(FOREVER)
REG_CAPTAIN.observeInBackground(FOREVER)


def check_relog():
    global BUSY
    if REG_RELOG.exists(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG)):
        BUSY = True
        relogged = False
        while relogged == False:
            wait(0.5)
            try:
                REG_RELOG.click(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG))
            except:
                pass
            wait(10)
            if REG_RELOG.exists(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG)):
                pass
            else:
                relogged = True
        BUSY = False
        mouseMove(REG_SEA.getCenter())     


def main():
    global ARRIVED
    global CAPTAIN
    global BUSY
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    check_relog_timeout = datetime.datetime.now() + datetime.timedelta(seconds=60)
    #check_teleport_timeout = datetime.datetime.now() + datetime.timedelta(seconds=60)
    check_captainvirgo_timeout = datetime.datetime.now() + datetime.timedelta(seconds=3)
    check_captainsagi_timeout = datetime.datetime.now() + datetime.timedelta(seconds=2222222223)
    check_captaincancer_timeout = datetime.datetime.now() + datetime.timedelta(seconds=2333333)
    while finished == False:
        if datetime.datetime.now() > check_relog_timeout:
            check_relog()
            check_relog_timeout = datetime.datetime.now() + datetime.timedelta(seconds=30)
        if datetime.datetime.now() > check_captainvirgo_timeout:
            captain_virgonormal()
            check_captainvirgo_timeout = datetime.datetime.now() + datetime.timedelta(seconds=80)
        if datetime.datetime.now() > check_captainsagi_timeout:
            captain_sagi()
            check_captainsagi_timeout = datetime.datetime.now() + datetime.timedelta(seconds=225)
        if datetime.datetime.now() > check_captaincancer_timeout:
            captain_cancer()
            check_captaincancer_timeout = datetime.datetime.now() + datetime.timedelta(seconds=100)
        if datetime.datetime.now() > finish_at:
            finished = True
    REG_SEA.stopObserver()
    run("cmd /C shutdown /s")

#configure(5)
main()