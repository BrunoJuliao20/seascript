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
REG_SEA = Region(448,156,1025,769)

# REG_ATK IS THE REGION WHERE THE YOUR ATTACKERS WIDGET APPEAR, SELECT THE WIDGET
REG_ATK =  Region(55,142,203,48)
# REG_LOW_HP: BE ON LOW HP AND SELECT THE LAST PART OF YOUR HP BAR
# AND TAKE A SCREENSHOT OF A SMALL PIECE OF THE BAR WHEN ITS BLACK
REG_LOW_HP = Region(1630,439,49,27)
REG_CURRENT_HP = Region(1635,441,43,24)
REG_REP_BTN = Region(1482,871,47,48)
REG_REVIVE = Region(926,518,241,207)
REG_RELOG = Region(959,614,188,44)

# IMAGES
IMG_PLAYER = "IMG_VELA.png"
IMG_NPC1 = "MAPA_BOLA.png"
IMG_NPC2 = "MAPA_CORACAO.png"
IMG_NPC3 = "MAPA_AVARENTO.png"
IMG_NPC4 = "MAPA_CAVALHEIRO.png"
IMG_NPC5 = "MAPA_FANTASMA.png"
IMG_NPC6 = "NPC_OSSO.png"
IMG_PORTALAZUL = "MAPA_ENTRAZUL.png"
IMG_PORTAL = "MAPA_PORTAL.png"
IMG_REVIVE = "IMG_50REPAIR.png"
IMG_DARK = "IMG_DARK.png"
IMG_RADAR = "IMG_RADAR.png"
IMG_RR = "IMG_RR1.png"
IMG_RR3 = "IMG_RR3.png"
IMG_AMBIENTE = "IMG_RR2.png"

# SIMILARITY
SIM_IMG_NPC1 = 0.7
SIM_IMG_NPC2 = 0.7
SIM_IMG_NPC3 = 0.7
SIM_IMG_NPC4 = 0.6
SIM_IMG_NPC5 = 0.6
SIM_IMG_NPC6 = 0.7
SIM_IMG_PORTAL = 0.65
SIM_IMG_PORTALAZUL = 0.6
SIM_IMG_ATK = 0.6
SIM_IMG_RADAR = 0.85
SIM_IMG_CREP_BTN = 0.85
SIM_IMG_REVIVE = 0.6
SIM_IMG_RELOG = 0.8
SIM_IMG_RR = 0.8
SIM_IMG_RR3 = 0.8
SIM_IMG_AMBIENTE = 0.8

# GLOBALS
########### HOW LONG TO RUN THE BOT ##############
RUNNING_HOURS = 4
BUSY = False
LOW_HP = False
LAST_MOVE = None
LAST_POS = None
CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=10)


def entra_mapa():
    for i in range(500):
        click(Location(1100,524))
        wait(2)
    click(Location(1565,182))
    wait(1)
    rightClick(Location(1000,474))
    wait(1)
    type(Key.SPACE)
    wait(14)
    click(Location(959,472))
    wait(1)
    click(Location(958,465))
    wait(1)


def portal(afasta_rato):
    BUSY = True
    type("W")
    type("S")
    flag = False
    try:
        if REG_SEA.exists(Pattern(IMG_PORTAL).similar(SIM_IMG_PORTAL)):
            flag = True
            match = REG_SEA.find(Pattern(IMG_PORTAL).similar(SIM_IMG_PORTAL))
            location = match.getTarget()
            rightClick(Location(location.x, (location.y)))
            type(Key.SPACE)
            wait(8)
            print("ole")
            click(Location(958,629))
            type(Key.ENTER)
        else:
            print("Nao encontrou o portal")
            type("A")
            type("D")
            mouseMove(REG_SEA.getCenter())
            click(Location(960 + afasta_rato, 540 + afasta_rato))
            afasta_rato = afasta_rato + 10
    except:
        BUSY = False
        return
    BUSY = False
    e.repeat()
    return flag


def fecha_portal():
    BUSY = True
    type("W")
    type("S")
    try:
        print("olaaaaa")
        if REG_SEA.exists(Pattern(IMG_PORTALAZUL).similar(SIM_IMG_PORTALAZUL)):
            match = REG_SEA.find(Pattern(IMG_PORTALAZUL).similar(SIM_IMG_PORTALAZUL))
            click(Location(1125,419))
        wait(4)
        click(Location(1125,419))
    except:
        BUSY = False
        return
    BUSY = False
   
def kill_npc1(e):
    global BUSY
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        type("W")
        type("S")
        current_atk = Screen(0).capture(REG_ATK)
        try:
            match = REG_SEA.find(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1).targetOffset(0, -28))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=5)
            while datetime.datetime.now() < atk_timeout:
                type("F")
            type(Key.SPACE)
            for i in range(10):
                wait(1)
                type("4")
                wait(0.5)
                click(Location(1154,347))
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    type("6")
                    break
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()


def kill_npc2(e):
    global BUSY
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        type("W")
        current_atk = Screen(0).capture(REG_ATK)
        try:
            match = REG_SEA.find(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2).targetOffset(0, -28))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=5)
            while datetime.datetime.now() < atk_timeout:
                type("F")
            type(Key.SPACE)
            for i in range(10):
                wait(1)
                type("4")
                wait(0.5)
                click(Location(1154,347))
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    type("6")
                    break
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()


