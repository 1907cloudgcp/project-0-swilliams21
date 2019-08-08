import src.main.python.com.revature.controller.controller as c
import src.main.python.com.revature.io.file_handler as fh
import src.main.python.com.revature.error.business_errors as be
import src.main.python.com.revature.error.io_errors as ioe
import logging

class business:
    logging.basicConfig(filename="banklog.log", level=logging.DEBUG, filemode="a")

    def __init__(self, runbool=True):
        logging.debug("Opened: {}".format(__name__))
        self.state = "loading"
        self.io = fh.file_handler()
        self.controller = c.controller()
        self.run(runbool)

    def run(self, run):
        self.io.load()
        self.controller.initalize(other=self)
        logging.debug("Run: {}".format(__name__))
        if(run):
            self.controller.run()

    def change_state(self, state):
        logging.info("State: {}->{}".format(self.state, state))
        self.state = state

    def querry_login(self, username, password):
        if(self.io.querry_login(username, password)):
            self.change_state("LoggedIn")
            self.user = username
            self.money = self.io.querry_money(username)
            logging.info("Login: {}".format(username))
            return True
        else:
            logging.error("Login Failed: {}".format(username))
            raise ioe.login_fail_exception

    def querry_register(self, username, password):
        if(self.io.querry_register(username)):
            self.io.register(username, password)
            self.change_state("1")
            print("registration successful")
            logging.info("Registration: {}".format(username))
            return True
        else:
            logging.error("Registration Fail: {}".format(username))
            raise ioe.registration_fail_exception

    def display_balance(self):
        print("Balance: "+str(self.money))
        logging.info('Money: {}'.format(self.money))

    def display_past_transactions(self):
        self.io.querry_transaction_history(self.user)
        logging.info('Transaction Viewed: {}'.format(self.user))

    def transaction(self, amount):
        self.money += amount
        self.io.save_balance(self.user, self.money)
        logging.debug('Transaction: {}, {}'.format(self.user, amount))

    def querry_deposite(self, amount):
        try:
            if(amount<0):
                raise be.negative_transaction_exception
            else:
                self.transaction(amount)
                self.io.add_transaction_history(self.user, "Deposite: "+str(amount))
                logging.info('Deposite Successful: {}, {}'.format(self.user, amount))
        except be.negative_transaction_exception:
            print("Negative Number Detected: Negative numbers are not allowed")
            logging.warning('Negative Transaction Exception: Negative Numbers are not Allowed: {}, {}'.format(self.user, amount))
        except be.transaction_exception:
            print("Unknown Transaction Exception: Idk, it broke")
            logging.warning('Unknown Transaction Error: It broke: {}, {}'.format(self.user, amount))

    def querry_withdraw(self, amount):
        try:
            if(amount<0):
                raise be.negative_transaction_exception
            elif(amount>self.money):
                raise be.not_enough_money_exception
            else:
                self.transaction(-amount)
                self.io.add_transaction_history(self.user, "Withdraw: "+str(amount))
                logging.info('Withdraw Successful: {}, {}'.format(self.user, amount))
        except be.negative_transaction_exception:
            print("Negative Number Detected: Negative numbers are not allowed")
            logging.error('Negative Transaction Exception: Negative Numbers are not Allowed: {}, {}'.format(self.user, amount))
        except be.not_enough_money_exception:
            print("Not Enough Money for Withdraw")
            logging.warning("Not Enough Money For Transaction: {}, {}, <- {}".format(self.user, self.money, amount))
        except be.transaction_exception:
            print("Unknown Transaction Exception: Idk, it broke")
            logging.warning('Unknown Transaction Error: It broke: {}, {}'.format(self.user, amount))