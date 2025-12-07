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
REG_CAPTAIN = Region(1135,351,246,181)

# REG_ATK IS THE REGION WHERE THE YOUR ATTACKERS WIDGET APPEAR, SELECT THE WIDGET
REG_ATK =  Region(54,142,212,52)
# REG_LOW_HP: BE ON LOW HP AND SELECT THE LAST PART OF YOUR HP BAR
# AND TAKE A SCREENSHOT OF A SMALL PIECE OF THE BAR WHEN ITS BLACK
REG_LOW_HP = Region(1630,439,49,27)
REG_CURRENT_HP = Region(1635,441,43,24)
REG_REP_BTN = Region(1482,871,47,48)
REG_REVIVE = Region(926,518,241,207)
REG_RELOG = Region(959,614,188,44)

# IMAGES
IMG_PLAYER = "IMG_PLAYER.png"
#IMG_NPC1 = "IMG_PARGOPROFUNDEZA.png"
IMG_NPC1 = "NPC_PATRULHADOR.png"
IMG_NPC2 = "IMG_DEMPESCUCUDO.png"
IMG_NPC3 = "IMG_PARGO.png"
IMG_EVENTCHEST = "IMG_EVENTCHEST.png"
IMG_LOW_HP = "IMG_LOW_HP.png"
IMG_CREP_BTN = "IMG_CREP_BTN.png"
IMG_REVIVE = "IMG_50REPAIR.png"
IMG_DARK = "IMG_DARK.png"
IMG_VIRGO = "IMG_VIRGO.png"
IMG_SAGI = "IMG_SAGI.png"
IMG_CANCER = "IMG_CANCER.png"
IMG_VIRGOMAP = "IMG_VIRGOMAP.png"
IMG_CARTOGRAFO = "IMG_CARTOGRAFO.png"
IMG_VIRGOFLYN = "IMG_VIRGOFLYN.png"
IMG_VIRGOARTEMIS = "IMG_VIRGOARTEMIS.png"
IMG_RADAR = "IMG_RADAR.png"
IMG_ENTRAR = Pattern("IMG_ENTRAR.png").similar(0.90)
IMG_RELOG = "IMG_RELOG.png"
IMG_AVANCAR = "IMG_AVANCAR.png"
IMG_RR = "IMG_RR1.png"
IMG_RR3 = "IMG_RR3.png"
IMG_AMBIENTE = "IMG_RR2.png"

# SIMILARITY
SIM_IMG_PLAYER = 0.8
SIM_IMG_NPC1 = 0.8
SIM_IMG_NPC2 = 0.7
SIM_IMG_NPC3 = 0.8
SIM_IMG_NPC4 = 0.7
SIM_IMG_VIRGO = 0.8
SIM_IMG_SAGI = 0.8
SIM_IMG_CANCER = 0.8
SIM_IMG_VIRGOMAP = 0.8
SIM_IMG_VIRGOFLYN = 0.7
SIM_IMG_VIRGOARTEMIS = 0.7
SIM_IMG_CARTOGRAFO = 0.8
SIM_IMG_ENTRAR = 0.95
SIM_IMG_AVANCAR = 0.9
SIM_IMG_EVENTCHEST = 0.7
SIM_IMG_LOW_HP = 0.75
SIM_IMG_ATK = 0.6
SIM_IMG_RADAR = 0.85
SIM_IMG_CREP_BTN = 0.85
SIM_IMG_REVIVE = 0.7
SIM_IMG_RELOG = 0.8
SIM_IMG_RR = 0.8
SIM_IMG_RR3 = 0.8
SIM_IMG_AMBIENTE = 0.8



# GLOBALS
########### HOW LONG TO RUN THE BOT ##############
RUNNING_HOURS = 1.5
BUSY = False
ARRIVED = False
LOW_HP = False
TELEPORT = False
CAPTAIN = False

