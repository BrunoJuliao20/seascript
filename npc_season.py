#NPC
import random
import datetime
Settings.MoveMouseDelay = 0.25
# KEEP OBSERVE SCAN RATE IN 1 TO USE LESS CPU
# INCREASE IF YOU WANT
Settings.ObserveScanRate = 1

# CONFIGURATION
# REGIONS
# REG_SEA KEEP IT IN 800X600 FOR LESS CPU USAGE
REG_SEA = Region(452,165,1015,756)
REG_SEA_2 = Region(REG_SEA.getX() - 1, REG_SEA.getY() - 1, REG_SEA.getW() - 1, REG_SEA.getH() - 1)
# REG_ATK IS THE REGION WHERE THE YOUR ATTACKERS WIDGET APPEAR, SELECT THE WIDGET
REG_ATK = Region(96,186,215,55)
# REG_LOW_HP: BE ON LOW HP AND SELECT THE LAST PART OF YOUR HP BAR
# AND TAKE A SCREENSHOT OF A SMALL PIECE OF THE BAR WHEN ITS BLACK
REG_LOW_HP = Region(1635,600,49,23)
REG_CURRENT_HP = Region(1635,597,47,27)
REG_REP_BTN = Region(1363,981,48,51)
REG_REVIVE = Region(751,532,156,139)
REG_RELOG = Region(959,614,188,44)

# IMAGES
IMG_PLAYER = "IMG_PLAYER.png"
IMG_NPC = "NPC_RENOME.png"
IMG_NPC2 = "NPC_ESGRIMI.png"
IMG_NPC3 = "NPC_REVENGE.png"
IMG_LOW_HP = "IMG_LOW_HP.png"
IMG_CREP_BTN = "IMG_CREP_BTN.png"
IMG_REVIVE = "IMG_REVIVE.png"
IMG_RELOG = "IMG_RELOG.png"

# SIMILARITY
SIM_IMG_PLAYER = 0.7
SIM_IMG_NPC = 0.8
SIM_IMG_NPC2 = 0.8
SIM_IMG_NPC3 = 0.5
SIM_IMG_ATK = 0.8
SIM_IMG_LOW_HP = 0.75
SIM_IMG_CREP_BTN = 0.85
SIM_IMG_REVIVE = 0.8
SIM_IMG_RELOG = 0.8

# GLOBALS
# HOW LONG TO RUN THE BOT
RUNNING_HOURS = 3
BUSY = False
ARRIVED = False
LOW_HP = False
MAX_ARRIVAL_WAIT = datetime.datetime.now() + datetime.timedelta(seconds=90)

NPC_HP = 100
# NPC_WAIT IS CALCULATED AUTOMATICALLY
NPC_WAIT = None
PLAYER_DAMAGE = 50
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

LOC_POS_01 = Location(1227, 133)
LOC_POS_02 = Location(1294, 138)
LOC_POS_03 = Location(1298, 180)
LOC_POS_04 = Location(1231, 174)
LOC_POS_05 = Location(1261, 154)

# REGIONS RELATED TO THE MINIMAP CLICK LOCATIONS ABOVE (SELECT THE SEA, FREE OF ISLANDS)

REG_POS_01 = Region(1560,110,6,61)
REG_POS_02 = Region(1575,134,20,42)
REG_POS_03 = Region(1564,159,73,29)
REG_POS_04 = Region(1588,180,51,10)
REG_POS_05 = Region(1606,151,34,7)
# End


def kill_npc(e):
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
        #type("4")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC).similar(SIM_IMG_NPC).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            click(Location(location.x, (location.y + 35)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
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
            type("9")
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()

REG_SEA.onAppear(Pattern(IMG_NPC).similar(SIM_IMG_NPC), kill_npc)
REG_SEA.observeInBackground(FOREVER)

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
        #type("4")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            click(Location(location.x, (location.y + 35)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
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
            wait(4)
            type("T")
            wait(2)
            type("9")
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()

REG_SEA.onAppear(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2), kill_npc2)
REG_SEA.observeInBackground(FOREVER)


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
        #type("4")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            click(Location(location.x, (location.y + 35)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
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
            wait(60)
            type("5")
            type("6")
        except:
            BUSY = False
            ARRIVED = True
            e.repeat()
            return
        BUSY = False
        ARRIVED = True
        e.repeat()

REG_SEA.onAppear(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3), kill_npc3)
REG_SEA.observeInBackground(FOREVER)


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
        wait(2)
        if REG_REVIVE.exists(Pattern(IMG_REVIVE).similar(SIM_IMG_REVIVE)):
            BUSY = False
            LOW_HP = False
            return
        if REG_CURRENT_HP.exists(Pattern(current_hp_image).similar(0.85)):
            type("Q")
            wait(1)
            type("Q")
        REG_REP_BTN.waitVanish(Pattern(IMG_CREP_BTN).similar(SIM_IMG_CREP_BTN), 50)
        BUSY = False
        LOW_HP = False

