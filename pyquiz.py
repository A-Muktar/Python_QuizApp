'''
        \\\\\\\\\\\\\\\\\\\\\\\\
              Coded by:
             TechLead Co. LTD
        \\\\\\\\\\\\\\\\\\\\\\\\
'''

# Importing Tkinter module
from tkinter import *
from tkinter import  messagebox
# Creating master Tkinter window 
master = Tk()
#setting geometry for layout
master.geometry("520x320")
#title for window
master.title("TechLeead Co. Quiz App")
#background of window
master["bg"]="#04112d"
#list for storing  questions
QueList=["What is HTML","Who developed C?","Who developed Python?","When Python is released?","Which of the following is not a keyword?","What is the answer to this expression, 22 % 3 is?"]
#list for storing options
OptList=[["Hypertag markup language", "HyperText MakeUp Language", "HyperText Markup Language", "HyperText Messaging Language"],["Denish Ritchie" ,"Bjarne Stroustrup" ,"James Gosling" ,"Tim Berners Lee"],["Denish Ritchie" ,"Bjarne Stroustrup" ,"James Gosling" ,"Guido van Rossum"],["1992","1991","1990","1994"],["assert","nonlocal","pass","eval"],["5","7","1","0"]]
#list for storing correct output
OutList=["3","1","4","2","4","3"]
#initiaize variable i and result with 0
i=result=0
# Tkinter string variable 
# able to store any string value 
v = StringVar(master, "1")
que=StringVar()
op1=StringVar()
op2=StringVar()
op3=StringVar()
op4=StringVar()
op5=StringVar()

#label for heading
Label(master, width="300", text="Python Quiz Application", bg="dodgerblue", fg="#000000",font='Helvetica 12 bold').pack()
#label for question
Label(master,text='',textvariable=que,bg="#04112d",fg="#ffffff",font='Helvetica 13 bold').place(x=90,y=35)
#radiobuttno for option1
Radiobutton(master,text='',variable=v,value="1",bg="#04112d").place(x=140,y=60)
#label for option1
Label(master,text="",textvariable=op1,bg="#04112d",fg="#ffffff",font='Helvetica 12').place(x=160,y=60)
#radiobutton for option2
Radiobutton(master,text='',variable=v,value="2",bg="#04112d").place(x=140,y=80)
#label for option2
Label(master,text="",textvariable=op2,bg="#04112d",fg="#ffffff",font='Helvetica 12').place(x=160,y=80)
#radiobutton for option3
Radiobutton(master,text='',variable=v,value="3",bg="#04112d").place(x=140,y=100)
#label for option3
Label(master,text="",textvariable=op3,bg="#04112d",fg="#ffffff",font='Helvetica 12').place(x=160,y=100)
#radiobutton for option4
Radiobutton(master,text='',variable=v,value="4",bg="#04112d").place(x=140,y=120)
#label for option4
Label(master,text="",textvariable=op4,bg="#04112d",fg="#ffffff",font='Helvetica 12').place(x=160,y=120)
#setting first question in label
que.set("Q.1 "+QueList[0])
#passing first question's options in variable option
option=OptList[0]
#displaying options in labels
op1.set(option[0])
op2.set(option[1])
op3.set(option[2])
op4.set(option[3])

#incrementing i
i+=1
#defining function
def myFun():
    #declaring i and result as global variable
    global i
    global result
    #applying condition for question
    if i<=len(QueList):
     #applying condition for selected option
     if v.get() == OutList[i-1]:
         #incrementing the result counter
         result+=1
     # applying condition for last question
     if(i!=len(QueList)):
      #setting question in label
      que.set("Q."+str(i+1)+" "+(QueList[i]))
      option=OptList[i]
      #setting options in labels
      op1.set(option[0])
      op2.set(option[1])
      op3.set(option[2])
      op4.set(option[3])

     else:
         #displaying result
      messagebox.showinfo("Result","Total Question:"+str(len(QueList))+"\nCorrect:"+str(result)+"\nIncorrect:"+str(len(QueList)-result)+"\nResult:"+str((result/(len(QueList))*100))+"%")
    #incrementing i for question
    i += 1
#label for instruction
Label(master,text="Click on radio button to answer",font='Helvetica 11',bg="#04112d",fg="yellow").place(x=100,y=180)
#button for submit and next
Button(master,text="Next",command=myFun,bg="blue",fg="white",width="10",font='Helvetica 12').place(x=160,y=200)
# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
mainloop() 