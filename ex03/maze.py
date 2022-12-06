import tkinter as tk

#練習8
import maze_maker as mm

#練習5
def key_down(event):
    global key
    key = event.keysym

#練習6
def key_up(event):
    global key
    key = ""

#練習7
def main_proc():
    global cx, cy
    if key == "Up": cy -= 20
    if key == "Down": cy += 20
    if key == "Left": cx -= 20
    if key == "Right": cx += 20
    #練習11
    global mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    #練習12
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1        
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

#goal時の演出
def goal_f():
    global mx , my , ome_x, ome_y
    if mx == 13 and my == 7:
        ome_x , ome_y = 700,500
        ome = tk.PhotoImage(file="fig/ome.png")
        canvas.create_image(ome_x,ome_y,image=ome)
        root.after_cancel(100, goal_f)


#練習1
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    #練習2
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    #練習9
    maze_lst = mm.make_maze(15,9)
    #練習10
    mm.show_maze(canvas, maze_lst)

    #練習3
    cx, cy = 300, 400
    #練習12
    mx,my = 1,1
    cx,cy = mx*100+50,my*100+50
    tori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")

    #startの座標と表示
    start_x , start_y = 150,50
    start = tk.PhotoImage(file="fig/start.png")
    canvas.create_image(start_x,start_y,image=start)
    #goalの座標と表示
    goal_x , goal_y = 1350,850
    goal = tk.PhotoImage(file="fig/goal.png")
    canvas.create_image(goal_x,goal_y,image=goal)
    
    canvas.pack()   
    #練習4
    key = ""
    #練習5
    root.bind("<KeyPress>", key_down)
    #練習6
    root.bind("<KeyRelease>", key_up)
    #練習7
    main_proc()
    goal_f()

    root.mainloop()