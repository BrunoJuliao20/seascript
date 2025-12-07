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
# REG_ATK IS THE REGION WHERE THE YOUR ATTACKERS WIDGET APPEAR, SELECT THE WIDGET
# REG_LOW_HP: BE ON LOW HP AND SELECT THE LAST PART OF YOUR HP BAR
# AND TAKE A SCREENSHOT OF A SMALL PIECE OF THE BAR WHEN ITS BLACK
REG_LOW_HP = Region(1635,600,49,23)
REG_CURRENT_HP = Region(1635,597,47,27)
REG_REP_BTN = Region(1363,981,48,51)
REG_REVIVE = Region(751,532,156,139)
REG_RELOG = Region(959,614,188,44)

# IMAGES
IMG_ECRASMITH = "IMG_ECRASMITH.png"
IMG_SAQUESPONTAPES = "IMG_SAQUESPONTAPES.png"
IMG_SMITH = "IMG_SMITH.png"
IMG_CARASMITH = "IMG_CARASMITH.png"
IMG_DEFESA = "IMG_DEFESA.png"
IMG_ENTRAMAPAGRUPO = "IMG_ENTRAGROUPMAP.png"
IMG_CONCLUSAO = "IMG_PARABENS.png"
IMG_CONCLUSAO2 = "IMG_CONCLUSAO2.png"
IMG_LOW_HP = "IMG_LOW_HP.png"
IMG_CREP_BTN = "IMG_CREP_BTN.png"
IMG_REVIVE = "IMG_REVIVE.png"
IMG_DARK = "IMG_DARK.png"
IMG_RR = "IMG_RR1.png"
IMG_RR3 = "IMG_RR3.png"
IMG_AMBIENTE = "IMG_RR2.png"

# SIMILARITY
SIM_IMG_PLAYER = 0.8
SIM_IMG_ECRASMITH = 0.7
SIM_IMG_SAQUESPONTAPES = 0.7
SIM_IMG_SMITH = 0.7
SIM_IMG_CARASMITH = 0.72
SIM_IMG_DEFESA = 0.75
SIM_IMG_RR = 0.9
SIM_IMG_RR3 = 0.9
SIM_IMG_AMBIENTE = 0.9
SIM_IMG_LOW_HP = 0.75
SIM_IMG_CREP_BTN = 0.85
SIM_IMG_REVIVE = 0.8

# GLOBALS
# HOW LONG TO RUN THE BOT
RUNNING_HOURS = 6
BUSY = False
LOW_HP = False


# LOCATIONS TO CLICK ON THE MINIMAP FOR MOVING (TRY TO AVOID ISLAND)
# UNCOMMENT THE configure() FUNCTION ON THE LAST CODE LINE
# COMMENT THE main() FUNCTIONS PLACING A # IN FRONT OF IT
# INSERT THE NUMBER OF THE POSITION IN THE configure(number-of-position-here)
# IT WILL CLICK ON THE DEFIRED POSITION
# FOR YOU TO SELECT THE RELATED SEA REGION

lista_radar = [(1577, 127),(1619, 126),(1575, 168),(1621, 169),(1597, 150)]

def groupmap():
    tempo = 0
    for i in range(3):
        click(Location(1640,185))
        wait(0.5)
        rightClick(Location(580,570))
        wait(31+2*tempo)
        click(Location(1630,150))
        wait(0.5)      
        rightClick(Location(1245,480))
        wait(20+tempo)
        if REG_SEA.exists(Pattern(IMG_CONCLUSAO2).similar(0.7)):
            return
        click(Location(1556,150))
        wait(0.5)
        rightClick(Location(455,500))
        wait(5)
        type("Q")
        if REG_SEA.exists(Pattern(IMG_REVIVE).similar(0.8)):
            click(Location(824,600))
            return
        if REG_SEA.exists(Pattern(IMG_CONCLUSAO).similar(0.7)):
            click(Location(1187,468))
            return
        wait(25)
        type("Q")
        wait(20+tempo)
        if REG_SEA.exists(Pattern(IMG_CONCLUSAO).similar(0.7)):
            click(Location(1187,468))
            return
        tempo = tempo+2
    return

