from unicodedata import category


class Application:

    def __init__(self,application_name,category,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.company=company
        self.app_size=app_size
        self.no_of_user=no_of_users
        self.ratings=ratings


    def signup(self):
        print(f"Signup done,{self.application_name}")

    def login(self):
        print(f"Welcome to {self.application_name}")

    def logout(self):
        print(f"Thank You for using{self.application_name}")

    def info(self):
        print(self.application_name,"\n",self.category,"\n",self.company,"\n",self.app_size,"\n",self.no_of_user,"\n",self.ratings,"\n")




app1=Application("Instagram","Social Media","Meta",100,10000,4.5)

app2=Application("Facebook","Social Media","Meta",100,2000,4.6)

app3=Application("WhatsApp","Social Media","Meta",80,50000,5)






app1.signup()
app1.login()
app1.logout()
app1.info()


app2.signup()
app2.login()
app2.logout()
app2.info()

app3.signup()
app3.login()
app3.logout()
app3.info()





