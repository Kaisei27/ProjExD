import random
import datetime

a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
b = [i for i in range(len(a))]
c = random.choice(b)
d = str(random.sample(a,c))
print("対象文字は : " + str(d))

e = random.sample((a),2)
print("欠損文字は : " + str(e))
f = []
for a in b:
    if a == b:
        pass
    if a != b:
        f += 1
print("表示文字は : " + str(f) )

