#NPC
import random
import datetime
Settings.MoveMouseDelay = 0.3
# KEEP OBSERVE SCAN RATE IN 1 TO USE LESS CPU
# INCREASE IF YOU WANT
Settings.ObserveScanRate = 1
from math import sqrt

# CONFIGURATION
# REGIONS
# REG_SEA KEEP IT IN 800X600 FOR LESS CPU USAGE
REG_SEA = Region(452,165,1015,756)
REG_ARPOON_LOAD = Region(373,897,78,85)

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
IMG_NPC1 = "IMG_GUANGEE.png"
IMG_NPC2 = "IMG_OLHONEGRO.png"
IMG_NPC3 = "IMG_DESTROCO.png"
IMG_NPC4 = "IMG_FRUTA.png"
IMG_EVENTCHEST = Pattern("IMG_EVENTCHEST.png").similar(0.60)
IMG_CHEST1= "IMG_CHEST1.PNG"
IMG_CHEST2= "IMG_CHEST2.png"
IMG_CHEST = "IMG_CHEST.png"
IMG_LOW_HP = "IMG_LOW_HP.png"
IMG_DARK = "IMG_DARK.png"
IMG_ARPAO100 = "IMG_ARPAO100.png"
IMG_CREP_BTN = "IMG_CREP_BTN.png"
IMG_REVIVE = "IMG_50REPAIR.png"
IMG_RELOG = "IMG_RELOG.png"
IMG_RADAR = "IMG_RADAR.png"
IMG_RR = "IMG_RR1.png"
IMG_RR3 = "IMG_RR3.png"
IMG_AMBIENTE = "IMG_RR2.png"

# SIMILARITY
SIM_IMG_PLAYER = 0.7
SIM_IMG_NPC1 = 0.75
SIM_IMG_NPC2 = 0.75
SIM_IMG_NPC3 = 0.75
SIM_IMG_NPC4 = 0.8
SIM_IMG_EVENTCHEST = 0.7
SIM_IMG_CHEST1 = 0.7
SIM_IMG_CHEST2 = 0.7
SIM_IMG_CHEST = 0.36
SIM_IMG_ARPAO100 = 0.9
SIM_IMG_ATK = 0.6
SIM_IMG_LOW_HP = 0.75
SIM_IMG_CREP_BTN = 0.85
SIM_IMG_REVIVE = 0.8
SIM_IMG_RELOG = 0.8
SIM_IMG_RADAR = 0.8
SIM_IMG_RELOG = 0.8
SIM_IMG_RR = 0.8
SIM_IMG_RR3 = 0.8
SIM_IMG_AMBIENTE = 0.8

# GLOBALS
# HOW LONG TO RUN THE BOT
RUNNING_HOURS = 6
BUSY = False
ARRIVED = False
LOW_HP = False
MAX_ARRIVAL_WAIT = datetime.datetime.now() + datetime.timedelta(seconds=90)

# NPC_WAIT IS CALCULATED AUTOMATICALLY
NPC_WAIT = None
LAST_MOVE = None
LAST_POS = None
CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=5)

# LOCATIONS TO CLICK ON THE MINIMAP FOR MOVING (TRY TO AVOID ISLAND)
# UNCOMMENT THE configure() FUNCTION ON THE LAST CODE LINE
# COMMENT THE main() FUNCTIONS PLACING A # IN FRONT OF IT
# INSERT THE NUMBER OF THE POSITION IN THE configure(number-of-position-here)
# IT WILL CLICK ON THE DEFIRED POSITION
# FOR YOU TO SELECT THE RELATED SEA REGION

# REGIONS RELATED TO THE MINIMAP CLICK LOCATIONS ABOVE (SELECT THE SEA, FREE OF ISLANDS)
# End


def kill_npc1(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        check_arpoon()
        BUSY = True
        current_atk = Screen(0).capture(REG_ATK)
        type("A")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y +1)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.8)):
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            type(Key.SPACE)
            wait(2)
            for i in range(25):
                wait(5)
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


def kill_npc2(e):
    global BUSY
    global ARRIVED
    if BUSY == True:
        wait(2)
        e.repeat()
        return
    else:
        check_arpoon()
        BUSY = True
        current_atk = Screen(0).capture(REG_ATK)
        type("S")
        try:
            match = REG_SEA.find(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.6)):         
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            type(Key.SPACE)
            wait(1)
            for i in range(25):
                wait(5)
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
        check_arpoon()
        BUSY = True
        type("A")
        type("D")
        current_atk = Screen(0).capture(REG_ATK)
        try:
            match = REG_SEA.find(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3).targetOffset(0, -30))
            location = match.getTarget()
            click(location)
            rightClick(Location(location.x, (location.y + 3)))
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
            wait(1)
            for i in range(25):
                wait(0.5)
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



def kill_npc4(e):
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
            match = REG_SEA.find(Pattern(IMG_NPC4).similar(SIM_IMG_NPC4).targetOffset(0,0))
            location = match.getTarget()
            click(location)
            wait(0.2)
            rightClick(Location(location.x, (location.y)))
            atk_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6)
            while datetime.datetime.now() < atk_timeout:
                type("F")
                if REG_ATK.exists(Pattern(current_atk).similar(0.6)):         
                    pass
                else:
                    wait(Pattern(current_atk).similar(0.8), NPC_WAIT)
                    break
            type(Key.SPACE)
            wait(1)
            for i in range(3):
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
            mouseMove(REG_SEA.getCenter())
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
        

