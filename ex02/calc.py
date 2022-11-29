import tkinter as tk
import tkinter.messagebox as tkm

def button_click_0(event):
    btn = event.widget
    txt = btn["0"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

#ウィンドウ作成
root = tk.Tk()
root.title("練習問題")
root.geometry("300x500")
root.mainloop()

#ボタン作成
#button = tk.Button(root,text = "押すな",command = button_click)
#button.bind("<1>",button_click_0)
#button.pack()