import random as rand
from string import ascii_lowercase
import time
import os
# print('\u273A')
# print('\u2690')

# MESSAGES
def game_over_message():
    print("""                                                                                     xxxx""")
    time.sleep(0.2)
    print('''XXXXXXX   XXXXXXX   XX   XX   XXXXXXX      XXXXXXX   X     X   XXXXXXX   XXXXXXX     xxxx''')
    time.sleep(0.2)
    print('''X     X   X     X   X X X X   X            X     X   X     X   X         X     X     xxxx''')
    time.sleep(0.2)
    print('''X     X   X     X   X  X  X   X            X     X   X     X   X         X     X     xxxx''')
    time.sleep(0.2)
    print('''X         X     X   X  X  X   XXXXXXX      X     X   X     X   XXXXXXX   XXXXXXX     xxxx ''')
    time.sleep(0.2)
    print('''X   XXX   XXXXXXX   X  X  X   X            X     X    X   X    X         XXX              ''')
    time.sleep(0.2)
    print('''X     X   X     X   X     X   X            X     X     X X     X         X  XX       xxxx ''')
    time.sleep(0.2)
    print('''XXXXXXX   X     X   X     X   XXXXXXX      XXXXXXX      X      XXXXXXX   X    XX     xxxx ''')
    time.sleep(0.2)
    print(" ")
    print(" ")

def win_message():
    print("""                                xxxx """)
    time.sleep(0.2)
    print('''X       X   XXXXXXX   X     X   xxxx ''')
    time.sleep(0.2)
    print('''X       X      X      XX    X   xxxx ''')
    time.sleep(0.2)
    print('''X   X   X      X      X X   X   xxxx ''')
    time.sleep(0.2)
    print('''X  X X  X      X      X  X  X   xxxx ''')
    time.sleep(0.2)
    print('''X X   X X      X      X   X X        ''')
    time.sleep(0.2)
    print('''XX     XX      X      X    XX   xxxx ''')
    time.sleep(0.2)
    print('''X       X   XXXXXXX   X     X   xxxx ''')
    time.sleep(0.2)
    print(" ")
    print(" ")

def welcome_message():
    print(" ")
    print("""                                                                           xxxx""")
    time.sleep(0.1)
    print('''X       X   XXXXXXX   X        XXXXXXX   XXXXXXX   X       X   XXXXXXX     xxxx''')
    time.sleep(0.1)
    print('''X       X   X         X        X         X     X   XX     XX   X           xxxx''')
    time.sleep(0.1)
    print('''X   X   X   X         X        X         X     X   X X   X X   X           xxxx''')
    time.sleep(0.1)
    print('''X  X X  X   XXXXXXX   X        X         X     X   X  X X  X   XXXXXXX     xxxx ''')
    time.sleep(0.1)
    print('''X X   X X   x         X        X         X     X   X   X   X   X                ''')
    time.sleep(0.1)
    print('''XX     XX   X         X        X         X     X   X       X   X           xxxx ''')
    time.sleep(0.1)
    print('''X       X   XXXXXXX   XXXXXXX  XXXXXXX   XXXXXXX   X       X   XXXXXXX     xxxx ''')
    time.sleep(0.1)
    print(" ")
    print(" ")


def setup_map(width,height,x):
    empty_map = [[x for i in range(width)] for i in range(height)]
    return empty_map

def show_map(list,width,height):
    toplabel = '    '
    for i in ascii_lowercase[:width]:
        toplabel = toplabel + i + '   '
    print(toplabel)
    print("   ",end="")
    print("----"*width)
    counter = 1
    for row in list:
        line = " | ".join(row)
        line = line.replace("X","\u273A")
        line = line.replace("P","\u2690")
        if counter<10:
            print(f"{counter} ",end="| ")
            print(line,end="")
            print(" |")
            print("   ",end="")
            print("----"*width)
            counter+=1
        else:
            print(f"{counter}",end="| ")
            print(line,end="")
            print(" |")
            print("   ",end="")
            print("----"*width)
            counter+=1

