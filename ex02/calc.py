import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tk.END.insert(0)
    #tkm.showinfo("",f"{num}ボタンがクリックされました")
def button_numclick(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END,num)
def equal_click(event):
    eqn=entry.get()
    resp = eval(eqn)
    entry.delete(0,tk.END)    
    entry.insert(tk.END,resp)
#ウィンドウ作成
root = tk.Tk()
root.geometry("300x500")
#4
entry = tk.Entry(root,width=10,font=("",40),justify="right")
entry.grid(row=0,column=0,columnspan=3)

#ボタン作成
r,c = 1,0
for num in range(9,-1,-1):
    button = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    button.grid(column = c,row = r)
    button.bind("<1>",button_numclick)
    
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

#+ボタン
button = tk.Button(root,text="+",font=("",30),width=4,height=2)
button.grid(column=1,row=4)
button.bind("<1>",button_numclick)

#=ボタン
button = tk.Button(root,text="=",font=("",30),width=4,height=2)
button.grid(column=2,row=4)
button.bind("<1>",equal_click)

root.mainloop()