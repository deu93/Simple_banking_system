import random
import sqlite3

# Connect db
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class Bank:
    def __init__(self):
        self.balance = 0
        self.id = 0
    
    # Menu
    def menu(self):
        while True:
            self.choice = input("1. Create an account\n2. Log into account\n0. Exit\n")
            if self.choice == "1":
                self.cardnum_generate()
                self.cardpass_generate()
                print("Your card has been created")
                print(f"Your card number:\n{int(self.final_cardnum3)}")
                print(f"Your card PIN:\n{self.cardpass}\n")
                
            elif self.choice == "2":
                self.user_cardnum_inpt = input("Enter your card number:\n")
                self.user_cardpass_inpt = input("Enter your PIN:\n")
                if self.final_cardnum3 == self.user_cardnum_inpt:
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

    # Card info generate
    def cardnum_generate(self):
        self.card_first_half = "400000"
        self.card_second_half = ""
        for x in range(9):
            self.card_second_half += str(random.randint(0, 9))
        self.checksum = random.randint(0, 9)
        self.cardnum = self.card_first_half + str(self.card_second_half) 
        self.sum_cardnums = 0
        self.cardnum2 = [int(x) for x in self.cardnum]
        self.cardnum3 = [v for k, v in enumerate(self.cardnum2) if not k%2]
        self.cardnum4 = [v for k, v in enumerate(self.cardnum2) if k%2]
        self.final_cardnum = self.cardnum
        self.final_cardnum3 = ""
        self.cheksum_gen()
        self.db_creating
        
    
    def cheksum_gen(self):
        for x in self.cardnum3:
                x = x * 2
                if x >= 9:
                    x -= 9
                self.sum_cardnums += x
        for x in self.cardnum4:
            self.sum_cardnums += x
        if self.sum_cardnums % 10 == 0:
            self.final_cardnum3 = self.cardnum + "0"
        else:
            self.checksum_num = self.sum_cardnums % 10
            self.checksum_num1 = 10 - self.checksum_num
            self.final_cardnum3 = self.cardnum + str(self.checksum_num1)
            
    def cardpass_generate(self):
        self.cardpass = ""
        for x in range(4):
            self.cardpass += str(random.randint(0, 9))
    
    # SQL query
    def db_creating(self):
        cur.execute('SELECT id')
        if len(cur.fetchone()) < 0:
            cur.execute('CREATE DATABASE card.s3db')
            cur.execute('CREATE TABLE card(id INT,number TEXT,pin TEXT,balance INTEGER DEAFULT 0)')
        else:
            cur.execute('INSERT INTO card VALUES({self.id+=1,self.final_cardnum3,self.cardpass,self.balance})')

    
        
my_bank = Bank()
my_bank.menu()