def add_bomb(list,width,height,bomb_count):
    check_bomb_count = 0
    bombXY = []
    while check_bomb_count!=bomb_count:
        x = rand.randint(0, height-1)   #row
        y = rand.randint(0, width-1)    #col
        if (x,y) not in bombXY:
            bombXY.append((x,y))
            check_bomb_count+=1
        else:
            continue
    for i,j in bombXY:
        list[i][j] = "X" #Bomb
    return list

def add_margin(main_map,width,height):
    margin_main_map = [["0"]*(width+2)]          #first row
    for row in range(height):                    #--store data from 'main_map' to 'margin_main_map'--
        margin_main_map.append(main_map[row])
    margin_main_map.append(["0"]*(width+2))      #last row
    for q in range(1 , len(margin_main_map)-1):
        row = margin_main_map[q]
        new_row = ["0"]                          #1-first index
        for s in row:
            new_row.append(s)                    #2-load other index from 'row' to 'new_row'
        new_row.append("0")                      #3-add last index
        margin_main_map[q] = new_row             #replace 'new_row' with 'row'
    return margin_main_map

def neighbor_bomb(margin_list,main_map,width,height):
        for row in range(1,height+1):
            for col in range(1,width+1):
                cell_list = []
                c22 = margin_list[row][col]         #middle cell in squar 3x3
                if c22 != "X":
                    cell_list.append(margin_list[row-1][col-1]) #c11
                    cell_list.append(margin_list[row-1][col])   #c12 - up
                    cell_list.append(margin_list[row-1][col+1]) #c13

                    cell_list.append(margin_list[row][col-1])   #c21 - left
                    cell_list.append(margin_list[row][col+1])   #c23 - right

                    cell_list.append(margin_list[row+1][col-1]) #c31
                    cell_list.append(margin_list[row+1][col])   #c32 - down
                    cell_list.append(margin_list[row+1][col+1]) #c33
                    main_map[row-1][col-1]=  str(cell_list.count("X"))  #c22 = cell_list.count("X")
        return main_map    #main map made successfully and returned

def select_ground():
    print("________ GROUNDS __________")
    print("|                          ")
    print("| 1> 9x9 - 10 BOMB         ")
    print("| 2> 12x12 - 20 BOMB       ")
    print("| 3> 15x20 - 40 BOMB       ")
    print("|                          ")
    print("| 4> BACK TO MENU          ")
    print("|                          ")
    print("---------------------------")
    n = int(input(" ENTER CODE: "))
    if n==1:
        return (9,9,10)
    elif n==2:
        return (12,12,20)
    elif n==3:
        return (20,15,40)
    else:
        return main_menu()

def save_status():
    global status
    global name
    if status=="won": #win
        f = open(f"{name}.txt","r")
        log = f.readlines()
        f.close()
        psw = log[0]
        log[1] = str(int(log[1])+1) #win count+1
        log[2] = log[2]
        f = open(f"{name}.txt","w")
        f.write(psw)             #write password
        f.write(log[1])          #write win count
        f.write("\n")
        f.write(log[2])          #write lose count
        #f.write("\n")
        f.write("status of last game you played: ! WIN !\n")
        f.write(str(status_time))
        f.write("\n")
        for i in status_map:   #write map to file
            line = " ".join(i)
            f.write(line)
            f.write("\n")
        f.close()

    else: #lose
        f = open(f"{name}.txt","r")
        log = f.readlines()
        # psw = f.readline()
        f.close()
        f = open(f"{name}.txt","w")
        psw = log[0]
        log[2] = str(int(log[2])+1)
        log[1] = log[1]
        f.write(psw)
        f.write(log[1])
        f.write(log[2])
        f.write("\n")
        f.write("status of last game you played: ! LOSE ! \n")
        for i in status_map:
            line = " ".join(i)
            f.write(line)
            f.write("\n")
        f.close()