def check_arpoon():
    global BUSY
    BUSY = True
    try:
        if REG_ARPOON_LOAD.exists(Pattern(IMG_ARPAO100).similar(SIM_IMG_ARPAO100)):
            click(Location(1532,216))
            wait(1)
            type("9")
            rightClick(Location(460,300))
            wait(16)
            type("9")
            rightClick(Location(453,920))
            wait(8)
            type("4")
            mouseMove(REG_ARPOON_LOAD.getCenter())
            wait(1)
            click(REG_ARPOON_LOAD.getCenter())
            wait(10)
            mouseMove(REG_SEA.getCenter())
            wait(9)
            type("9")
            eldourado()
    except:
        pass
    BUSY = False


def eldourado():
    velocidade = 50  # Velocidade do barco em pixels por segundo (ajuste conforme necessário)
    while True:
        # Buscar todas as caixas visíveis
        caixas = list(REG_SEA.findAll(Pattern(IMG_CHEST).similar(SIM_IMG_CHEST))) if exists(IMG_CHEST) else []        
        # Se não houver mais caixas, verificar novamente antes de finalizar
        if not caixas:
            wait(0.5)  # Aguarda um pouco e verifica novamente
            caixas = list(REG_SEA.findAll(Pattern(IMG_CHEST).similar(SIM_IMG_CHEST))) if exists(IMG_CHEST) else []
            
            if not caixas:
                print("Todas as caixas foram coletadas!")
                break  # Sai do loop se realmente não houver mais caixas

        # Localizar o jogador (barco)
        player = find(IMG_PLAYER).getCenter()  # Obtém o centro do barco

        # Variáveis para rastrear a caixa mais próxima
        caixa_mais_proxima = None
        menor_distancia = 999 

        # Encontrar a caixa mais próxima
        for caixa in caixas:
            pos_caixa = caixa.getCenter()
            distancia = sqrt((pos_caixa.x - player.x)**2 + (pos_caixa.y - player.y - 20)**2)
            
            if distancia < menor_distancia:
                menor_distancia = distancia
                caixa_mais_proxima = caixa

        # Clicar na caixa mais próxima e ajustar o tempo de espera
        if caixa_mais_proxima:
            pos_mais_proxima = caixa_mais_proxima.getCenter()
            click(pos_mais_proxima)  # Mover para a caixa mais próxima

            # Calcular o tempo de espera com base na distância
            tempo_espera = menor_distancia / velocidade
            type("9")
            wait(tempo_espera)  # Aguarda o tempo necessário para o barco chegar
        else:
            print("Erro: Nenhuma caixa encontrada.")
            if REG_SEA.exists(Pattern(IMG_CHEST).similar(0.47)):
                eldourado()


REG_SEA.onAppear(Pattern(IMG_NPC1).similar(SIM_IMG_NPC1), kill_npc1)
REG_SEA.onAppear(Pattern(IMG_NPC2).similar(SIM_IMG_NPC2), kill_npc2)
REG_SEA.onAppear(Pattern(IMG_NPC3).similar(SIM_IMG_NPC3), kill_npc3)
#REG_SEA.onAppear(Pattern(IMG_NPC4).similar(SIM_IMG_NPC4), kill_npc4)
REG_SEA.onAppear(Pattern(IMG_EVENTCHEST).similar(SIM_IMG_EVENTCHEST), collect_eventchest)
REG_SEA.observeInBackground(FOREVER)


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
    return random.randrange(0, 5)


def move(lista_radar):
    global BUSY
    if BUSY == True:
        return
        exit(0)
    else:
        BUSY = True
        global LAST_MOVE
        global LAST_POS
        global CHECK_MOVE_TIMEOUT
        random_pick = generate_move()
        # AVOID not MOVE
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
        CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=20)
        type(Key.SPACE)
        BUSY = False


def calculacoord_radar():
    radar = Screen(0).exists(Pattern(IMG_RADAR).similar(SIM_IMG_RADAR))
    posicao = radar.getTarget()
    x = posicao.getX()
    y = posicao.getY()
    lista_radar = [(x+20,y),(x+100,y),(x+20,y+70),(x+100,y+70),(x+65,y+32)]
    return lista_radar 


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
            mouseMove(Location(213, 210))
            wait(0.5)
            try:
                REG_RELOG.click(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG))
            except:
                pass
            mouseMove(Location(213, 213))
            wait(10)
            if REG_RELOG.exists(Pattern(IMG_RELOG).similar(SIM_IMG_RELOG)):
                pass
            else:
                relogged = True
        BUSY = False
        mouseMove(REG_SEA.getCenter())


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
        mouseMove(Location(263,33))
        wait(2)
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
    check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=6000)
    coord = calculacoord_radar()
    CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=10)
    while finished == False:
        if datetime.datetime.now() > check_revive_timeout:
            check_revive()
            check_revive_timeout = datetime.datetime.now() + datetime.timedelta(seconds=8)
        if datetime.datetime.now() > check_update_timeout:
            check_update()
            check_update_timeout = datetime.datetime.now() + datetime.timedelta(seconds=600)
        if BUSY == False:
            if datetime.datetime.now() > CHECK_MOVE_TIMEOUT:
                move(coord)
                CHECK_MOVE_TIMEOUT = datetime.datetime.now() + datetime.timedelta(seconds=20)
        check_repair()
        if LOW_HP == True:
            repair()
        if datetime.datetime.now() > finish_at:
            finished = True
    REG_SEA.stopObserver()
    run("cmd /C shutdown /s")

#configure(5)
main()