import src.main.python.com.revature.controller.controller as c
import src.main.python.com.revature.io.file_handler as fh
import src.main.python.com.revature.error.business_errors as be
import src.main.python.com.revature.error.io_errors as ioe


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
        if(self.io.querry_login(username,password)):
            self.change_state("LoggedIn")
            self.user = username
            self.money = self.io.querry_money(username)
        else:
            raise ioe.login_fail_exception

    def querry_register(self, username, password):
        if(self.io.querry_register(username)):
            self.io.register(username, password)
            self.change_state("1")
            print("registration successful")
        else:
            raise ioe.registration_fail_exception

    def display_balance(self):
        print("Balance: "+str(self.money))

    def display_past_transactions(self):
        self.io.querry_transaction_history(self.user)

    def transaction(self, amount):
        self.money += amount
        self.io.save_balance(self.user, self.money)

    def querry_deposite(self, amount):
        try:
            if(amount<0):
                raise be.negative_transaction_exception
            else:
                self.transaction(amount)
                self.io.add_transaction_history(self.user, "Deposite: "+str(amount))
        except be.negative_transaction_exception:
            print("Negative Transaction Exception: Negative Numbers are not Allowed")

        except be.transaction_exception:
            print("Unknown Transaction Exception: Idk, it broke")

    def querry_withdraw(self, amount):
        try:
            if(amount<0):
                raise be.negative_transaction_exception
            elif(amount>self.money):
                raise be.not_enough_money_exception
            else:
                self.transaction(-amount)
                self.io.add_transaction_history(self.user, "Withdraw: "+str(amount))
        except be.negative_transaction_exception:
            print("Negative Transaction Exception: Negative Numbers are not Allowed")
        except be.not_enough_money_exception:
            print("Not Enough Money for Withdraw")
        except be.transaction_exception:
            print("Unknown Transaction Exception: Idk, it broke")
