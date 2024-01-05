dice = int(input('Please enter the number of dice : '))
sign = input('Please enter the sign of criteria : ')
criteria = int(input('Please enter the criteria number : '))

favourable_outcomes = 0

number_list = [1, 2, 3, 4, 5, 6]

z = 6

if dice == 1:
    number_list = [1, 2, 3, 4, 5, 6]

elif dice > 1:
    dice = dice - 1
    for x in range(dice):
        for i in range(6):
            for y in range(z):
                add = number_list[y] + (i + 1)
                number_list.append(add)
            y = 0
        i = 0
        del number_list[0:z]
        z = z * 6

if sign == ">":
    for a in number_list:
        if a > criteria:
            favourable_outcomes += 1

if sign == "=":
    for a in number_list:
        if a == criteria:
            favourable_outcomes += 1

if sign == "<":
    for b in number_list:
        if b < criteria:
            favourable_outcomes += 1

print('')
print('')
print('Probability in fraction is : ', favourable_outcomes, "/", z)
print('Probability in percentage is : ', (favourable_outcomes / z * 100), '%')