#########################

def play_game():
    global status
    os.system('cls||clear')
    (width,height,bomb_count) = select_ground()                        #1-select ground
    os.system('cls||clear')
    
    main_map = []
    empty_map = setup_map(width,height,"0")                            #2-make empty map
    main_map = add_bomb(empty_map,width,height,bomb_count)             #3-add bomb + empty map ->main map
    margin_main_map = add_margin(main_map,width,height)                #4-add margin for calculate neighbor correctly         
    admin_map = neighbor_bomb(margin_main_map,main_map,width,height)   #5-calculate neghbor bomb for each cell
    global status_map
    status_map = main_map            #for saving map to file
    f = open("admin_map.txt","w")    #----write 'admin_map' to 'admin_map.txt'----
    for row in admin_map:
        for indx in row:
            f.write(indx)
        f.write("\n")
    f.close()
    user_map = setup_map(width,height," ")   #make a empty map for input from user
    ######
    def check_inputs(inputs):  #chect correction of inputs (a 1 L)
        check = True
        abc = []
        for i in ascii_lowercase[:width]:
                abc.append(i)
        if len(inputs)!=3:     #less or more input
                check = False
        elif len(inputs)==3:
            if inputs[2]!="L" and inputs[2]!="R":
                check = False
            elif int(inputs[1])<0 or int(inputs[1])>height or inputs[0] not in abc:
                check = False

        return check
    #####
    total_Bomb = int(bomb_count)
    flags = 0
    start = time.time()
    min = 0
    TrueFlag = 0
    while True: #while break --when--> user win || user lost
        ################# TIME ######################
        total_time = int(width)*int(height)*5    #calculate tottal time
        game_time = int(time.time() - start)     #calculate user played time
        time_left = total_time - game_time       #calculat time left

        total_min = total_time//60
        total_sec = total_time%60

        min = 0
        second = 0
        min+=time_left//60
        second += time_left%60

        #----check time over----
        if time_left<=0: 
            game_over_message()
            print(" ")
            # print("------------- GAME OVER !-------------")
            print("-----------  TIME RAN OUT! ----------")
            print(" ")
            status = "lose"
            status_map = admin_map
            show_map(admin_map,width,height)
            end_game()
        
        #---check win with 'TrueFalg'=='total_Bomb'----
        if TrueFlag==total_Bomb:    
            show_map(admin_map,width,height)
            print(" ")
            print("---------- WELL DONE!! ----------")
            print(" ")
            print("----------- YOU WON!!! -----------")
            status = "won"        #for write in file (line 4 = last plat status)
            global status_time    #for write in file
            status_time=game_time
            myf = open("time.txt","w")
            myf.write(str(status_time))
            myf.close()
            print(" ")
            win_message()
            print(" ")
            time.sleep(3)
            end_game()
            break
        #---game run----
        show_map(user_map,width,height)    #show user map
        print(" ")
        hint_massage = "-----(example: 'a 1 L' -> click  |  'a 1 R' -> Flag  | enter 'exit' for quit)-----"
        print(hint_massage)
        print(" ")
        flag_left = total_Bomb - flags

        #-------show time---------
        if total_sec<10:
            if second<10:
                print(f" >TIME LEFT: {min}:0{second} / {total_min}:0{total_sec}")
            else:
                print(f" >TIME LEFT: {min}:{second} / {total_min}:0{total_sec}")
        else:
            if second<10:
                print(f" >TIME LEFT: {min}:0{second} / {total_min}:{total_sec}")
            else:
                print(f" >TIME LEFT: {min}:{second} / {total_min}:{total_sec}")
        #--------------------------
        print(f" >FLAGS LEFT: {flag_left} / {total_Bomb}")
        print(" ")
        inputs = input(f" ENTER YOUR MOVE: ")
        #check user want exit?
        if inputs=="exit":
            inp = input("you sure you want to quit? ('yes' or 'no') :")
            if inp=="yes":
                return main_menu()
            else:
                continue
        #user input 
        inputs = inputs.split()
        check = check_inputs(inputs)

        if check==False: #invalid input
            print("invalid inputs! please enter your move again!")
            time.sleep(1)
            os.system('cls||clear')
            continue

        else:
            abc = []
            for i in ascii_lowercase[:width]:
                abc.append(i)
            user_y = inputs[0]         #1234...
            user_x = int(inputs[1])    #abcd...
            user_y = int(abc.index(user_y) +1)  #convert 'abc..' to '1234...'

            # ---if move = Flag---
            if inputs[2]=="R":
                if user_map[user_x-1][user_y-1] == "P": #cell alreday Flag
                    user_map[user_x-1][user_y-1] = " "
                    flags-=1
                    os.system('cls||clear')
                    continue
                else:
                    flags+=1
                    user_map[user_x-1][user_y-1] = "P"  #cell not already a Flag
                    if admin_map[user_x-1][user_y-1] == "X": #if correct detection,TrueFlag+1
                        TrueFlag+=1
                    os.system('cls||clear')

            #----move is not flag-----
            else:
                if admin_map[user_x-1][user_y-1] == "X":      #GAME OVER
                    user_map[user_x-1][user_y-1] = "X"
                    os.system('cls||clear')
                    print(" ")
                    print("----------- Game Over! -----------")
                    print(" ")
                    game_over_message()
                    time.sleep(5)
                    show_map(admin_map,width,height)
                    print(" ")
                    print("  ")
                    status = "lose"
                    status_map = admin_map
                    end_game()
                    break
                #this cell is '0' in admin map
                elif admin_map[user_x-1][user_y-1]=="0":
                    u_x_idx = user_x-1
                    u_y_idx = user_y-1
                    def zero_neighbor(xx,yy):
                        if 0<=(xx-1)<=height-1 and 0<=(yy-1)<=width-1: #check is in margin || no offside!
                            user_map[xx-1][yy-1] = admin_map[xx-1][yy-1]

                        if 0<=(xx-1)<=height-1 and 0<=(yy)<=width-1:
                            user_map[xx-1][yy] = admin_map[xx-1][yy]

                        if 0<=(xx-1)<=height-1 and 0<=(yy+1)<=width-1:
                            user_map[xx-1][yy+1] = admin_map[xx-1][yy+1]

                        if 0<=(xx)<=height-1 and 0<=(yy-1)<=width-1:
                            user_map[xx][yy-1] = admin_map[xx][yy-1]

                        if 0<=(xx)<=height-1 and 0<=(yy)<=width-1:
                            user_map[xx][yy] = admin_map[xx][yy]

                        if 0<=(xx)<=height-1 and 0<=(yy+1)<=width-1:
                            user_map[xx][yy+1] = admin_map[xx][yy+1]

                        if 0<=(xx+1)<=height-1 and 0<=(yy-1)<=width-1:
                            user_map[xx+1][yy-1] = admin_map[xx+1][yy-1]

                        if 0<=(xx+1)<=height-1 and 0<=(yy)<=width-1:
                            user_map[xx+1][yy] = admin_map[xx+1][yy]

                        if 0<=(xx+1)<=height-1 and 0<=(yy+1)<=width-1:
                            user_map[xx+1][yy+1] = admin_map[xx+1][yy+1]

                    zero_neighbor(user_x-1,user_y-1)

                    for i in range(-1,2):
                        for j in range(-1,2):
                            if 0<=u_x_idx+i<=height-1 and 0<=u_y_idx+j<=width-1:
                                if admin_map[u_x_idx+i][u_y_idx+j]=="0":  #in neighbor somebody is '0'
                                    zero_neighbor(u_x_idx+i,u_y_idx+j)    #ok! we do it again with this cell !

                                    for ii in range(-1,2):
                                        for jj in range(-1,2):
                                            if 0<=u_x_idx+i+ii<=height-1 and 0<=u_y_idx+j+jj<=width-1:
                                                if admin_map[u_x_idx+i+ii][u_y_idx+j+jj]=="0":
                                                    zero_neighbor(u_x_idx+i+ii,u_y_idx+j+jj)

                                                    for iii in range(-1,2):
                                                        for jjj in range(-1,2):
                                                            if 0<=u_x_idx+i+ii+iii<=height-1 and 0<=u_y_idx+j+jj+jjj<=width-1:
                                                                if admin_map[u_x_idx+i+ii+iii][u_y_idx+j+jj+jjj]=="0":
                                                                    zero_neighbor(u_x_idx+i+ii+iii,u_y_idx+j+jj+jjj)


                        os.system('cls||clear')
                        continue #go to first of while loop
                    else:
                        user_map[user_x-1][user_y-1] = admin_map[user_x-1][user_y-1]
                        os.system('cls||clear')
                        continue #go to first of while loop
                
                #this cell is a number like 1,2,3... in admin map
                elif admin_map[user_x-1][user_y-1] != "0":
                    user_map[user_x-1][user_y-1] = admin_map[user_x-1][user_y-1]
                    os.system('cls||clear')
                    continue  #go to first of while loop

