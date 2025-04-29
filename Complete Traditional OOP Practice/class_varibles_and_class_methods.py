# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name="Meezan Bank"

    def __init__(self,customer_name):
        self.customer_name=customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Customer: {self.customer_name}")
        print(f"Bank Name: {self.bank_name}")

b1 = Bank("Habib Bank")
b2 = Bank("Bank Islami")
b1.show_details()
b2.show_details()
print("\nChanging bank name...\n")
Bank.change_bank_name("Meezan Bank")
b1.show_details()
b2.show_details()

