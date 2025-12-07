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
REG_ATK =  Region(55,142,203,48)
# REG_LOW_HP: BE ON LOW HP AND SELECT THE LAST PART OF YOUR HP BAR
# AND TAKE A SCREENSHOT OF A SMALL PIECE OF THE BAR WHEN ITS BLACK
REG_LOW_HP = Region(1630,439,49,27)
REG_CURRENT_HP = Region(1635,441,43,24)
REG_REP_BTN = Region(1482,871,47,48)
REG_REVIVE = Region(751,532,156,139)
REG_RELOG = Region(959,614,188,44)

# IMAGES
IMG_PLAYER = "IMG_PLAYER.png"
IMG_NPC1 = "IMG_DEMPESCUCUDO.png"
IMG_NPC2 = "NPC_CAMPEONATO.png"
IMG_NPC3 = "NPC_2024.png"
IMG_DESTROCO = "IMG_DESTROCO.png"
IMG_EVENTCHEST = Pattern("IMG_EVENTCHEST.png").similar(0.60)
IMG_LOW_HP = "IMG_LOW_HP.png"
IMG_CREP_BTN = "IMG_CREP_BTN.png"
IMG_REVIVE = "IMG_REVIVE.png"
IMG_DARK = "IMG_DARK.png"
IMG_RR = "IMG_RR1.png"
IMG_RR3 = "IMG_RR3.png"
IMG_AMBIENTE = "IMG_RR2.png"
IMG_RADAR = "IMG_RADAR.png"

# SIMILARITY
SIM_IMG_PLAYER = 0.8
SIM_IMG_NPC1 = 0.7
SIM_IMG_NPC2 = 0.6
SIM_IMG_NPC3 = 0.7
SIM_IMG_DESTROCO = 0.75
SIM_IMG_EVENTCHEST = 0.70
SIM_IMG_ATK = 0.6
SIM_IMG_RR = 0.9
SIM_IMG_RR3 = 0.9
SIM_IMG_AMBIENTE = 0.9
SIM_IMG_LOW_HP = 0.75
SIM_IMG_CREP_BTN = 0.85
SIM_IMG_REVIVE = 0.8
SIM_IMG_RADAR = 0.8

# GLOBALS
# HOW LONG TO RUN THE BOT
RUNNING_HOURS = 12
BUSY = False
ARRIVED = False
LOW_HP = False
MAX_ARRIVAL_WAIT = datetime.datetime.now() + datetime.timedelta(seconds=90)

NPC_HP = 100
# NPC_WAIT IS CALCULATED AUTOMATICALLY
NPC_WAIT = None
PLAYER_DAMAGE = 51
PLAYER_RELOAD = 2

LAST_MOVE = None
LAST_POS = None
CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=5)

# LOCATIONS TO CLICK ON THE MINIMAP FOR MOVING (TRY TO AVOID ISLAND)
# UNCOMMENT THE configure() FUNCTION ON THE LAST CODE LINE
# COMMENT THE main() FUNCTIONS PLACING A # IN FRONT OF IT
# INSERT THE NUMBER OF THE POSITION IN THE configure(number-of-position-here)
# IT WILL CLICK ON THE DEFIRED POSITION
# FOR YOU TO SELECT THE RELATED SEA REGION
#LOC_POS_01 = Location(475, 950)

# REGIONS RELATED TO THE MINIMAP CLICK LOCATIONS ABOVE (SELECT THE SEA, FREE OF ISLANDS)

REG_POS_01 = Region(1559,105,25,17)
REG_POS_02 = Region(1557,174,23,14)
REG_POS_03 = Region(1600,174,39,13)
REG_POS_04 = Region(1624,108,15,19)
REG_POS_05 = Region(1588,137,26,28)
# End


def kill_npc1(e):
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
            match = REG_SEA.find(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1).targetOffset(22, -32))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y + 35)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=4)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.8)):
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            #REG_ATK.wait(Pattern(IMG_ATK).similar(SIM_IMG_ATK), 5)
            #type("T")
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


def kill_npc2(e):
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
        type("5")
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
            #REG_ATK.wait(Pattern(IMG_ATK).similar(SIM_IMG_ATK), 5)
            #type("T")
            type(Key.SPACE)
            wait(2)
            for i in range(20):
                wait(12)
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
            match = REG_SEA.find(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3).targetOffset(-30, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, location.y))
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
            type("5")
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


def kill_destroco(e):
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
            match = REG_SEA.find(Pattern(IMG_DESTROCO).similar(SIM_IMG_DESTROCO).targetOffset(0, -26))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y + 30)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.8)):
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            #REG_ATK.wait(Pattern(IMG_ATK).similar(SIM_IMG_ATK), 5)
            type(Key.SPACE)
            type("F")
            wait(2)
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
            rightClick(location)
            wait(1)
            mouseMove(REG_SEA.getCenter())
            type(Key.SPACE)
            end_wait = False
            wait_limit = datetime.datetime.now() + datetime.timedelta(seconds=5)
            wait_region = Region((location.x - 100), (location.y - 100), 200, 200)
            while end_wait == False:
                if wait_region.exists(Pattern(IMG_EVENTCHEST).similar(SIM_IMG_EVENTCHEST)):
                    pass
                else:
                    end_wait = True
                if datetime.datetime.now() > wait_limit:
                    end_wait = True
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()


REG_SEA.onAppear(Pattern(IMG_EVENTCHEST).similar(SIM_IMG_EVENTCHEST), collect_eventchest)
REG_SEA.onAppear(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1), kill_npc1)
#REG_SEA.onAppear(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2), kill_npc2)
REG_SEA.onAppear(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3), kill_npc3)
#REG_SEA.onAppear(Pattern(IMG_DESTROCO).similar(SIM_IMG_DESTROCO), kill_destroco)
REG_SEA.observeInBackground(FOREVER)


def calculate_npc_wait():
    wait_time = (NPC_HP / PLAYER_DAMAGE) * PLAYER_RELOAD
    return wait_time

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
        wait(900)
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
            type("Q")
            if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
                pass
            else:
                revived = True
        BUSY = False
        LOW_HP = True
        mouseMove(REG_SEA.getCenter())


def calculacoord_radar():
    radar = Screen(0).exists(Pattern(IMG_RADAR).similar(SIM_IMG_RADAR))
    posicao = radar.getTarget()
    x = posicao.getX()
    y = posicao.getY()
    lista_radar = [(x+20,y),(x+100,y),(x+20,y+70),(x+100,y+70),(x+65,y+32)]
    return lista_radar


def main():
    global NPC_WAIT
    global ARRIVED
    NPC_WAIT = calculate_npc_wait()
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=10)
    check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=36)
    coord = calculacoord_radar()
    while finished == False:
        if BUSY == False and ARRIVED == True:
            move(coord)
        if datetime.datetime.now() > check_revive_timeout:
            check_revive()
            check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
        if datetime.datetime.now() > check_update_timeout:
            check_update()
            check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=600)
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