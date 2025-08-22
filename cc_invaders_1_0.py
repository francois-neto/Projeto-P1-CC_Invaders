import sys
import os
import random
import time
import curses

title_cc = [ 
    "    ▓■■■■■▓|      ▓■■■■■▓|  ",
    "  ▓▓|      ▓▓|  ▓▓|      ▓▓|",
    " ▓▓|           ▓▓|          ",
    "■▓▓|          ■▓▓|          ",
    " ▓▓|           ▓▓|          ",
    "  ▓▓|      ▓▓|  ▓▓|      ▓▓|",
    "    ▓■■■■■▓|      ▓■■■■■▓|  "]

title_invaders = [
    " █■■■■█| ██|          ██| █■■█|     █■■█|  ██████████|  █████████|   ■████████| ██████████|    ██████████■  ",
    "   ██|   ██■█|        ██|  ██|       ██|   ██|     ██|  ██|     ███| ██|        ██|      ██|  ██|           ",
    "   ▓▓|   ▓▓|  ██|     ▓▓|   ▓▓|     ▓▓|    ▓▓|     ▓▓|  ▓▓|      ▓▓| ▓▓|        ▓▓|      ▓▓|  ▓▓|           ",
    "   ██|   ██|    ██|   ██|   ██|     ██|    ██■■■■■■██|  ██|       █| ███████|   ██■■■■■■██|   ████████████| ",
    "   ▓▓|   ▓▓|      ██| ▓▓|    ▓▓|   ▓▓|     ▓▓|     ▓▓|  ▓▓|      ▓▓| ▓▓|        ▓▓|      ▓▓|            ▓▓| ",
    "   ██|   ██|        █■██|      █| █|       ██|     ██|  ██|     ███| ██|        ██|      ██|            ██| ",
    " █■■■■█| ██|          ██|       ██|       █■■█|   █■■█| █████████|   ■████████| ██|      ██|  ■██████████|  ",
    " .......................................................................................................... "]

dalton = [
    "                         :%@@@@@@@@@@@@@@@@@@@@@@#-                     ",
    "                    :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-                ",
    "                 :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-            ", 
    "               :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-          ",
    "             -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:       ",
    "           .%@@@@@@@@@@@@@@#%%#*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=      ",
    "           #@@@@@@@@%+==-:.       .=*@@@@@@%%@@@@@@@@@@@@@@@@@@@@%      ",
    "          -@@@@@@@@+:.                .:--.  ..-+#%%%@@@@@@@@@@@@@#.    ",  
    "          %@@@@@@@+:                               ..:-+#%@@@@@@@@@%.   ",    
    "         *@@@@@@@#-                                    :+#@@@@@@@@@@*   ",    
    "        -@@@@@@@@+:                                     +#@@@@@@@@@@@-  ",    
    "        #@@@@@@@#-.                                     -+%@@@@@@@@@@%  ",    
    "        #@@@@@@%+==-                                   .:=%@@@@@@@@@@@. ",    
    "       .%@@@@@@#*%@@%######+-:             .:...   ..:=-:-+%@@@@@@@@@@- ",    
    "        %@@@@@@#@@#+-:::::-+**-           -#####*=+###@@#++#@@@@@@@@@@- ",     
    "        :=%@@@@%%*==*#*##+=  ..:.        .:==:   ..  .-#%##%@@@@@@@@@@: ",    
    "          =@@@@@*=-+#*=-=::   .=*-   :--..=#++*-*#@#=.  :+#@@@@@@@@@@@. ",     
    "          :@@@%@+.            :*#.   #*       ..:-=**+=-=#@@@@@@@@@@@+  ",     
    "           *@@%*=.            *@:    +%-             :*==*%@@@@@@-.++   ",     
    "           .=@#==:°......   :+*=     :==.   ........°:..=#@@@@*-. :+    ",
    "            :@%+:           ==-        .:               -%@@@=  :*+     ",
    "            -@%+:           .-++...-:   .               -%@@# .:#-      ",
    "           :+@%+:              .::..                   .+@@@+ .++       ",
    "             =@*.                                      -%@@@*:+@:       ",
    "              @%-.       -**-:  ____  :...             =@@@@@==.        ",
    "             :#@#+-       :==-.______:==--.           :%@@@@=           ",
    "          -*@@@@@@#+.                                -%@@@@*            ",
    " ----:-=+#@@@@@@@@@@%=.                            -#@@@@@*             ",
    ".@@@@@@@@@@@@@@@@@@@@@%=.                    .:--+%@@##@@#              ",
    ".@@@@@@@@@@@@@@@@#%@@@@@%*:              .-*#%%%@@%+=+%@@*              ",
    ".@@@@@@@@@@@@@@@%-.=%@@@@@@#*+-::...::-+#@@@@%##*=::-+%@@@%-:           ",
    ".@@@@@@@@@@@@@@@#.   -*%@@@@@@@##***##%@@@@%*+-:    .-#@@@@@@+.         ",
    ".@@@@@@@@@@@@@@@+       :=+*%%@%#*++**###*=-.        .#@@@@@@@@#+:.     "]

