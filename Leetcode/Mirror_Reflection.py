def mirrorReflection(self, p, q):
    while p % 2 == 0 and q % 2 == 0:
        p, q = p / 2, q / 2
    return 1 - p % 2 + q % 2


p, q = 3, 2
p, q = 3, 1
while p % 2 == 0 and q % 2 == 0:
    p, q = p / 2, q / 2
out = 1 - p % 2 + q % 2
