from tkinter import *
from tkinter import messagebox
import frontend.signup
import frontend.customerDashboard
from backend.loginManagement import login
from middleware.customer import Customer


class Signin:

    def __init__(self, root):
        self.root = root
        self.root.title("SignIn")
        self.root.geometry("550x500")  # size of the window
        self.root.state('zoomed')  # windows on zoomed / full-screen size
        self.root.resizable(False, False)  # windows resizable false
        self.root.config(background="#CECED2")  # background color change

        def signup():
            self.root.destroy()
            root = Tk()
            obj = frontend.signup.Registration(root)
            root.mainloop()

        font1 = ('Cooper Black', 30, "bold")
        font2 = ('Cordia New', 14)
        font3 = ('Times New Roman', 25, "bold")

        def login720():
            cus_login = Customer(email=email_txt.get(),
                                 password=password11.get())
            user = login(cus_login)

            if (email_txt.get() == '') or (password11.get() == ''):
                msg11 = messagebox.showwarning(
                    "Taxi Booking System", "Please Enter Email and Password")

            else:
                if user == None:
                    msg1 = messagebox.showerror(
                        "Taxi Booking System", "Error: Wrong Username or Password")
                else:
                    msg2 = messagebox.showinfo(
                        "Taxi Booking System", "Welcome {}".format(user[1]))
                    self.root.destroy()
                    root = Tk()
                    frontend.customerDashboard.CusDashboard(root)
                    root.mainloop()

        # First frame
        frame1 = Frame(root, bg="#EFEFF4", height=650, width=600)

        signin_txt = Label(frame1, text="Sign in", font=font1)
        signin_txt.place(x=200, y=160)

        email_frame = LabelFrame(frame1, text="Email")
        email_frame.place(x=175, y=250)

        email_txt = Entry(email_frame, text="", font=font2, relief=RAISED)
        email_txt.pack()

        password_frame = LabelFrame(frame1, text="Password")
        password_frame.place(x=175, y=300)

        password11 = Entry(password_frame, text="", font=font2, relief=RAISED)
        password11.pack()

        btn_signin = Button(frame1, text="Submit", font=font3,
                            relief=GROOVE, command=login720, bg="#4CD964", fg="#EFEFF4")
        btn_signin.place(x=220, y=375)

        frame1.place(x=175, y=100)

        # Second Frame
        frame2 = Frame(self.root, bg="#4CD964", height=650, width=600)

        signup_lbl = Label(frame2, text="Sign UP", bg="#4CD964",
                           font=font1, fg="#EFEFF4")
        signup_lbl.place(x=200, y=200)

        signup_txt = Label(
            frame2, text="Sign up here if you don't have account", bg="#4CD964", font=font2)
        signup_txt.place(x=125, y=300)

        btn_signup = Button(frame2, text="SIGN UP", font=font3,
                            relief=GROOVE, command=signup, bg="#EFEFF4")
        btn_signup.place(x=200, y=350)

        frame2.place(x=775, y=100)