fala_dalton = [
    "██████████████████████████████████████████████████",
    "██                                              ██",
    "██         OLÁ, ESTUDANTE DE COMPUTAÇÃ0!        ██",
    "██ PRECISO DA  SUA AJUDA PARA EVITAR QUE ALGUNS ██",
    "██ BUGS DERRUBEM A CLOUD DO NOSSO CURSO E APA - ██",
    "██ GUEM NOSSOS DIRETÓRIOS. ACABE COM ELES LOGO! ██",
    "██   USE 'S' PARA DISPARAR E <- -> PARA MOVER!  ██",
    "██                                              ██",
    "██████████████████████████████████████████████████"]

game_over = [
    "   ████████|   ██████████|  ██          ██   ■████████| ",
    "  ██|     ██|  ██|     ██|  ██■█      █■██   ██|        ",
    " ▓▓|           ▓▓|     ▓▓|  ▓▓  ██  ██  ▓▓   ▓▓|        ",
    " ██|    █████| ██■■■■■■██|  ██    ██    ██   ███████|   ",
    " ▓▓|      ▓▓|  ▓▓|     ▓▓|  ▓▓          ▓▓   ▓▓|        ",
    "  ██|     ██|  ██|     ██|  ██          ██   ██|        ",
    "   ████████|  █■■█|   █■■█| ██          ██   ■████████| ",
    "                                                        ",
    "   ████████|   █■■█|     █■■█| ■████████| ██████████|   ",
    "  ██|     ██|   ██|       ██|  ██|        ██|      ██|  ",
    " ▓▓|       ▓▓|   ▓▓|     ▓▓|   ▓▓|        ▓▓|      ▓▓|  ",
    " ██|       ██|   ██|     ██|   ███████|   ██■■■■■■██|   ",
    " ▓▓|       ▓▓|    ▓▓|   ▓▓|    ▓▓|        ▓▓|      ▓▓|  ",
    "  ██|     ██|       █| █|      ██|        ██|      ██|  ",
    "   ████████|         ██|       ■████████| ██|      ██|  ",
    " ______________________________________________________ "]