MAX_ARRIVAL_WAIT = datetime.datetime.now() + datetime.timedelta(seconds=90)
NPC_HP = 100
# NPC_WAIT IS CALCULATED AUTOMATICALLY
NPC_WAIT = None
PLAYER_DAMAGE = 50
PLAYER_RELOAD = 2

LAST_MOVE = None
LAST_POS = None
CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=5)

def kill_npc1(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        current_atk = Screen(0).capture(REG_ATK)
        type("4")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y + 35)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=4)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.6)):
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            type(Key.SPACE)
            wait(2)
            for i in range(45):
                wait(1)
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    print("ola")
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
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        BUSY = True
        current_atk = Screen(0).capture(REG_ATK)
        type("4")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x - 20, (location.y)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=3)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.6)):         
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            type(Key.SPACE)
            wait(2)
            for i in range(100):
                wait(1)
                if REG_ATK.exists(Pattern(IMG_DARK).similar(0.99)):
                    print("OLE")
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
        type("4")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y + 30)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=3)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.6)):         
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            #REG_ATK.wait(Pattern(IMG_ATK).similar(SIM_IMG_ATK), 5)
            #type("T")
            type(Key.SPACE) 
            wait(2)
            for i in range(40):
                wait(4)
                type("4")
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


def collect_eventchest(e):
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
        try:
            match = REG_SEA.find(Pattern(IMG_EVENTCHEST).similar(SIM_IMG_EVENTCHEST))
            location = match.getTarget()
            click(location)
            wait(6)
            mouseMove(REG_SEA.getCenter())
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()


def teleport():
    global BUSY
    global TELEPORT
    if BUSY == True:
        wait(10)
    BUSY = True
    type("W")
    type("S")
    try:
        click(Location(1560, 186))
        wait(1)
        click(Location(457, 918))
        type("9")
        wait(30)
        type("6")
        #TELEPORT FALSE = 48/3
        #TELEPORT TRUE = 52/1
        if TELEPORT == False:
            #teleport 48 to 52
            wait(1)
            click(Location(1039, 512))
            wait(16)
            TELEPORT = True
        else:
            #teleport 52 to 48
            wait(1)
            click(Location(1093, 545))
            wait(16)
            TELEPORT = False
    except:
        BUSY = False
        return
    BUSY = False


def speedup(x):
    if x == 1:
        for i in range(1):
            click(Location(1055, 475))
            wait(0.5)
            mouseMove(Location(995, 505))
            doubleClick(Location(995, 505))
            wait(0.5)
            click(Location(955, 710))
    if x == 2:
         for i in range(2):
            click(Location(1055, 640))
            wait(0.5)
            mouseMove(Location(995, 505))
            doubleClick(Location(995, 505))
            wait(0.5)
            click(Location(955, 710))
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
    click(Location(1340, 340))
    click(Location(1372, 309))
    type("3")
    return