#########################

def exit_game():
    print("------THANKS FOR YOUR PLAYING !------")
    print("")
    print("-----------SEE YOU LATER !----------")
    time.sleep(4)
    os.system('cls||clear')
    exit()

def end_game():#after playing a game
    save_status() #at first save data
    print(" ")
    print(" 1> REMATCH") #->select ground
    print(" 2> MAIN MENU")
    print(" 3> EXIT")
    print(" ")
    code = input("ENTER CODE: ")
    os.system('cls||clear')
    if code!="1" and code!="2" and code!="3":
        print("INVALID CODE!")
        return end_game()
    if code=="1":
        return select_ground()
    elif code=="2":
        return main_menu()
    elif code=="3":
        return exit_game()

def start_menu():#1
    os.system('cls||clear')
    welcome_message()
    time.sleep(1)
    os.system('cls||clear')
    print("====="*8)
    print("Loading!")
    for i in range(20):
        print("\u273A",end=" ")
        time.sleep(0.1)
    print(" ")
    os.system('cls||clear')
    print(' ')
    print(" HELLO! WELCOME TO 'MINESWEEPER' GAME !")
    time.sleep(1)
    os.system('cls||clear')
    return account()

def sign_in():#3
    print("__________ SIGN IN __________")
    print(" ")
    username = input(" ENTER YOUR USERNAME: ")
    if os.path.exists(f"{username}.txt"):   #check file exist
        global password
        f = open(f"{username}.txt","r") 
        password = f.readline()             #read password from file
        if "\n" in password:
            password = password[:-1]        #delete \n
        f.close()
        check_pass = input(" ENTER YOUR PASSWORD: ")
        os.system('cls||clear')
        if check_pass==password:
            print(" ")
            print("YOU WRER SIGHNED IN!")
            time.sleep(1)
            os.system('cls||clear')
            global name
            name = username
            return main_menu()
        else:
            print("PASSWORD INCORRECT! ")
            time.sleep(1)
            os.system('cls||clear')
            return sign_in()

    else:
        os.system('cls||clear')
        print("----------SIGN IN----------")
        print("WRONG USER NAME OR YOU DONT HAVE AN ACCOUNT!")
        print(" 1> RETRY")
        print(" 2> Back")
        code = int(input("ENTER CODE: "))
        if code==1:
            os.system('cls||clear')
            return sign_in()
        else:
            os.system('cls||clear')
            return account()