you_won = [
    "        ██■      ■██|   ████████|   ██|        ██|        ",
    "         ██|     ██|   ██|     ██|  ██|        ██|        ",
    "         ▓▓|     ▓▓|  ▓▓|       ▓▓| ▓▓|        ▓▓|        ",
    "         ■████████■   ██|       ██| ██|        ██|        ",
    "             ▓▓|      ▓▓|       ▓▓| ▓▓|        ▓▓|        ",
    "             ██|       ██|     ██|   ██|      ██|         ",
    "             ██|        ████████|     █████████|          ",
    "                                                          ",
    " █■■█|      ██|     █■■█|   ████████|    ██|          ██| ",
    "  ██|       ██|      ██|   ██|     ██|   ██■█|        ██| ",
    "   ▓▓|      ▓▓|      ▓▓|  ▓▓|       ▓▓|  ▓▓|  ██|     ▓▓| ",
    "   ██|      ██|      ██|  ██|       ██|  ██|    ██|   ██| ",
    "    ▓▓|   ▓▓  ▓▓|   ▓▓|   ▓▓|       ▓▓|  ▓▓|      ██| ▓▓| ",
    "      █| █|     █| █|      ██|     ██|   ██|        █■██| ",
    "       ██|       ██|        ████████|    ██|          ██| ",
    " ________________________________________________________ "]

cloud = '█▓■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■■▓█████▓■▓█'
enemy = '╔╚█╝╗'
nave = '■█■▓■█■'

