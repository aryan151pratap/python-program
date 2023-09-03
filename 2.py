a=float(input("enter value of Celcius : "))
f=(9/5)*a+32
print("Fahrenheit : ",f)
k=273.15+a
print("Kelvin : ",k)

b=float(input("enter value of Fahrenheit : "))
print("celcius : ",(b-32)*5/9)
print("kelvin : ",(b-32)*5/9+273.15)

c=float(input("enter value of kelvin : "))
print("celcius : ",c-273.15)
print("fahrenheit : ",9/5*(c-273.15)+32)
