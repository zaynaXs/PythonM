#print(float(input("What is x? ")) + float(input("What is y?" )))


x = float(input("What is x? "))
y = float(input("What is y?" ))

z = x + y

#z = round(x + y[, 2]) not correct, gives an error y

print(f"{z:,}")