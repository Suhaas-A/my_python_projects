import random

password = ""

c1 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c2 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c3 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c4 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c5 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c6 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c7 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
c8 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

c9 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c10 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c11 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c12 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c13 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c14 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c15 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
c16 = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

c17 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c18 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c19 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c20 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c21 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c22 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c23 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])
c24 = random.choice(['@', '!', '#', '$', '%', '^', '&', '?'])

sys_pass = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24]
random.shuffle(sys_pass)

for i in range(24):
    password += sys_pass[i]

print('password is : ', password)
