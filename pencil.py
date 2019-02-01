import random

header = "P3\n500 500\n255\n"
f = open("cooza.ppm", "w")
total = header
for i in range(0,500):
    line = ""
    for j in range(0,500):
        line += "{} {} {} ".format((j+random.randrange(100))%256, (j-random.randrange(100))%256, (j*random.randrange(100))%256)
    total += line + "\n"

f.write(total)
