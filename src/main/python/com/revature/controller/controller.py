import src.main.python.com.revature.service.business as b

class controller:
    def initalize(self, other):
        self.business = other
        other.change_state("init")

    def run(self):
        while(True):
            if(self.business.state=="1"):
                print("----------")
                print("1: login")
                print("2: register")
                print("0: exit")
                data = input()
                if(data=='0'):
                    break
                elif(data=='1'):
                    self.business.change_state("login")
                elif(data=='2'):
                    self.business.change_state("register")
            elif(self.business.state=="login"):
                print("----------")
                print("Username")
                username = input()
                print("Password")
                password = input()
                try:
                    self.business.querry_login(username, password)
                except:
                    print("Failed Login")
            elif (self.business.state=="register"):
                print("----------")
                print("Username")
                username = input()
                print("Password")
                password = input()
                # add code
                # throw error
            elif (self.business.state=="LoggedIn"):
                print("----------")
                print("Logged in")
                print("1: View Balance")
                print("2: View Past Transactons")
                print("3: Deposit")
                print("4: Withdraw")
                print("0: Log out")
                data = input()
                if(data=='0'):
                    self.business.change_state("1")
                elif(data=='1'):
                    self.business.display_balance()
                elif(data=='2'):
                    self.business.display_past_transactions()
                elif(data=='3'):
                    print("amount")
                    amount = float(input())
                    self.business.transaction(amount)
                elif (data=='4'):
                    print("amount")
                    amount = -float(input())
                    self.business.transaction(amount)
            elif(self.business.state=="init"):
                print("Welcome to Bank Terminal")
                self.business.change_state("1")
            else:
                #add error later
                break