def captain_virgonormal():
    global BUSY
    #BUSY = True
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
        #Mouse.wheel(WHEEL_DOWN, 5)
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_VIRGO).similar(SIM_IMG_VIRGO)):
                match = REG_SEA.find(Pattern(IMG_VIRGO).similar(SIM_IMG_VIRGO).targetOffset(50, -20))
                location = match.getTarget()
                #clica no sagitario
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 5)
                for i in range(15):
                    if REG_CAPTAIN.exists(Pattern(IMG_VIRGOMAP).similar(SIM_IMG_VIRGOMAP)):
                        match = REG_CAPTAIN.find(Pattern(IMG_VIRGOMAP).similar(SIM_IMG_VIRGOMAP).targetOffset(-100, 0))
                        location = match.getTarget()
                        click(Location(location))
                        wait(0.5)
                        if REG_SEA.exists(Pattern(IMG_ENTRAR).similar(SIM_IMG_ENTRAR)):
                            click(Location(955,750))
                            speedup(1)
                            #BUSY = False
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
    #BUSY = False
    
    
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
                            speedup(1)
                            BUSY = False
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
                            speedup(1)
                            BUSY = False
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
        #Mouse.wheel(WHEEL_DOWN, 10)
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_SAGI).similar(SIM_IMG_SAGI)):
                match = REG_SEA.find(Pattern(IMG_SAGI).similar(SIM_IMG_SAGI).targetOffset(50, -20))
                location = match.getTarget()
                #clica no sagitario
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 10)
                for i in range(15):
                    if REG_CAPTAIN.exists(Pattern(IMG_CARTOGRAFO).similar(SIM_IMG_CARTOGRAFO)):
                        match = REG_CAPTAIN.find(Pattern(IMG_CARTOGRAFO).similar(SIM_IMG_CARTOGRAFO).targetOffset(-100, 0))
                        location = match.getTarget()
                        click(Location(location))
                        wait(0.5)
                        if REG_SEA.exists(Pattern(IMG_ENTRAR).similar(SIM_IMG_ENTRAR)):
                            click(Location(955,750))
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
        #Mouse.wheel(WHEEL_DOWN, 10)
        for i in range(5):
            if REG_SEA.exists(Pattern(IMG_CANCER).similar(SIM_IMG_CANCER)):
                match = REG_SEA.find(Pattern(IMG_CANCER).similar(SIM_IMG_CANCER).targetOffset(50, -20))
                location = match.getTarget()
                #clica no cancer
                click(Location(location))
                wait(0.5)
                mouseMove(Location(1170, 380))
                Mouse.wheel(WHEEL_DOWN, 12)
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


REG_SEA.onAppear(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1), kill_npc1)
REG_SEA.onAppear(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2), kill_npc2)
#REG_SEA.onAppear(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3), kill_npc3)
REG_SEA.onAppear(Pattern(IMG_EVENTCHEST).similar(SIM_IMG_EVENTCHEST), collect_eventchest)
REG_SEA.observeInBackground(FOREVER)
#REG_CAPTAIN.observeInBackground(FOREVER)


def calculate_npc_wait():
    wait_time = (NPC_HP / PLAYER_DAMAGE) * PLAYER_RELOAD
    return wait_time

def check_repair():
    global LOW_HP
    if REG_LOW_HP.exists(Pattern(IMG_LOW_HP).similar(SIM_IMG_LOW_HP)):
        LOW_HP = True

def repair():
    global BUSY
    global LOW_HP
    if BUSY == True:
        return
    else:
        BUSY = True
        current_hp_image = Screen(0).capture(REG_CURRENT_HP)
        type("Q")
        wait(3)
        if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
            BUSY = False
            LOW_HP = False
            return
        if REG_CURRENT_HP.exists(Pattern(current_hp_image).similar(0.85)):
            type("Q")
            wait(1)
            type("4")
        REG_REP_BTN.waitVanish(Pattern(IMG_CREP_BTN).similar(SIM_IMG_CREP_BTN), 50)
        BUSY = False
        LOW_HP = False


def generate_move():
    return random.randrange(0, 5)

def move(lista_radar):
    global LAST_MOVE
    global LAST_POS
    global ARRIVED
    global CHECK_MOVE_TIMEOUT
    global MAX_ARRIVAL_WAIT
    ARRIVED = False
    random_pick = generate_move()
    
    # AVOID MOVE
    while (random_pick == LAST_MOVE):
        random_pick = generate_move()
   # END AVOID MOVE 
    x = random.randrange(450,1450)
    y = random.randrange(170,930)     
    LAST_MOVE = random_pick
    if random_pick == 1:
        coordx = lista_radar[random_pick][0]
        coordy = lista_radar[random_pick][1]
        click(Location(coordx,coordy))
        wait(0.5)
        click(Location(x,y))
        wait(0.5)
        type("V")
    if random_pick == 2:
        coordx = lista_radar[random_pick][0]
        coordy = lista_radar[random_pick][1]
        click(Location(coordx,coordy))
        wait(0.5)
        click(Location(x,y))
        wait(0.5)
        type("V")
    if random_pick == 3:
        coordx = lista_radar[random_pick][0]
        coordy = lista_radar[random_pick][1]
        click(Location(coordx,coordy))
        wait(0.5)
        click(Location(x,y))
        wait(0.5)
        type("V")
    if random_pick == 4:
        coordx = lista_radar[random_pick][0]
        coordy = lista_radar[random_pick][1]
        click(Location(coordx,coordy))
        wait(0.5)
        click(Location(x,y))
        wait(0.5)
        type("V")
    if random_pick == 0:
        coordx = lista_radar[random_pick][0]
        coordy = lista_radar[random_pick][1]
        click(Location(coordx,coordy))
        wait(0.5)
        click(Location(x,y))
        wait(0.5)
        type("V")
    CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=8)
    MAX_ARRIVAL_WAIT = datetime.datetime.now() + datetime.timedelta(seconds=30)
    type(Key.SPACE)