def sign_up():#3 
    global name
    print("__________ SIGN UP __________")
    print(" ")
    username = input("ENTER YOUR USERNAME: ")
    if os.path.exists(f"{username}.txt"):    #if username exist in files,user should enter another username
        os.system('cls||clear')
        print("USER NAME ALREADY TAKEN! CHOOSE ANOTHER ONE!")
        time.sleep(1)
        os.system('cls||clear')
        return sign_up()
    else:
        global password          #set password
        password = input("ENTER PASSWORD: ")
        name = username          #set username
        f = open(f"{username}.txt","w")
        f.write(password)        #write password in file
        f.write("\n")
        f.write("0")             #write won count
        f.write("\n")
        f.write("0")             #write lost count
        f.write("\n")
        f.close()
        os.system('cls||clear')
        print("SIGNING UP HAVE DONE! YOU ARE LOG IN!")
        time.sleep(1)
        os.system('cls||clear')
        return main_menu()

def account(): #2
    print("__________START MENU__________")
    print("|                             ")
    print("| 1> SIGN IN                  ")
    print("|                             ")
    print("| 2> SIGN UP                  ")
    print("|                             ")
    print("|                             ")
    print("------------------------------")
    sign_code = input("| ENTER CODE: ")
    os.system('cls||clear')
    if sign_code!="1" and sign_code!="2": #retry
        print("INVALID CODE! ")
        time.sleep(0.75)
        os.system('cls||clear')
        return account
    if sign_code=="1": #sign in
        sign_in()
    else:              #sign up
        sign_up()