def procura_smith():
    global BUSY
    if BUSY == True:
        wait(2)
        return
    else:
        BUSY = True
        try:
            for i in range(6):
                coordx=lista_radar[i][0]
                coordy=lista_radar[i][1]
                click(Location(coordx,coordy))
                if REG_SEA.exists(Pattern(IMG_SMITH).similar(0.6)):
                    match = REG_SEA.find(Pattern(IMG_SMITH).similar(SIM_IMG_SMITH))
                    type("9")
                    location = match.getTarget()
                    rightClick(Location(location.x, (location.y -20)))
                    type(Key.SPACE)
                    wait(8)
                    for j in range(5):
                        match2 = REG_SEA.find(Pattern(IMG_CARASMITH).similar(SIM_IMG_CARASMITH))
                        location = match2.getTarget()
                        click(Location(location.x-10, (location.y)))
                        wait(3)
                        if REG_SEA.exists(Pattern(IMG_ECRASMITH).similar(0.8)):
                            wait(0.5)
                            click(Location(790,702))
                            wait(1)
                            if REG_SEA.exists(Pattern(IMG_SAQUESPONTAPES).similar(0.9)):
                                match3 = REG_SEA.find(Pattern(IMG_SAQUESPONTAPES).similar(SIM_IMG_SAQUESPONTAPES))
                                location = match3.getTarget()
                                click(location)
                                wait(0.5)
                                click(Location(1030,712))
                                wait(9)
                                while(REG_SEA.exists(Pattern(IMG_ENTRAMAPAGRUPO).similar(0.6))):
                                    wait(1)
                                type("V")    
                                groupmap()
        except:
            BUSY = False
            ARRIVED = True
            return
        BUSY = False
        ARRIVED = True
        procura_smith()


REG_SEA.onAppear(Pattern(IMG_SMITH).similar(SIM_IMG_SMITH), procura_smith)
REG_SEA.observeInBackground(FOREVER)


def check_repair():
    global LOW_HP
    if REG_LOW_HP.exists(Pattern(IMG_LOW_HP).similar(SIM_IMG_LOW_HP)):
        LOW_HP = True


def check_update():
    global BUSY
    BUSY = True
    if REG_SEA.exists(Pattern(IMG_RR).similar(SIM_IMG_RR)) or REG_SEA.exists(Pattern(IMG_AMBIENTE).similar(SIM_IMG_AMBIENTE)) or REG_SEA.exists(Pattern(IMG_RR3).similar(SIM_IMG_RR3)):
        wait(5)
        click(Location(860,630))
        wait(5)
        click(Location(1895,8))
        wait(5)
        click(Location(1478,80))
        #fecha paginas em cima
        wait(3)
        #mexe rato para abrir o sea
        mouseMove(Location(264,34))
        #1hour = 60*60 3600
        wait(600)
        doubleClick(Location(264,34))
        wait(5)
        #clica concordo 1º
        click(Location(1400,920))
        wait(5)
        click(Location(950,450))
        wait(5)
        click(Location(700,480))
        wait(5)
        #clica em type password
        click(Location(960,535))
        wait(0.5)
        type("1")
        wait(0.5)
        type("2")
        wait(0.5)
        type("3")
        wait(0.5)
        type("4")
        wait(0.5)
        click(Location(1040,650))
        wait(5)
        #clica 2º concordo
        click(Location(960,620))
        #ate aqui faz login
        wait(2)
        click(Location(1400,920))
        wait(2)
        #carrega jogar
        click(Location(1090,175))
        wait(15)
        if REG_SEA.exists(Pattern(IMG_RR3).similar(SIM_IMG_RR3)):
            check_update()
        click(Location(1275,740))
        wait(1)
    BUSY = False


def repair():
    global BUSY
    global LOW_HP
    if BUSY == True:
        return
    else:
        BUSY = True
        current_hp_image = Screen(0).capture(REG_CURRENT_HP)
        type("Q")
        wait(2)
        if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
            BUSY = False
            LOW_HP = False
            return
        if REG_CURRENT_HP.exists(Pattern(current_hp_image).similar(0.85)):
            type("Q")
            wait(1)
        REG_REP_BTN.waitVanish(Pattern(IMG_CREP_BTN).similar(SIM_IMG_CREP_BTN), 50)
        BUSY = False
        LOW_HP = False


def check_revive():
    global BUSY
    global LOW_HP
    if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
        BUSY = True
        revived = False
        while revived == False:
            wait(0.5)
            click(REG_REVIVE.getCenter())
            type("Q")
            if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
                pass
            else:
                revived = True
        BUSY = False
        LOW_HP = True
        mouseMove(REG_SEA.getCenter())

def main():
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=10)
    check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=36)
    while finished == False:
        if datetime.datetime.now() > check_revive_timeout:
            check_revive()
            check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
        if datetime.datetime.now() > check_update_timeout:
            check_update()
            check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=600)
        procura_smith()
        check_repair()
        if LOW_HP == True:
            repair()
        if datetime.datetime.now() > finish_at:
            finished = True
    REG_SEA.stopObserver()
    run("cmd /C shutdown /s")

#configure(5)
main()