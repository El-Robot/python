f = open('testcase.txt', 'w')
n = 10

for i in range(n - 2):
    f.write("1")
    f.write("0")
    for j in range(n - 2):
        f.write("1")
    f.write("\n")

f.write("1")
for j in range(n - 1):
        f.write("0")

f.write("\n")

for z in range(n):
        f.write("1")

f.write("\n")
