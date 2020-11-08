from tkinter import *
import tkinter.messagebox
import threading
from word2number import w2n
from num2words import num2words



class Website_url:
    def __init__(self,root):
        self.root=root
        self.root.title("Website Url")
        self.root.iconbitmap("logo733.ico")
        self.root.geometry("500x260")
        self.root.resizable(0,0)



        inputs=StringVar()



        def on_enter1(e):
            but_w2n['background']="black"
            but_w2n['foreground']="cyan"
            
            

        def on_leave1(e):
            but_w2n['background']="SystemButtonFace"
            but_w2n['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def on_enter3(e):
            but_n2w['background']="black"
            but_n2w['foreground']="cyan"
            
            

        def on_leave3(e):
            but_n2w['background']="SystemButtonFace"
            but_n2w['foreground']="SystemButtonText"



        def WtoN():
            try:
                text.delete('1.0','end')
                if inputs.get()!="":
                    if not inputs.get().isdigit():
                        convert=str(w2n.word_to_num(inputs.get()))
                        ans="{0} Converted to digit = {1}".format(inputs.get(),convert)
                        text.insert('end',ans)
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter words")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter words")
  
            except Exception as e:
                tkinter.messagebox.showerror("Error","Invalid Word")

        

        def NtoW():
            try:
                text.delete('1.0','end')
                if inputs.get()!="":
                    if inputs.get().isdigit():
                        convert=num2words(int(inputs.get()))
                        ans="{0} Converted to words = {1}".format(inputs.get(),convert)
                        text.insert('end',ans)
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Integer")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter words")
            except Exception as e:
                tkinter.messagebox.showerror("Error","Please Enter number")

      


        def clear():
            inputs.set("")
            text.delete('1.0','end')



#==================frame=========================#
        mainframe=Frame(self.root,width=500,height=260,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)


        firstframe=Frame(mainframe,width=494,height=130,relief="ridge",bd=3,bg="#e842ff")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=123,relief="ridge",bd=3)
        secondframe.place(x=0,y=130)

#=========================firstframe========================================#
        

        lab_website_url=Label(firstframe,text="Enter A Word Or A Number",font=('times new roman',12),bg="#e842ff",fg="white")
        lab_website_url.place(x=150,y=10)

        ent_website_url=Entry(firstframe,width=38,font=('times new roman',12),relief="ridge",bd=4,textvariable=inputs)
        ent_website_url.place(x=80,y=40)

        but_w2n=Button(firstframe,text="Word To Number",width=13,font=('times new roman',12),cursor="hand2",command=WtoN)
        but_w2n.place(x=30,y=80)
        but_w2n.bind("<Enter>",on_enter1)
        but_w2n.bind("<Leave>",on_leave1)


        but_n2w=Button(firstframe,text="Number To Word",width=13,font=('times new roman',12),cursor="hand2",command=NtoW)
        but_n2w.place(x=180,y=80)
        but_n2w.bind("<Enter>",on_enter3)
        but_n2w.bind("<Leave>",on_leave3)


        but_clear=Button(firstframe,text="Clear",width=13,font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=330,y=80)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=========================secondframe======================================#

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=6,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Website_url(root)
    root.mainloop()
