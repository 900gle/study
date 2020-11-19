num = 1
high = 60
bounce = 0.6
while num <= 10:
    print(num, round(high, 4))
    high = high * bounce
    num += 1
