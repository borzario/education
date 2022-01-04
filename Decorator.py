def decor(func):
    def vnut(num):
        print('***')
        func(num)
        print("***\nEND OF PAGE")
    return vnut

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input());