import csv
import os

# Define filenames
CUSTOMER_FILE = "customers.csv"

# Function to initialize default customer data
def initialize_customers():
    customers = [
        {'Name': 'Mayank Srivastava', 'Pin': '6394', 'Balance': 200000000.00},
        {'Name': 'Harsh Joshi', 'Pin': '9632', 'Balance': 19000000.00},
        {'Name': 'Aayan Saifi', 'Pin': '7316', 'Balance': 3000000.00},
        {'Name': 'Kartikey', 'Pin': '9874', 'Balance': 10000.00},
        {'Name': 'Rishabh', 'Pin': '8521', 'Balance': 150099.00},
    ]
    
    # Write default customer data to CSV
    with open(CUSTOMER_FILE, mode='w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Pin', 'Balance'])
        writer.writeheader()
        writer.writerows(customers)

# Function to read customer data from CSV
def read_customers():
    customers = {}
    if os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, mode='r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers[row['Name']] = {
                    'Pin': row['Pin'],
                    'Balance': float(row['Balance'])
                }
    else:
        # Initialize with default customers if file does not exist
        initialize_customers()
        return read_customers()  # Recursively call to read data after initialization
    return customers

# Function to write customer data to CSV
def write_customers(customers):
    with open(CUSTOMER_FILE, mode='w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Pin', 'Balance'])
        writer.writeheader()
        for name, data in customers.items():
            writer.writerow({'Name': name, 'Pin': data['Pin'], 'Balance': data['Balance']})

# Function to authenticate the user
def authenticate_user(customers):
    while True:
        name = input("Enter your name: ")
        if name not in customers:
            print("Customer not found.")
            continue
        pin = input("Enter your PIN: ")  # Use input instead of getpass.getpass
        if pin == customers[name]['Pin']:
            return name
        else:
            print("Incorrect PIN. Please try again.")

# Function to check balance
def check_balance(customers, user):
    print("***********************")
    print(f"Your current balance is: ${customers[user]['Balance']:.2f}")
    print("**********************************")

# Function to withdraw amount
def withdraw_amount(customers, user):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > customers[user]['Balance']:
                print("Insufficient balance.")
            else:
                pin = input("Enter your PIN to confirm withdrawal: ")  # Use input instead of getpass.getpass
                if pin == customers[user]['Pin']:
                    customers[user]['Balance'] -= amount
                    write_customers(customers)
                    print("*********************************************************")
                    print(f"Withdrawal successful. New Balance: ${customers[user]['Balance']:.2f}")
                    print("\t\tThanks for the transaction.\t\t")
                    print("********************************")
                    return
                else:
                    print("Incorrect PIN. Withdrawal failed.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

# Function to handle user login
def login():
    print('------------------')
    print("1. Login")
    print("2. Exit")
    print('--------------------')
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        u1 = input("Enter Username: ")
        pwd1 = input("Enter User Password: ")
        if u1 == 'root' and pwd1 == '123':
            print("************************************************************")
            print("Login Successful!")
            print("*************************************************************")
            return True
        else:
            print("Invalid credentials. Please try again.")
            return login()
    else:
        print("Exiting...")
        exit()

# Main function to manage ATM operations
def atm_management_system():
    print("******************************************************************************")
    print("---------------------------| IILM University |-------------------------")
    print("---------------------------| ATM Management System |-------------------")

    if login():
        customers = read_customers()
        user = authenticate_user(customers)

        while True:
            print()
            print("_________________________________________________")
            print(" \n|Options: |")
            print("|***********1. Check Balance ****************| ")
            print("|***********2. Withdraw Money ***************| ")
            print("|***********3. Exit *************************| ")
            print("________________________________")
            print()
            choice = input("Enter your choice: ")

            if choice == '1':
                check_balance(customers, user)
            elif choice == '2':
                withdraw_amount(customers, user)
            elif choice == '3':
                print("*****************************************")
                print("Thank you! Have a nice day!")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    atm_management_system()


                    

                    
    

