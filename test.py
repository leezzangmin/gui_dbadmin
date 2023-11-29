from tkinter import *


def calc_text_json_explain():
    print(len(text1.get("1.0",END))-1)

def listcmd():
    print(listbox.size())
    print(listbox.get(0))

root = Tk()
root.title("zzangmin dbadmin")
root.geometry("640x640+300+300")
#root.resizable(False,False)

label1= Label(root, text="label 테스트")
label1.pack()

button1 = Button(root,text="1번")
button1.pack()

button2 = Button(root,text="2번", padx=5, pady=30)
button2.pack()



button3 = Button(root,text="query_cost", width=10, height=10, command=calc_text_json_explain)
button3.pack()

text1 = Text(root, width=10, height=10)
text1.pack()
text1.insert(END, "input text label")


e=Entry(root, width=10)
e.pack()
e.insert(0,"asdf")


listbox= Listbox(root, selectmode="extended", height=0) # selectmode single, height 0은 모두
listbox.insert(END,"사과")
listbox.insert(END,"포도")
listbox.pack()

root.mainloop()