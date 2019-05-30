import tkinter as tk
import math

# ボタンを押したときの処理
def calc_paper():
    # 計算
    h = int(textHeight.get())
    p=0
    n=0
    while p <= h:
        n+=1
        p=math.floor(0.00008*2**n)
    # 結果をラベルに表示
    s = "紙を"+str(n)+"回折れば超えられる高さです（"+str(p)+"ｍ）"
    labelResult['text'] = s

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("origami")
win.geometry("400x200")

# 部品を作成 --- (*3)
labelHeight = tk.Label(win, text=u'なんメートル？')
labelHeight.pack()

textHeight = tk.Entry(win)
textHeight.pack()

labelResult = tk.Label(win, text=u'---')
labelResult.pack()

calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_paper
calcButton.pack()

# ウィンドウを動かす
win.mainloop()