def kill_npc3(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        type("A")
        type("D")
        current_atk = Screen(0).capture(REG_ATK)
        type("6")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3).targetOffset(0, -28))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=5)
            while datetime.datetime.now() < atk_timeout:
                type("F")
            type(Key.SPACE)
            wait(1)
            for i in range(12):
                wait(0.8)
                type("4")
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    type("6")
                    break
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()


def kill_npc4(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        afasta_rato = 20
        type("D")
        type("A")
        BUSY = True
        current_atk = Screen(0).capture(REG_ATK)
        try:
            match = REG_SEA.find(Pattern(IMG_NPC4).similar(SIM_IMG_NPC4).targetOffset(0, -28))
            location = match.getTarget()
            type("9")
            click(location)
            rightClick(Location(location.x, location.y))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=5)
            while datetime.datetime.now() < atk_timeout:
                type("F")
            type(Key.SPACE)
            wait(1)
            for i in range(60):
                wait(0.5)
                type("4")
                wait(0.5)
                type("5")
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    type(Key.ENTER)
                    if portal(afasta_rato) == True:
                        print("Encontrou o portal")
                    else:
                        click(Location(1578,172))
                        wait(1)
                        click(Location(964,491))
                        wait(15)
                        click(Location(1047,631))
                        wait(2)
                        entra_mapa()
                    wait(1)
                    break      
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        type(Key.ENTER)
        BUSY = False
        ARRIVED = True
        e.repeat()


def kill_npc5(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        type("A")
        type("D")
        current_atk = Screen(0).capture(REG_ATK)
        try:
            match = REG_SEA.find(Pattern(IMG_NPC5).similar(SIM_IMG_NPC5).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, location.y))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=3)
            while datetime.datetime.now() < atk_timeout:
                type("F")
            type(Key.SPACE) 
            wait(2)
            for i in range(60):
                wait(0.5)
                type("4")
                wait(0.5)
                type("5")
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    break       
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()


def kill_npc6(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        type("A")
        type("D")
        current_atk = Screen(0).capture(REG_ATK)
        type("6")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC6).similar(SIM_IMG_NPC6).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, location.y))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=3)
            while datetime.datetime.now() < atk_timeout:
                type("F")
            type(Key.SPACE) 
            wait(2)
            for i in range(10):
                wait(1)
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    break  
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()



#######################################################################################################
#######################################################################################################
REG_SEA.onAppear(Pattern(IMG_PORTAL).similar(SIM_IMG_PORTAL), portal)
REG_SEA.onAppear(Pattern(IMG_PORTALAZUL).similar(SIM_IMG_PORTALAZUL), fecha_portal)
REG_SEA.onAppear(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1), kill_npc1)
REG_SEA.onAppear(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2), kill_npc2)
REG_SEA.onAppear(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3), kill_npc3)
REG_SEA.onAppear(Pattern(IMG_NPC4).similar(SIM_IMG_NPC4), kill_npc4)
REG_SEA.onAppear(Pattern(IMG_NPC5).similar(SIM_IMG_NPC5), kill_npc5)
#REG_SEA.onAppear(Pattern(IMG_NPC6).similar(SIM_IMG_NPC6), kill_npc6)
REG_SEA.observeInBackground(FOREVER)
########################################################################################################


# Configurações globais
CURRENT_POS = 0  # Posição inicial no padrão (cima esquerda)

def move(QUADRADO_COORDS):
    click(Location(1125,419))
    wait(0.5)
    global BUSY, CURRENT_POS
    if BUSY:
        return  # Evita múltiplas execuções simultâneas
    BUSY = True
    # Determina a próxima posição no padrão
    coordx, coordy = QUADRADO_COORDS[CURRENT_POS]
    click(Location(coordx, coordy))  # Move para a posição
    type("9")
    wait(0.5)
    type("V")
    wait(0.5)
    type(Key.SPACE)
    wait(0.5)
    type("4")
    CURRENT_POS = (CURRENT_POS + 1) % len(QUADRADO_COORDS)  # Retorna ao início após o último ponto
    BUSY = False



def check_revive():
    global BUSY
    global LOW_HP
    if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
        BUSY = True
        revived = False
        while revived == False:
            wait(0.5)
            click(REG_REVIVE.getCenter())
            wait(0.5)
            type("Q")
            wait(3)
            if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
                pass
            else:
                revived = True
        BUSY = False
        LOW_HP = True
        mouseMove(REG_SEA.getCenter())
        entra_mapa()


def calculacoord_radar():
    lista_radar = [(1534,160),(1535,210),(1599,210),(1597,159),(1566,188)]
    return lista_radar


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
        wait(1)
        #clica 2º concordo
        click(Location(960,620))
        #ate aqui faz login
        wait(5)
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


def main():
    global BUSY
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
    check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=36)
    coord = calculacoord_radar()
    entra_mapa()
    CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=10)
    while finished == False:
        if datetime.datetime.now() > check_revive_timeout:
            check_revive()
            check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
        if datetime.datetime.now() > check_update_timeout:
            check_update()
            check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=600)
        if BUSY == False:
            if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                if datetime.datetime.now() > CHECK_MOVE_TIMEOUT:
                    move(coord)
                    CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=15)
        if datetime.datetime.now() > finish_at:
            finished = True
    REG_SEA.stopObserver()
    run("cmd /C shutdown /s")

#configure(5)
main()