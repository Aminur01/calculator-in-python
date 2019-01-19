from tkinter import*
#for taking the number
def btnClk(number):
	global operator
	operator=operator + str(number)
	text_Input.set(operator)
#for AC ie to clear
def btnClrDsply():
	global operator
	operator=""
	text_Input.set("")
#for equal
def btnEqlInpts():
	global operator 
	sumup=str(eval(operator))
	text_Input.set(sumup)
	operator=""
	

cal=Tk()
cal.title("Aminur")
operator=""
text_Input =StringVar()

#main display
txtDisplay = Entry(cal,font=('arial',20,'bold'),fg="red", textvariable=text_Input, bd=30, insertwidth=4, bg="black", justify='right').grid(columnspan=4)

#buttons
btnac=Button(cal,padx=6,bd=8, fg="red",font=('arial',20,'bold'),text="AC", bg="black", command=btnClrDsply).grid(row=1,column=0)

btnmult=Button(cal,padx=20,bd=8, fg="red",font=('arial',20,'bold'),text="*",bg="black", command=lambda:btnClk("*")).grid(row=1,column=1)

btndiv=Button(cal,padx=20,bd=8, fg="red",font=('arial',20,'bold'),text="/",bg="black", command=lambda:btnClk("/")).grid(row=1,column=2)

add=Button(cal,padx=20,bd=8, fg="red",font=('arial',20,'bold'),text="+",bg="black", command=lambda:btnClk("+")).grid(row=1,column=3)


btn7=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="7",bg="black",command=lambda:btnClk(7)).grid(row=2,column=0)

btn8=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="8",bg="black",command=lambda:btnClk(8)).grid(row=2,column=1)

btn9=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="9",bg="black",command=lambda:btnClk(9)).grid(row=2,column=2)

sub=Button(cal,padx=24,bd=8, fg="red",font=('arial',20,'bold'),text="-",bg="black",command=lambda:btnClk("-")).grid(row=2,column=3)


btn4=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="4",bg="black",command=lambda:btnClk(4)).grid(row=3,column=0)

btn5=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="5",bg="black",command=lambda:btnClk(5)).grid(row=3,column=1)

btn6=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="6",bg="black",command=lambda:btnClk(6)).grid(row=3,column=2)

btnzero=Button(cal,padx=20,bd=8, fg="red",font=('arial',20,'bold'),text="0",bg="black",command=lambda:btnClk(0)).grid(row=3,column=3)


btn1=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="1",bg="black",command=lambda:btnClk(1)).grid(row=4,column=0)

btn2=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="2",bg="black",command=lambda:btnClk(2)).grid(row=4,column=1)

btn3=Button(cal,padx=16,bd=8, fg="red",font=('arial',20,'bold'),text="3",bg="black",command=lambda:btnClk(3)).grid(row=4,column=2)

diveq=Button(cal,padx=20,bd=8, fg="red",font=('arial',20,'bold'),text="=",bg="black",command=btnEqlInpts).grid(row=4,column=3)

cal.mainloop()

