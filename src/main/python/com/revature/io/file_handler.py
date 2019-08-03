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

    def querry_register(self, username):
        with open("io/user.txt", "r") as f:
            data = f.read()
            data = data.split("\n")
            for line in data:
                line = line.split(",")[0]
                print(line)
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
