class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(""" welclome to Chatbook !! How would you like to procced ?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           \nEnter a number : """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email id here : ")
        pwd = input("Setup your password here : ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Plese sign up first by processing 1 in the main menu")
        else:
            uname = input("Enter your email id/username here : ")
            pwd = input("Enter your password here : ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please enter correct credentials !!")

        print("\n")
        self.menu()


    def post(self):
        if self.loggedin == True:
            txt = input("Write your post here: ")
            print(f"Your following content has been posted: {txt}")
        else:
            print("You need to sign in first to write a post.")
        print("\n")
        self.menu()


    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here : ")
            frnd = input("whom to send the message? : ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to sign in first to send message to your friend !! ")
        print("\n")
        self.menu()
        


# obj = Chatbook()
