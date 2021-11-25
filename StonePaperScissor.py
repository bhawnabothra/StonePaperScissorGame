from tkinter import *
from PIL import Image, ImageTk
from random import randint

root=Tk()
root.geometry("700x400")
root.minsize(700,400)
root.maxsize(700,400)
root.title("STONE PAPER SCISSOR")
root.configure(background="#00cccc")

#IMAGE
stone_user=ImageTk.PhotoImage(Image.open("stone_user.png").resize((120,120)))
paper_user=ImageTk.PhotoImage(Image.open("paper_user.png").resize((120,120)))
scissor_user=ImageTk.PhotoImage(Image.open("scissor_user.png").resize((120,120)))
stone_comp=ImageTk.PhotoImage(Image.open("stone_comp.png").resize((120,120)))
paper_comp=ImageTk.PhotoImage(Image.open("paper_comp.png").resize((120,120)))
scissor_comp=ImageTk.PhotoImage(Image.open("scissor_user.png").resize((120,120)))

#IMAGE INSERT
label_user=Label(root,image=stone_user)
label_comp=Label(root,image=stone_comp)
label_comp.grid(row=3,column=1)
label_user.grid(row=3,column=6)

#SCORE
user_score=Label(root, text="0", font="YuGothicUISemibold 20 ", bg="#00cccc", fg="white")
computer_score=Label(root, text="0", font="YuGothicUISemibold 20 ", bg="#00cccc", fg="white")
computer_score.grid(row=3,column=2)
user_score.grid(row=3, column=4)

#INDICATOR
Label(root, font="YuGothicUISemibold 12 ", text="USER", bg="#b0e0e6", fg="black",relief=GROOVE).grid(row=4,column=6)
Label(root, font="YuGothicUISemibold 12 ", text="COMPUTER", bg="#b0e0e6", fg="black",relief=GROOVE).grid(row=4,column=1)
Label(root, font="YuGothicUISemibold 25 ", text="SCORE", bg="#b0e0e6", fg="black",relief=SUNKEN).grid(row=2,column=3)

#MESSAGE
msg=Label(root, text="",font="YuGothicUISemibold 15 ", fg="white",bg="#00cccc")
msg.grid(row=3,column=3)

#update_message
def updatemessage(y):
    msg['text']=y

#update User Score
def updateUserScore():
    user_score["text"] = str(int(user_score["text"])+1)

#update Computer Score
def updateComputerScore():
    computer_score["text"] = str(int(computer_score["text"])+1)

#check winner
def winnerchecking(user,computer):
        if user == computer:
            updatemessage("Its a tie!!!")
        elif user == "stone":
            if computer == "paper":
                updatemessage("You loose")
                updateComputerScore()
            else:
                updatemessage("You Win")
                updateUserScore()
        elif user == "paper":
            if computer == "scissor":
                updatemessage("You loose")
                updateComputerScore()
            else:
                updatemessage("You Win")
                updateUserScore()
        elif user == "scissor":
            if computer == "stone":
                updatemessage("You loose")
                updateComputerScore()
            else:
                updatemessage("You Win")
                updateUserScore()
        else:
            pass

#choice
choices=["stone","paper","scissor"]

def choiceupdate(y):
    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "stone":
        label_comp.configure(image=stone_comp)
    elif compChoice == "paper":
        label_comp.configure(image=paper_comp)
    else:
        label_comp.configure(image=scissor_comp)

    # for user
    if y == "stone":
        label_user.configure(image=stone_user)
    elif y == "paper":
        label_user.configure(image=paper_user)
    else:
        label_user.configure(image=scissor_user)

    winnerchecking(y, compChoice)

#BUTTONS
stone = Button(root, width=20, height=2, text="STONE", bg="#f49ac2", fg="black",command=lambda: choiceupdate("stone"),relief=RIDGE).grid(row=6,column=2)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FFFF00", fg="black",command=lambda: choiceupdate("paper"),relief=RIDGE).grid(row=6,column=3)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#CD5C5C", fg="black",command=lambda: choiceupdate("scissor"),relief=RIDGE).grid(row=6,column=4)

root.mainloop()