ice = input("do you know ice number c? ")
if ice == "yes":
    print("ok!")
ice_c = float(input("give an ice number c: "))
price = float(input("give a price number: " ))
variable = input("do you know variable_c? ")
if variable == "yes":
    print("ok")
    variable_c=float(input("give a viariable c: "))
elif variable == "no":
    print("you don't know variable c. ")
    quan = input("do you know quantility? ")
    if quan == "yes":
        print("ok")
        quan_value = float(input("give a quantility number: "))
        if quan_value == quan_value < 0 or quan_value > 0 or quan_value == 0:
            vone = input ("do you know variable one? ")
            if vone == "yes":
                vone_value = float(input("give a variable one number: "))
                if vone_value == vone_value > 0 or vone_value < 0 or vone_value == 0:
                    variable_c = quan_value * vone_value
                    print ("variable_c:" , vone_value * quan_value)
                else:
                    print ("failed") 
break_even = ice_c / price - variable_c
print("break one:" , break_even)