def menu_start(inicio):
    curses.curs_set(0)
    inicio.clear()
    
    altura, largura = inicio.getmaxyx()
    
    y_cc = (altura - len(title_cc) - len(title_invaders) - 7) // 2
    for i in range(len(title_cc)):
        linha_cc = title_cc[i]
        x_cc = (largura // 2) - (len(linha_cc) // 2)
        inicio.addstr(y_cc + i, x_cc, linha_cc)
    
    y_inv = y_cc + len(title_cc) + 2
    for j in range(len(title_invaders)):
        linha_inv = title_invaders[j]
        x_inv = (largura // 2) - (len(linha_inv) // 2)
        inicio.addstr(y_inv + j, x_inv, linha_inv)
    
    start = "-======= PRESS ANY KEY =======-"
    y_start = y_inv + len(title_invaders) + 3
    x_start = (largura // 2) - (len(start) // 2)
    inicio.addstr(y_start, x_start, start)

    by = "by francisco.neto"
    inicio.addstr(altura - 3, largura // 2 - len(by) // 2, by)
    
    inicio.border()
    inicio.refresh()
    inicio.getch()

def dalton_ajuda(intro):
    curses.curs_set(0)
    intro.clear()

    altura, largura = intro.getmaxyx()
    
    y_dalton = (altura - len(dalton)) // 2
    for i in range(len(dalton)):
        linha_dal = dalton[i]
        x_dalton = 1

        if 0 <= y_dalton < altura and 0 <= x_dalton < largura:
            try:
                intro.addstr(y_dalton + i, x_dalton, linha_dal)
            except curses.error:
                pass
    
    y_fala = (altura - len(fala_dalton)) // 2
    for i in range(len(fala_dalton)):
        linha_fala = fala_dalton[i]
        x_fala = int(largura // 1.33) - len(fala_dalton[i]) // 2
        
        intro.addstr(y_fala + i, x_fala, linha_fala)

    intro.border()
    intro.refresh()
    intro.getch()

def bad_end(fim):
    curses.curs_set(0)
    fim.clear()

    altura, largura = fim.getmaxyx()

    y_gameover = (altura - len(game_over)) // 2
    for i in range(len(game_over)):
        linha_go = game_over[i]
        x_gameover = (largura // 2) - (len(linha_go) // 2)
        fim.addstr(y_gameover + i, x_gameover, linha_go)
    
    perdeu_dict = '!DIRETÓRIOS DA VM DESTRUÍDOS!'

    y_dicts, x_dicts = y_gameover + len(game_over) + 2, largura // 2 - len(perdeu_dict) // 2
    fim.addstr(y_dicts, x_dicts, perdeu_dict)

    fim.border()
    fim.refresh()
    fim.getch()

def good_end(fim2):
    curses.curs_set(0)
    fim2.clear()

    altura, largura = fim2.getmaxyx()

    y_youwon = (altura - len(you_won)) // 2
    for i in range(len(you_won)):
        linha_yo = you_won[i]
        x_youwon = (largura // 2) - (len(linha_yo) // 2)
        fim2.addstr(y_youwon + i, x_youwon, linha_yo)

    fim2.border()
    fim2.refresh()
    fim2.getch()

def level_p1(p1):
    curses.curs_set(0)
    p1.keypad(True)
    p1.nodelay(True)
    
    vida = 100

    altura, largura = p1.getmaxyx()
    x_nave, y_nave = (largura // 2) - (len(nave) // 2), altura - 6
    x_cloud, y_cloud = largura // 2 - len(cloud) // 2, altura - 4

    lasers = []
    lasers_enemys = []

    position_enemys = [(2, x) for x in range (x_cloud, largura - x_cloud, 10) ]
    direcao_enemy = 1
    
    while True:
        p1.clear()
        
        barra_vida = f'║ ESTABILIDADE DA CLOUD EM {vida}% ║'
        x_vida, y_vida = largura // 2 - len(barra_vida) // 2, altura - 2

        laser_trajeto = []
        laser_enemy_trajeto = []

        p1.addstr(y_vida, x_vida, barra_vida)
        p1.addstr(y_cloud, x_cloud, cloud)
        p1.addstr(y_nave, x_nave, nave)

        if not position_enemys:
            p1.nodelay(False)
            good_end(p1)
            return
        for y_enemy, x_enemy in position_enemys:
            p1.addstr(y_enemy, x_enemy, enemy)
            if random.random() < 0.042:
                laser_enemy_trajeto.append((y_enemy + 1, x_enemy + 1))
        lasers_enemys += laser_enemy_trajeto
        
        for i in range(len(position_enemys)):
            y, x = position_enemys[i]
            position_enemys[i] = (y, x + direcao_enemy)

        if (x >= largura - len(enemy) - 2 and direcao_enemy == 1) or position_enemys[0][1] <= 1 :
            direcao_enemy *= -1    

        tecla = p1.getch()
        if tecla == ord('l'):
            p1.nodelay(False)
            return False
        elif tecla == curses.KEY_RIGHT and x_nave + 8 < largura:
            x_nave += 1
        elif tecla == curses.KEY_LEFT and x_nave - 1 > 0:
            x_nave -= 1
        elif tecla == ord('s'):
            x_laser, y_laser = x_nave + len(nave) // 2, y_nave - 1
            lasers.append((y_laser, x_laser))
        
        for y_tiro, x_tiro in lasers_enemys:
            if y_tiro < altura:
                p1.addstr(y_tiro, x_tiro, '■')
                laser_enemy_trajeto.append((y_tiro + 1, x_tiro))
                if y_tiro == y_nave and x_nave <= x_tiro <= x_nave + len(nave):
                    vida -= 0.25
                if y_tiro == y_cloud and x_cloud <= x_tiro <= x_cloud + len(cloud):
                    vida -= 0.5
                if vida <= 0: 
                    p1.nodelay(False)
                    bad_end(p1)
                p1.addstr(y_vida, x_vida, barra_vida)
        lasers_enemys = laser_enemy_trajeto

        for y_tiro, x_tiro in lasers:
            if y_tiro > 0:
                p1.addstr(y_tiro, x_tiro, '║')
                laser_trajeto.append((y_tiro - 1, x_tiro))
        lasers = laser_trajeto

        enemys_restantes = []
        for y_enemy, x_enemy in position_enemys:
            interceptado = False 
            for y_tiro, x_tiro in lasers:
                if y_enemy == y_tiro and x_enemy <= x_tiro <= x_enemy + len(enemy) - 1:
                    interceptado = True
                    break
            if not interceptado:
                enemys_restantes.append((y_enemy, x_enemy))
        position_enemys = enemys_restantes

        p1.refresh()
        time.sleep(0.1)
        
def game(telas):
    menu_start(telas)
    dalton_ajuda(telas)
    level_p1(telas)

curses.wrapper(game)
