class file_handler:
    load = {}
    def load(self):
        load = {}

    def querry_login(self, username, password):
        try:
            return True

        except:
            print("Login Failed")
        return False

    def register(self, username, password):
        #with open("src/main/python/revature/io/user.txt", "a") as f:
        with open("io/user.txt", "a") as f:
            f.write("\n"+username+","+password)

