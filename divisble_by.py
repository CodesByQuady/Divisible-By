#Create a program that asks the user for a number and then prints out a list of all divisors of that number.

x = int(input('Enter A Number: '))
def divisible_by(x):
    y = range(1, (x +  1))
    z = []
    for i in y:
        if x % i == 0:
            z.append(i)
    print(z)

divisible_by(x)