def check_arrival():
    global ARRIVED
    global CHECK_MOVE_TIMEOUT
    click(LAST_POS)
    if REG_SEA.exists(Pattern(IMG_PLAYER).similar(SIM_IMG_PLAYER)):
        ARRIVED = True
    else:
        CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=8)
    type(Key.SPACE)


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


def calculacoord_radar():
    radar = Screen(0).exists(Pattern(IMG_RADAR).similar(SIM_IMG_RADAR))
    posicao = radar.getTarget()
    x = posicao.getX()
    y = posicao.getY()
    lista_radar = [(x+20,y),(x+100,y),(x+20,y+70),(x+100,y+70),(x+65,y+32)]
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
    global NPC_WAIT
    global ARRIVED
    global CAPTAIN
    global BUSY
    NPC_WAIT = calculate_npc_wait()
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    check_relog_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
    check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
    check_teleport_timeout = datetime.datetime.now() + datetime.timedelta(seconds=600000)
    check_captainvirgo_timeout = datetime.datetime.now() + datetime.timedelta(seconds=601112)
    check_captainsagi_timeout = datetime.datetime.now() + datetime.timedelta(seconds=255550)
    check_captaincancer_timeout = datetime.datetime.now() + datetime.timedelta(seconds=211110)
    check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=36)
    coord = calculacoord_radar()
    while finished == False:
        if BUSY == False and ARRIVED == True:
            move(coord)
        if datetime.datetime.now() > check_revive_timeout:
            check_revive()
            check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
        if datetime.datetime.now() > check_relog_timeout:
            check_relog()
            check_relog_timeout = datetime.datetime.now() + datetime.timedelta(seconds=300)
        if datetime.datetime.now() > check_teleport_timeout:
            teleport()
            check_teleport_timeout = datetime.datetime.now() + datetime.timedelta(seconds=280)
        if datetime.datetime.now() > check_captainvirgo_timeout:
            captain_virgonormal()
            check_captainvirgo_timeout = datetime.datetime.now() + datetime.timedelta(seconds=180)
        if datetime.datetime.now() > check_captainsagi_timeout:
            captain_sagi()
            check_captainsagi_timeout = datetime.datetime.now() + datetime.timedelta(seconds=85)
        if datetime.datetime.now() > check_captaincancer_timeout:
            captain_cancer()
            check_captaincancer_timeout = datetime.datetime.now() + datetime.timedelta(seconds=115)
        if datetime.datetime.now() > check_update_timeout:
            check_update()
            check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
        if BUSY == False and ARRIVED == False:
            if datetime.datetime.now() > MAX_ARRIVAL_WAIT:
                ARRIVED = True
            if ARRIVED == False:
                if datetime.datetime.now() > CHECK_MOVE_TIMEOUT:
                    check_arrival()
        check_repair()
        if LOW_HP == True:
            repair()
        if datetime.datetime.now() > finish_at:
            finished = True
    REG_SEA.stopObserver()
    run("cmd /C shutdown /s")

#configure(5)
main()