def generate_move():
    return random.randrange(1, 6)

def move():
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
         
    LAST_MOVE = random_pick
    if random_pick == 1:
        LAST_POS = LOC_POS_01
        mouseMove(LOC_POS_01)
        wait(1)
        click(LOC_POS_01)
        random_x = random.randrange(REG_POS_01.getX(), (REG_POS_01.getX() + REG_POS_01.getW() - 5))
        random_y = random.randrange(REG_POS_01.getY(), (REG_POS_01.getY() + REG_POS_01.getH() - 5))
        mouseMove(Location(random_x, random_y))
        wait(1)
        click(Location(random_x, random_y))
        type("V")
    if random_pick == 2:
        LAST_POS = LOC_POS_02
        mouseMove(LOC_POS_02)
        wait(2)
        click(LOC_POS_02)
        random_x = random.randrange(REG_POS_02.getX(), (REG_POS_02.getX() + REG_POS_02.getW() - 5))
        random_y = random.randrange(REG_POS_02.getY(), (REG_POS_02.getY() + REG_POS_02.getH() - 5))
        mouseMove(Location(random_x, random_y))
        wait(1)
        click(Location(random_x, random_y))
        type("V")
    if random_pick == 3:
        LAST_POS = LOC_POS_03
        mouseMove(LOC_POS_03)
        wait(1)
        click(LOC_POS_03)
        random_x = random.randrange(REG_POS_03.getX(), (REG_POS_03.getX() + REG_POS_03.getW() - 5))
        random_y = random.randrange(REG_POS_03.getY(), (REG_POS_03.getY() + REG_POS_03.getH()- 5))
        mouseMove(Location(random_x, random_y))
        wait(1)
        click(Location(random_x, random_y))
        type("V")
    if random_pick == 4:
        LAST_POS = LOC_POS_04
        mouseMove(LOC_POS_04)
        wait(1)
        click(LOC_POS_04)
        random_x = random.randrange(REG_POS_04.getX(), (REG_POS_04.getX() + REG_POS_04.getW() - 5))
        random_y = random.randrange(REG_POS_04.getY(), (REG_POS_04.getY() + REG_POS_04.getH() - 5))
        mouseMove(Location(random_x, random_y))
        wait(1)
        click(Location(random_x, random_y))
        type("V")
    if random_pick == 5:
        LAST_POS = LOC_POS_05
        mouseMove(LOC_POS_05)
        wait(1)
        click(LOC_POS_05)
        random_x = random.randrange(REG_POS_05.getX(), (REG_POS_05.getX() + REG_POS_05.getW() - 5))
        random_y = random.randrange(REG_POS_05.getY(), (REG_POS_05.getY() + REG_POS_05.getH() - 5))
        mouseMove(Location(random_x, random_y))
        wait(1)
        click(Location(random_x, random_y))
        type("V")
    CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=5)
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
            mouseMove(Location(0, 0))
            wait(0.5)
            click(REG_REVIVE.getCenter())
            mouseMove(Location(0, 0))
            wait(5)
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
            mouseMove(Location(0, 0))
            wait(0.5)
            try:
                REG_RELOG.click(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG))
            except:
                pass
            mouseMove(Location(0, 0))
            wait(10)
            if REG_RELOG.exists(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG)):
                pass
            else:
                relogged = True
        BUSY = False
        mouseMove(REG_SEA.getCenter())

def configure(position):
    if position == 1:
        click(LOC_POS_01)
    if position == 2:
        click(LOC_POS_02)
    if position == 3:
        click(LOC_POS_03)
    if position == 4:
        click(LOC_POS_04)
    if position == 5:
        click(LOC_POS_05)       

def main():
    global NPC_WAIT
    global ARRIVED
    NPC_WAIT = calculate_npc_wait()
    finish_at = datetime.datetime.now() + datetime.timedelta(hours=RUNNING_HOURS)
    finished = False
    check_relog_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
    check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
    while finished == False:
        if BUSY == False and ARRIVED == True:
            move()
        if datetime.datetime.now() > check_revive_timeout:
            check_revive()
            check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
        if datetime.datetime.now() > check_relog_timeout:
            check_relog()
            check_relog_timeout = datetime.datetime.now() + datetime.timedelta(seconds=15)
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
    REG_SEA_2.stopObserver()
    run("cmd /C shutdown /s")

#configure(5)
main()