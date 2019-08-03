import src.main.python.com.revature.controller.controller as c
import src.main.python.com.revature.io.file_handler as fh
import src.main.python.com.revature.error.business_errors as be


class business:

    def __init__(self):
        self.io = fh.file_handler()
        self.controller = c.controller()
        self.run()

    def run(self):
        self.io.load()
        self.controller.initalize(other=self)
        self.controller.run()

    def change_state(self, state):
        self.state = state

    def querry_login(self, username, password):
        if(True):
            self.change_state("LoggedIn")

    def querry_register(self, username, password):
        if(True):
            self.io.register(username, password)
            self.change_state("1")
            print("registration successful")

    def display_balance(self):
        print("poor")

    def display_past_transactions(self):
        print("poor")

    def transaction(self, amount):
        print("poor " + str(amount))