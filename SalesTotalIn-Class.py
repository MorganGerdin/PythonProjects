# Morgan Gerdin
# Sales total in-class
# due: 2/4/2022
RATE = .07    # declare tax rate


def main():
    Item1 = float(input("what is the price of item 1?"))     # get three prices
    Item2 = float(input("what is the price of item 2?"))
    Item3 = float(input("what is the price of item 3?"))
    Subtotal = Item1 + Item2 + Item3      # get subtotal
    SalesTax = tax(Subtotal)
    print(f"the subtotal is {Subtotal: .2f}")
    print(f"the sales tax is {SalesTax: .2f}")
    print(f"the Total is {Subtotal + SalesTax: .2f}")


def tax(Sub):
    return Sub * RATE

# call main 
main()