def change_name():
    global name
    os.system('cls||clear')
    print("__________CHANGE NAME__________")
    print(" ")
    current_name = name
    new_name = input("ENTER YOUR NEW NAME! ")

    if os.path.exists(f"{new_name}.txt"):     #check is new name already taken or not
        os.system('cls||clear')
        print("THIS NAME HAS ALREADY TAKEN!")
        print("CHOOSE ANOTHER NAME!")
        time.sleep(2)
        os.system('cls||clear')
        return change_name()
    else:
        os.system('cls||clear')
        name = new_name               #change global name(for id in main menu )
        os.rename(f"{current_name}.txt",f"{new_name}.txt")   #change txt file name with os library
        print("CHANGING NAME HAVE DONE!")
        time.sleep(2)
        os.system('cls||clear')
        return main_menu()

def history():
    global name
    print("_______________ LOG _______________")
    print("")
    if os.path.exists(f"{name}.txt"):
        f = open(f"{name}.txt","r")
        log_list = f.readlines()  #store data from 'txt file' into 'log_list'
        f.close()
        if len(log_list)==3:      #history is empty | no play! | user have password,lose=0,win=0
            print("WINS: 0")
            print(" ")
            print("LOSES: 0")
            print(" ")
            print("NO RECORD ! LOG IS EMPTY !")
            print("")
            code = input("ENTER ANY NUMBER FOR BACK TO MAIN MENU: ")
            os.system('cls||clear')
            return main_menu()
        else:                     #histary have much more than pass,lose,win ->last play status, last map ,time(if won)
            line = log_list[3]    #status of last play
            line = line.split(" ")
            check_status = line[-2]         #chack status == win || == lose
            if len(log_list) > 3 and check_status=="WIN":   #---------win state----------#
                print(f"wins: {log_list[1]}")       #win count
                print(f"loses: {log_list[2]}")      #lose count
                print(log_list[3])
                log_time = int(log_list[4])
                log_min = log_time//60
                log_sec = log_time%60
                if log_sec<10:
                    print(f" TIME : {log_min}:0{log_sec}")
                else:
                    print(f" TIME : {log_min}:{log_sec}")

                mylist = []  #last play map without table
                for i in log_list[5:]: #skip-> 1-pass ,2-win count ,3-lose count ,4-last play status ,5-time
                    i = i[:-1]         #delete \n
                    line = i.split()
                    mylist.append(line)

                print("")
                show_map(mylist,len(mylist[0]),0)  #show last paly map in a nice table!
                print(" ")
                code = input("ENTER ANY NUMBER FOR BACK TO MAIN MENU: ")
                os.system('cls||clear')
                return main_menu()

            elif len(log_list) > 3:     #-----------losing state------------#
                print(f"wins: {log_list[1]}")   #win count
                print(f"loses: {log_list[2]}")  #lose count
                print(log_list[3])              #status of last play
                mylist = []                     #last play map without table
                for i in log_list[4:]:
                    i = i[:-1]
                    line = i.split()
                    mylist.append(line)
                print("")
                show_map(mylist,len(mylist[0]),0)   #show last paly map in a nice table!
                print(" ")
                code = input("ENTER ANY NUMBER FOR BACK TO MAIN MENU: ")
                os.system('cls||clear')
                return main_menu()

