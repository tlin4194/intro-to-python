# Demonstrates formatting after the decimal place

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)
print(f"{z:.2f}")
