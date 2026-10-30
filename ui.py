from tkinter import *
from tkinter import messagebox
import database

db=database.Database('d:/python/exam/mydata.db')

win = Tk()
win.geometry('700x550')
win.title('information')
win.configure(bg='pink')
win.resizable(0,0)

# Function ----------------------------------------------------------------------------------------

def show_list ():
    item = db.select_item()
    lst_contacts.delete(0,END)
    for i in item:
        lst_contacts.insert(END,i)

def insert_list():
    fname = ent_fname.get()
    lname = ent_lname.get()
    password = ent_password.get()
    if  fname=='' or lname=='' or password=='':
        messagebox.showerror('error' , 'fill in the blank')
    else:
        fname = ent_fname.get()
        lname = ent_lname.get()
        cname = ent_cname.get ()
        password = ent_password.get()

    
        db.insert_item(fname,lname,cname,password)
        messagebox.showinfo('insert' , 'item inserted')
        clear_ent()


def clear_ent():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_cname.delete(0,END)
    ent_password.delete(0,END)
    ent_passwordd.delete(0,END)
    ent_fname.focus_set()

def select ():
    index = lst_contacts.curselection()
    if index:
        record = lst_contacts.get(index[0])
        clear_ent()
        ent_fname.insert(0,record[1])
        ent_lname.insert(0,record[2])
        ent_cname.insert(0,record[3])
        ent_password.insert(0,record[4])



def remove_item():
    select()
    index = lst_contacts.curselection()
    if index:
        remove = messagebox.askquestion('remove','are you sure?')
        if remove== 'yes':
            record = lst_contacts.get(index[0])
            db.remove_item(record[0])
            show_list()

def exitt ():
    result = messagebox.askquestion('exit','are you sure ? ')
    if result== 'yes':
        win.destroy()

def sign_in ():
    passwordd = ent_passwordd.get()
    lst_contacts.delete(0,END)
    rec = db.search_item(passwordd)
    if rec :
        root = Toplevel(win)
        root.geometry('200x200')
        root.configure(bg='light blue')
        root.title('welcome')
        lbl_welcome=Label(root , text='welcom  '+rec[0][1] , bg='light blue' , font='tahoma 10 bold').pack()

    else:
        messagebox.showerror('insert' , 'please insert your information first')
# widget   ----------------------------------------------------------------------------------------

lbl_star = Label(win , text = '*' , font='arial 17 bold ' , fg = 'red' , bg= 'pink')
lbl_star.place( x=20 , y=20 )

lbl_fname= Label(win , text = 'First name :' , font =( 'arial' , 12 , 'bold')  , bg = 'pink')
lbl_fname.place(x=35 , y=20)
ent_fname = Entry (win )
ent_fname.place(x=140, y= 23)

# ---

lbl_star = Label(win , text = '*' , font='arial 17 bold ' , fg = 'red' , bg= 'pink')
lbl_star.place( x=300 , y=20 )

lbl_lname= Label(win , text = 'Last name : ' , font ='arial 12 bold ' , bg='pink')
lbl_lname.place(x = 315 , y= 20)
ent_lname= Entry(win)
ent_lname.place(x=420 , y=23 )

# ---

lbl_star = Label(win , text = '*' , font='arial 17 bold ' , fg = 'red' , bg= 'pink')
lbl_star.place( x=20 , y=70 )

lbl_password = Label(win , text= 'password :' , font= 'arial 12 bold ' , bg='pink')
lbl_password.place(x=35 , y=70)
ent_password = Entry(win ,show='*')
ent_password.place(x= 140 , y=73)

# ---

lbl_cname= Label(win , text= 'course name :' , font='arial 12 bold' , bg= 'pink')
lbl_cname.place(x=300,y=70)
ent_cname = Entry(win)
ent_cname.place(x =420 , y=73)

# ---

lbl_sign=Label(win , text='if you have already signed up , enter your password ' , font='arial 12 bold' , bg= 'pink')
lbl_sign.place(x=20 , y=420)

lbl_passwordd = Label(win , text= 'password :' , font= 'arial 12 bold ' , bg='pink')
lbl_passwordd.place(x=20 , y=450)
ent_passwordd = Entry(win ,show='*')
ent_passwordd.place(x= 135, y=453)

# ---

lst_contacts = Listbox(win, width=65 , height=15)
lst_contacts.place(x=20 ,y=150)



btn_show=Button(win ,text='show' , font='tahoma 10 bold' , command=show_list, width=20)
btn_show.place(x=470 , y=150)

btn_insert=Button(win ,text='insert' , font='tahoma 10 bold' , command=insert_list , width=20)
btn_insert.place(x=470 , y=190)


btn_clear=Button(win ,text='clear' , font='tahoma 10 bold' , command=clear_ent , width=20)
btn_clear.place(x=470 , y=230)


btn_remove=Button(win ,text='remove' , font='tahoma 10 bold' , command=remove_item, width=20)
btn_remove.place(x=470 , y=270)


btn_exit=Button(win ,text='exit' , font='tahoma 10 bold' , command=exitt, width=20)
btn_exit.place(x=470, y=310)


btn_signin=Button(win ,text='sgin in' , font='tahoma 10 bold' , command=sign_in, width=20)
btn_signin.place(x=470, y=350)



win.mainloop()