import src.main.python.com.revature.error.io_errors as ioe
import os

class file_handler:
    load = {}
    def load(self):
        load = {}

    def querry_login(self, username, password):
        with open("io/user.txt", "r") as f:
            data = f.read()
            data = data.split("\n")
            loginlist = dict()
            for line in data:
                n = line.split(",")
                loginlist[n[0]] = n[1]
            try:
                if(loginlist[username]==password):
                    return True
            except:
                raise ioe.login_fail_exception
        return False

    def querry_money(self, username):
        with open("io/"+username+"/amount.txt", "r") as f:
            return float(f.read())

    def querry_register(self, username):
        with open("io/user.txt", "r") as f:
            data = f.read()
            data = data.split("\n")
            for line in data:
                line = line.split(",")[0]
                if(line == username):
                    return False
        return True

    def register(self, username, password):
        #with open("src/main/python/revature/io/user.txt", "a") as f:
        with open("io/user.txt", "a") as f:
            f.write("\n"+username+","+password)
        os.mkdir("io/"+username)
        with open("io/"+username+"/amount.txt", "w") as f:
            f.write("0")
        with open("io/"+username+"/history.txt", "w") as f:
            f.write("Account Initialization: 0")

    def add_transaction_history(self, username, message):
        with open("io/"+username+"/history.txt", "a") as f:
            f.write("\n"+message)

    def querry_transaction_history(self, username):
        with open("io/"+username+"/history.txt", "r") as f:
            print(f.read())

    def save_balance(self, username, balance):
        with open("io/"+username+"/amount.txt", "w") as f:
            f.write(str(balance))