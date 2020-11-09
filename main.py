import random


class Bank:
    def __init__(self):
        self.balance = 0

    def menu(self):
        while True:
            self.choice = input("1. Create an account\n2. Log into account\n0. Exit\n")
            if self.choice == "1":
                self.cardnum_generate()
                self.cardpass_generate()
                print("Your card has been created")
                print(f"Your card number:\n{int(self.cardnum)}")
                print(f"Your card PIN:\n{self.cardpass}\n")
                
            elif self.choice == "2":
                self.user_cardnum_inpt = input("Enter your card number:\n")
                self.user_cardpass_inpt = input("Enter your PIN:\n")
                if self.cardnum == self.user_cardnum_inpt:
                    if self.cardpass == self.user_cardpass_inpt:
                        print("You have successfully logged in!\n")
                        self.card_menu()
                    else:
                        print("Wrong card number or PIN!\n")
                else:
                        print("Wrong card number or PIN!\n")
            elif self.choice == "0":
                print("\nBye!")
                exit()


    def card_menu(self):
        while True:
            self.card_menu_choice = input("1. Balance\n2. Log out\n0. Exit\n")    
            if self.card_menu_choice == "1":
                print(f"\nBalance: {self.balance}\n")
            elif self.card_menu_choice == "2":
                print("You have successfully logged out!\n")
                break
            elif self.card_menu_choice == "0":
                print("\nBye!")
                exit()

    def cardnum_generate(self):
        self.card_first_half = "400000"
        self.card_second_half = ""
        for x in range(9):
            self.card_second_half += str(random.randint(0, 9))
        self.checksum = random.randint(0, 9)
        self.cardnum = self.card_first_half + str(self.card_second_half) + str(self.checksum)

    def cardpass_generate(self):
        self.cardpass = ""
        for x in range(4):
            self.cardpass += str(random.randint(0, 9))


my_bank = Bank()
my_bank.menu()