def change_psw():
    os.system('cls||clear')
    print("__________ CHANGE PASSWORD___________")
    print(" ")
    global password
    check_psw = input("ENTER YOUR CURRENT PASSWORD: ")
    if (check_psw == password):    #correct
        new_psw = input("ENTER NEW PASSWORD: ")
        password = new_psw
        global name
        f = open(f"{name}.txt","r")
        data = f.readlines()       #read all data of txt file and store in 'data'
        f.close()
        data[0] = password + "\n"  #data[0] = line 0 = password of user
        f = open(f"{name}.txt","w")
        for i in range(len(data)):
            f.write(data[i])       #rewrite data from 'data' to txt file
        f.close()
        print("CHANGING PASSWORD HAVE DONE! ")
        time.sleep(2)
        return main_menu()

    else:             #not correct
        print("PASSWORD IS INCORRECT!")
        print(" ")
        print(" 1> RETRY")
        print(" 2> BACK TO MENU ")
        print(" ")
        code = input("ENTER CODE: ")
        if code=="1":
            return change_psw()
        elif code=="2":
            return main_menu()

def credit():
    print(" ")
    print("_____________________________________________________")
    print(" ")
    print(" ----- CREATED BY: MOHAMMAD MAHDI AZARBAYEJANI -----")
    print("_____________________________________________________")
    print(" ")
    c = input("ENTER ANY KEY FOR BACK TO MENU: ")
    return main_menu()

def main_menu():#4
    os.system('cls||clear')
    global name
    print("___________MAIN MENU____________")
    print("| =============",end="")
    print("="*len(name))
    print("| ",end="")
    print(f"= your id: {name}",end="")
    print(" =")
    print("| =============",end="")
    print("="*len(name))
    print("|                              ")
    print("| 1> PLAY!                     ")
    print("| 2> CHANGE NAME               ")
    print("| 3> CHANGE password           ")
    print("| 4> HISTORY                   ")
    print("| 5> Log out                   ")
    print("| 6> GAME CREDIT               ")
    print("| 7> EXIT                      ")
    print("|                              ")
    print("")
    check_code = False
    while check_code==False:
        menu_code = int(input(" ENTER CODE: "))
        if menu_code!=1 and menu_code!=2 and menu_code!=3 and menu_code!=4 and menu_code!=5 and menu_code!=6 and menu_code!=7:
            os.system('cls||clear')
            print(" INVALID CODE! ")
            continue
        else:
            break
    os.system('cls||clear')
    if menu_code==1:
        play_game()
    elif menu_code==2:
        change_name()
    elif menu_code==3:
        change_psw()
    elif menu_code==4:
        history()
    elif menu_code==5:
        return start_menu()
    elif menu_code==6:
        return credit()
    else:
        return exit_game()

name=""            #for id in main_menu 
status = ""        #win - lose
status_map = []    #for save in map
status_time = 0    #for save in file
password=""        #check password when changing password
start_menu()