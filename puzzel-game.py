import random
import tkinter
from tkinter import *
from tkinter import messagebox
import math
import queue
import numpy as np

take =5
size = take*take


SOLUTION = [str(x) for x in range(1,size)]
SOLUTION.append('-')
# SOLUTION = '12345678-'
# SOLUTION=('1','2','3','4','5','6','7','8','-')

# SOLUTION = ['1','2','3','4','5','6','7','8','-']

def correctPosition():
    global size
    global SOLUTION
    m={}
    c=-1
    for idx , val in enumerate(SOLUTION[:-1]):
        if (idx % take == 0) :
            c = c+1
        m[val] = (c,idx % take)
        
    return m
correct_position = correctPosition()

if take ==3 :
    valid_moves = {
        0:  [1, 3],         # 0
        1:  [0, 2, 4],      # 1
        2:  [1, 5],         # 2
        3:  [0, 4, 6],      # 3
        4:  [1, 3, 5, 7],   # 4
        5:  [2, 4, 8],      # 5
        6:  [3, 7],         # 6
        7:  [4, 6, 8],      # 7
        8:  [5, 7]          # 8
    }

if take == 4:
    valid_moves = {
        0:  [1, 4],         # 0
        1:  [0, 2, 5],      # 1
        2:  [1, 3, 6],         # 2
        3:  [2, 7],      # 3
        4:  [0, 8, 5],   # 4
        5:  [1, 4, 6, 9],      # 5
        6:  [2, 5, 7, 10],         # 6
        7:  [3, 11, 6],      # 7
        8:  [4, 12, 9],          # 8  
        9:  [5, 8, 10, 13],
        10: [6, 9, 11, 14],
        11: [7 , 10 , 15],
        12: [8, 13],
        13: [12,14, 9],
        14: [10, 13, 15],
        15: [11, 14]
    }
if take==5:
    valid_moves = {
        0:  [1,5],
        1:  [0,2,6],
        2:  [1,3,7],
        3:  [2,4,8],
        4:  [3,9],
        5:  [0,6,10],
        6:  [5,1,7,11],
        7:  [6,2,8,12],
        8:  [3,7,9,13],
        9:  [4,8,14],
        10: [5,11,15],
        11: [6,12,16,10],
        12: [7,13,17,11],
        13: [8,14,18,12],
        14: [9,13,19],
        15: [10,16,20],
        16: [11,17,21,15],
        17: [12,18,22,16],
        18: [13,19,23,17],
        19: [14,18,24],
        20: [15,21],
        21: [16,22,20],
        22: [17,23,22],
        23: [18,24,22],
        24: [19,23]
    }


def number_of_tiles_out_of_place(state_of_puzzle: str) -> int:
    return sum(
        char != str(solution_state) and (solution_state != size or char != '-')
        for solution_state, char in enumerate(state_of_puzzle, start=1)
    )

def number_of_tiles_implace(state_of_puzzle: str) -> int:
    pass

def manhattan_distance(state_of_puzzle: str) -> int:
    final = 0
    for i in range(size):
        char_in_question = state_of_puzzle_gui[i]
        if (char_in_question == '-'):
            continue
        final = final + abs(i % take - correct_position[char_in_question][0]) + abs(
            int(i/take) - correct_position[char_in_question][1])
        # final = final + abs(i % 3 - ((int(i) - 1) % 3)) + abs(
        #     int(i/3) - int((int(i) - 1) / 3))
    return final

def euclidean_distance (state_of_puzzle: str) -> float:
    pass

