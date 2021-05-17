import json
import pickle

expenses = []
list_filename = "list.pkl"

def option():
    print("1: Add expenses\n2: View Expenses")
    selection = int(input("select 1 to ADD or 2 to View Expenses\n"))
    if(selection == 1):
        add_expenses()

    elif(selection == 2):
        view_expenses()

    else:
        print("please enter 1 or 2")
        option()

def add_expenses(): 
    open_file = open(list_filename, 'rb')
    expenses = pickle.load(open_file)
    open_file.close

    latest_expense = int(input("enter your latest expense in AUD\n"))
    expenses.append(latest_expense)
    open_file = open(list_filename, 'wb')
    pickle.dump(expenses, open_file)
    open_file.close
    print("expense added successfully")
    option()


def view_expenses():
    open_file = open(list_filename, 'rb')
    expenses = pickle.load(open_file)
    total_expense = sum(expenses)
    print("your individual expenses are ",expenses)
    print("your total expense is: ", total_expense)
    option()

option()
    