hello = 1
cont = "yes"
while cont == "yes":
    print("hello for the {} time".format(hello))
    cont = input("continue? ")
    if cont == "yes":
        hello += 1
    elif cont == "y":
        hello += 1
    elif cont == "no":
        break