def best_first_search(state_of_puzzle, heuristic: str) -> list[str]:
    q = queue.PriorityQueue()
    # state_of_puzzle=''.join(state_of_puzzle)
    s = state_of_puzzle.copy()
    state_of_puzzle.append(str(state_of_puzzle.index('-'))) 
    li=[]
    li.append(str(state_of_puzzle.index('-')))
    li = li +(state_of_puzzle)
    q.put((heuristic(state_of_puzzle), li))
    # q.put((heuristic(state_of_puzzle), str(state_of_puzzle.find('-')) + state_of_puzzle))
    state_of_puzzle=tuple(state_of_puzzle)
    states = {state_of_puzzle: None}
    k = SOLUTION.copy()
    k = ''.join(SOLUTION)
    k= tuple(k)
    while(k not in states.keys()):
        # print("_______________________")
        ################################################################################################################
        state = (q.get()[1])
        # print(state)
        possible_moves = valid_moves[int(state[0])]
        # print(possible_moves)
        for move in possible_moves:
            to_push = puzzle_move(state[1:], move)
            # to_push=''.join(to_push)
            # print(to_push)
            to_push=tuple(to_push)
            if(to_push not in states.keys()):
                # print("ggggggggggggggg")
                states[to_push] = state[1:]
                li2 = []
                li2.append(str(move))
                li2 = li2 + list(to_push)
                print (f'{li2} llllllllllllllllllllllllllllllllllllllll')
                q.put((heuristic(to_push), (li2)))
    final = [k]
    while (states[final[-1]] != None):
        final.append(states[final[-1]])
    final.reverse()
    return final


def random_move(depth: int) -> str:
    final = SOLUTION
    for _ in range(depth):
        final = puzzle_move(final, random.choice(valid_moves[final.index('-')]))
    return final

def puzzle_move(state_of_puzzle: str, pos: int) :
    char_to_move = state_of_puzzle[pos]
    final = []
    for i in state_of_puzzle:
        if (i == "-"):
            final.append(char_to_move)
        elif i == char_to_move:
            final.append("-")
        else:
            final.append(i)
    return final
