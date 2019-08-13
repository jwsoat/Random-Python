hello = 1
cont = "yes"
while cont == "yes":
    print("hello for the {} time".format(hello))
    cont = input("continue? ")
    if cont == "yes":
        hello += 1
    else:
        askcont= input("Are you Sure?" )
        if askcont == "yes":
            print("ok")
            cont = "no"
        if askcont == "no":
            hello +=1

