import time
import random

class MoneyMakingApp:
    def __init__(self):
        self.balance = 0
    def show_menu(self):
        print("\n---WELCOME TO THE MONEY-MAKING APP---")
        print("*"*20)
        print("1. Answer a survey (Earn Rs.100)")
        print("2. Watch an AD (Earn Rs.50)")
        print("3. Check Balance")
        print("4. Redeem Balance")
        print("5. Exit")
        print("*"*20)
    def answer_survey(self):
        print("\n--ANSWERING A QUICK SURVEY--")
        time.sleep(3)
        self.balance += 100
        print("SURVEY COMPLETED! YOU'VE EARNED RS.100")
        print("*"*20)
    def watch_ad(self):
        print("\n--WATCHING AN AD--")
        time.sleep(3)
        self.balance += 50
        print("AD WATCHED! YOU'VE EARNED RS.50")
        print("*"*20)
    def check_balance(self):
        print(f"\n YOUR CURRENT BALANCE IS : RS {self.balance}")
    def redeem_balance(self):
        if self.balance > 0:
            print(f"\n REDEEM YOUR BALANCE OF RS {self.balance}...")
            time.sleep(2)
            print("BALANCE REDEEMED SUCCESSFULLY!")
            self.balance = 0
        else:
            print("\n YOUR BALANCE IS ZERO! EARN SOME MONEY FIRST")
    def run(self):
        while True:
            self.show_menu()
            choice = input("Select an option (1-5): ")
            if choice == '1':
                self.answer_survey()
            elif choice == '2':
                self.watch_ad()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                self.redeem_balance()
            elif choice == '5':
                print("EXITING THE APP, GOODBYE!")
                break
            else:
                print("INVALID OPTION. PLEASE TRY AGAIN")
if __name__ == "__main__":
    app = MoneyMakingApp()
    app.run()