#################################################################################################################
if (__name__ == "__main__"):
    import tkinter
    import time
    # global variables
    game_window = tkinter.Tk()
    toTime = tkinter.IntVar()   
    heuristic_func = tkinter.IntVar()
    state_of_puzzle_gui = SOLUTION
    previous_scramble = state_of_puzzle_gui
    heuristic_func_to_use = [
        number_of_tiles_out_of_place,
        number_of_tiles_implace,
        manhattan_distance,
        euclidean_distance
    ]

    def move_gui(index: str):
        global state_of_puzzle_gui
        if (buttons[index]['text'] == "-"):
            return
        grid_of_puzzle = np.chararray((take,take))
        index_of_blank = None
        index_of_selected = None
        can_move_x = False
        can_move_y = False
        i = 0
        for x in range(take):
            for y in range(take):
                grid_of_puzzle[x][y] = state_of_puzzle_gui[i]
                if (buttons[i]['text'] == "-"):
                    index_of_blank = [x, y]
                elif (buttons[i]['text'] == buttons[index]['text']):
                    index_of_selected = [x, y]
                i += 1
        same_x = index_of_selected[0] == index_of_blank[0]
        same_y = index_of_selected[1] == index_of_blank[1]
        can_move_x = False
        can_move_y = False
        if (index_of_selected[0] > index_of_blank[0]):
            if ((index_of_selected[0] - 1) == index_of_blank[0]):
                can_move_x = True
        elif ((index_of_selected[0] + 1) == index_of_blank[0]):
            can_move_x = True

        if (index_of_selected[1] > index_of_blank[1]):
            if ((index_of_selected[1] - 1) == index_of_blank[1]):
                can_move_y = True
        elif ((index_of_selected[1] + 1) == index_of_blank[1]):
            can_move_y = True

        if ((can_move_x and same_y) or (same_x and can_move_y)):
            state_of_puzzle_gui = puzzle_move(state_of_puzzle_gui, index)
            set_gui_state_gui(state_of_puzzle_gui)
            
    
    def random_gui():
        global state_of_puzzle_gui
        global previous_scramble
        previous_scramble = state_of_puzzle_gui
        new_state_of_puzzle_gui = random_move(100)
        set_gui_state_gui(new_state_of_puzzle_gui)
        state_of_puzzle_gui = new_state_of_puzzle_gui
        
    def set_gui_state_gui(new_state: str):
        global state_of_puzzle_gui
        for i in range(size):
            buttons[i]['text'] = new_state[i]
        state_of_puzzle_gui = new_state
        game_window.update()

    def solve_gui(func_name):  # sourcery skip: hoist-statement-from-if
        global state_of_puzzle_gui
        global previous_scramble
        global heuristic_func
        global heuristic_func_to_use
        if (state_of_puzzle_gui == SOLUTION):
            return
        previous_scramble = state_of_puzzle_gui
        start_time = None
        end_time = None
        solution_path = None
        if (func_name.__code__.co_argcount == 2):
            to_use = heuristic_func_to_use[heuristic_func.get()]
            start_time = time.perf_counter()
            solution_path = func_name(state_of_puzzle_gui, to_use)
            end_time = time.perf_counter()
        else:
            start_time = time.perf_counter()
            solution_path = func_name(state_of_puzzle_gui)
            end_time = time.perf_counter()
        if (toTime.get()):
            top = tkinter.Toplevel(game_window)
            top.geometry("250x80")
            top.title("Time of Solve")
            tkinter.Label(top, text=str(end_time - start_time)[:6] + " seconds\nusing " + str(len(solution_path) - 1) + " moves", font=('Calibri 18 bold')).place(x=15, y=8)
        sleep_time = 10/len(solution_path)
        for step in solution_path:
            set_gui_state_gui(step)
            time.sleep(sleep_time)

    game_window.title("Puzzel")
    game_window.geometry('640x300+350+200')
    game_window.configure(background="gray16")
    game_window.resizable(width=False, height=False)
        # GUI Menu
    menubar = tkinter.Menu(game_window)
    size_menu = tkinter.Menu(menubar, tearoff=0)
    size_menu.add_radiobutton(label="3x3",variable=take,value=3)
    size_menu.add_radiobutton(label="4x4",variable=take,value=4)
    size_menu.add_radiobutton(label="5x5",variable=take,value=5)
    menubar.add_cascade(label="Size", menu=size_menu)
    game_window.config(menu=menubar)

    heuristic_menu = tkinter.Menu(menubar, tearoff=0)
    heuristic_menu.add_radiobutton(label="number_of_tiles_out_of_place",variable=heuristic_func, value=0)
    heuristic_menu.add_radiobutton(label="number_of_tiles_implace",variable=heuristic_func, value=1)
    heuristic_menu.add_radiobutton(label="manhattan_distance",variable=heuristic_func, value=2)
    heuristic_menu.add_radiobutton(label="euclidean_dastance",variable=heuristic_func, value=3)

    menubar.add_cascade(label="heuristic func", menu=heuristic_menu)
    game_window.config(menu=menubar)

    ###################################################### buttons
    left_frame= Frame(game_window,width=300 , height=300, bd=2, relief=RIDGE)
    left_frame.grid(row=1,column=0)

    right_frame= Frame(game_window,width=300 , height=300, bd=2, relief=RIDGE, bg="gray16" )
    right_frame.grid(row=1,column=1)

    pixel = tkinter.PhotoImage(width=1, height=1)
    buttons = []
    x = 0
    y = 0
    for i in range(0, size):
        if (i == size-1 ):
            buttons.append(tkinter.Button(left_frame, text="-", font=("Calibri 32"), image=pixel, height=300/take-10, width=300/take-10, bg="#AAAAAA", compound="center", command=lambda t=i: move_gui(t)))
        else:
            buttons.append(tkinter.Button(left_frame, text=str(i + 1), font=("Calibri 32"), image=pixel, height=300/take-10, width=300/take-10, bg="#AAAAAA", compound="center", command=lambda t=i: move_gui(t)))
        buttons[-1].place(x=(x % take) * (300/take), y=y * (300/take))
        x = x + 1
        if ((x % take) == 0):
            y = y + 1
    # random_gui()
    time_label = Label(right_frame, font=("calibri", 20,"bold"), text="Time :", bg="gray16",fg="white")
    time_label.grid(row=0 , column=0)

    time_result = Entry(right_frame, font=("calibri", 16,"bold"), bg="white")
    time_result.grid(row= 0, column=1)

    steps_label = Label(right_frame, font=("calibri", 20,"bold"), text="Steps :",bg="gray16",fg="white")
    steps_label.grid(row=1 , column=0)

    steps_result = Entry(right_frame, font=("calibri", 16,"bold"), bg="white")
    steps_result.grid(row= 1, column=1)

    random_button = Button(right_frame, font=("calibri", 18,"bold"),text ="Random", bg="white",width=7, height=1,bd = 5,command=random_gui)
    random_button.grid(row=2, column=0)

    solve_button = Button(right_frame, font=("calibri", 18,"bold"),text ="Solve", bg="white",width=7, height=1,bd =5, command=lambda method_to_use=best_first_search: solve_gui(method_to_use))
    solve_button.grid(row=2, column=1)

    game_window.mainloop()