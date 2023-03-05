class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    # display of printed class object:
    def __repr__(self):
        title_line = "*" * int((30 - len(self.category)) / 2) + self.category + "*" * int((30 - len(self.category)) / 2) + "\n"
        ledger = ""
        for item in self.ledger:
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.get_balance())
        return title_line + ledger + total

    def deposit(self, amount, description=False):
        if description:
            ledger_element = {"amount": amount, "description": description}
            self.ledger.append(ledger_element)
        else:
            ledger_element = {"amount": amount, "description": ""}
            self.ledger.append(ledger_element)

    def withdraw(self, amount, description=False):
        if self.check_funds(amount):
            if description:
                ledger_element = {"amount": -1 * amount, "description": description}
                self.ledger.append(ledger_element)
            else:
                ledger_element = {"amount": -1 * amount, "description": ""}
                self.ledger.append(ledger_element)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, another_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + another_category.category)
            another_category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    spend = []
    for category in categories:
        temp = 0
        for item in category.ledger:
            if item['amount'] < 0:
                temp += abs(item['amount'])
        spend.append(temp)

    total = sum(spend)
    percentage = [i / total * 100 for i in spend]

    s = "Percentage spent by category"
    for i in range(100, -1, -10):
        s += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i:
                s += " o "
            else:
                s += "   "
        s += " "
    s += "\n    ----------"

    cat_length = []
    for category in categories:
        cat_length.append(len(category.category))
    max_length = max(cat_length)

    for i in range(max_length):
        s += "\n    "
        for j in range(len(categories)):
            if i < cat_length[j]:
                s += " " + categories[j].category[i] + " "
            else:
                s += "   "
        s += " "

    return s
