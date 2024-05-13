from functions import *

menu: str = f"""
{"*" * 30}
[w] Withdraw 
[d] Deposit
[e] Extract
[q] Quit
{"*" * 30}
"""

balance: float = 1500.00
limit: float = 500.00
extract: str = ""
withdrawals_number: int = 0
WITHDRAWALS_LIMIT: int  = 3

while True:

    option = input(menu)

    match option:

        case "w":
            if withdrawals_number > WITHDRAWALS_LIMIT:
                print("\nwithdrawal limit exceeded!")
            else:
                withdraw(balance,limit,extract,withdrawals_number)
            