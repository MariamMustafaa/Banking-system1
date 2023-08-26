import pandas as pd #for storing el data 
import os
import random #3lshan el number bta3 el accounts

#first class
class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []
        self.current_customer = None

    def create_customer(self, name):
        customer = Customer(name)
        self.customers.append(customer)
        return customer

    def create_account(self, customer):
        account = Account(customer)
        self.accounts.append(account)
        return account

    def get_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def login(self, name):
        customer = self.get_customer(name)
        if customer is None:
            return False
        self.current_customer = customer
        return True

    def logout(self):
        self.current_customer = None

#2nd
class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

class Account:
    def __init__(self, customer):
        self.customer = customer
        self.balance = 0
        self.account_number = random.randint(10000000, 99999999)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def transfer(self, amount, recipient_account_number):
        recipient_account = bank.get_account(recipient_account_number)
        if recipient_account is None:
            raise ValueError("Recipient account not found")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        recipient_account.deposit(amount)
        self.withdraw(amount)


bank = Bank()

while True:
    print("1. Existing Account")
    print("2. New Account")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        if not bank.login(name):
            print("Customer not found")
            continue
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Transfer")
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                amount = int(input("Enter amount to deposit: "))
                bank.current_customer.balance += amount
                print(f"New balance: {bank.current_customer.balance}")
            elif choice == "2":
                amount = int(input("Enter amount to withdraw: "))
                try:
                    if amount > bank.current_customer.balance:
                        raise ValueError("Insufficient funds")
                    bank.current_customer.balance -= amount
                    print(f"New balance: {bank.current_customer.balance}")
                except ValueError as e:
                    print(str(e))
            elif choice == "3":
                print(f"Balance: {bank.current_customer.balance}")
            elif choice == "4":
                recipient_account_number = int(input("Enter recipient account number: "))
                recipient_account = bank.get_account(recipient_account_number)
                if recipient_account is None:
                    print("Recipient account not found")
                    continue
                amount = int(input("Enter amount to transfer: "))
                try:
                    if amount > bank.current_customer.balance:
                        raise ValueError("Insufficient funds")
                    bank.current_customer.balance -= amount
                    recipient_account.balance += amount
                    print(f"New balance: {bank.current_customer.balance}")
                except ValueError as e:
                    print(str(e))
            elif choice == "5":
                bank.logout()
                break
    elif choice == "2":
        name = input("Enter your name: ")
        customer = bank.create_customer(name)
        account = bank.create_account(customer)
        print(f"Account created with number {account.account_number}")


