import os
from datetime import datetime

# User Data Storage
users = {
    "Admin": {"password": "1234", "balance": 1000, "is_admin": True},
    "User1": {"password": "5678", "balance": 1000, "is_admin": False},
    "User2": {"password": "9012", "balance": 1000, "is_admin": False},
}

# Receipt generation helper function
def generate_receipt(username, action, details):
    """
    Creates a receipt file with the action details.
    The file is named with the username and a timestamp for uniqueness.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"receipt_{username}_{timestamp}.txt"
    content = (
        "=============================\n"
        "     Python Bank Receipt     \n"
        "=============================\n"
        f"Date & Time: {timestamp}\n"
        f"User: {username}\n"
        f"Action: {action}\n"
        "-----------------------------\n"
        f"Details: {details}\n"
        "=============================\n"
    )
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"💾 Receipt saved as '{filename}'")
    except Exception as e:
        print(f"❌ Failed to save receipt: {e}")

# Menu display functions
def login_menu():
    print("1. Login")
    print("2. Exit")

def user_menu():
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Change Password")
    print("5. Logout")

def admin_menu():
    print("\nAdmin Menu:")
    print("1. View Users")
    print("2. Delete User")
    print("3. Change Password")
    print("4. Logout")

# Banking interface for standard users
def banking(username):
    while True:
        print(f"\nWelcome, {username}!")
        user_menu()
        choice = input("Select an option: ")

        if choice == "1":  # Withdraw
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount > users[username]["balance"]:
                    print("❌ Insufficient Balance!")
                else:
                    users[username]["balance"] -= amount
                    print(f"✅ Withdrawal Successful! Remaining Balance: {users[username]['balance']}")
                    details = f"Withdrawn: {amount}. New Balance: {users[username]['balance']}."
                    generate_receipt(username, "Withdrawal", details)
            except ValueError:
                print("❌ Please enter a valid integer amount.")

        elif choice == "2":  # Deposit
            try:
                amount = int(input("Enter amount to deposit: "))
                users[username]["balance"] += amount
                print(f"✅ Deposit Successful! Updated Balance: {users[username]['balance']}")
                details = f"Deposited: {amount}. New Balance: {users[username]['balance']}."
                generate_receipt(username, "Deposit", details)
            except ValueError:
                print("❌ Please enter a valid integer amount.")

        elif choice == "3":  # Check Balance
            print(f"💰 Current Balance: {users[username]['balance']}")

        elif choice == "4":  # Change Password
            new_password = input("Enter new password: ")
            users[username]["password"] = new_password
            print("🔑 Password changed successfully!")
            details = "Password updated successfully."
            generate_receipt(username, "Change Password", details)

        elif choice == "5":  # Logout
            print("🔒 Logging out...")
            break

        else:
            print("❌ Invalid option. Try again.")

# Admin interface for privileged users
def admin_panel():
    while True:
        print("\n🔹 Admin Panel 🔹")
        admin_menu()
        choice = input("Select an option: ")

        if choice == "1":  # View Users
            print("\n📜 Registered Users:")
            for user in users:
                if user != "Admin":
                    print(f"➡ {user}")

        elif choice == "2":  # Delete User
            del_user = input("Enter username to delete: ")
            if del_user in users and not users[del_user]["is_admin"]:
                del users[del_user]
                print(f"🗑️ User {del_user} deleted successfully!")
                details = f"Deleted user: {del_user}."
                generate_receipt("Admin", "Delete User", details)
            else:
                print("❌ Invalid username or cannot delete Admin!")

        elif choice == "3":  # Change Admin Password
            new_password = input("Enter new admin password: ")
            users["Admin"]["password"] = new_password
            print("🔑 Admin password changed successfully!")
            details = "Admin password updated successfully."
            generate_receipt("Admin", "Change Password", details)

        elif choice == "4":  # Logout
            print("🔒 Logging out from Admin Panel...")
            break

        else:
            print("❌ Invalid option. Try again.")

# Main login function
def login():
    while True:
        print("\n🔷 Welcome to Python Bank 🔷")
        login_menu()
        option = input("Select an option: ")

        if option == "1":  # Login
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in users and users[username]["password"] == password:
                print("\n✅ Login Successful!")
                if users[username]["is_admin"]:
                    admin_panel()
                else:
                    banking(username)
            else:
                print("❌ Incorrect username or password!")

        elif option == "2":  # Exit
            print("👋 Exiting... Thank you for using Python Bank!")
            break

        else:
            print("❌ Invalid option. Try again.")

# Start the banking system
if __name__ == "__main__":
    login()
