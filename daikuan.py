
year = 19
month =year * 12

total = 1052118.75 #1200000.00
balance =total

rate =0.0325

monthRate = rate/12

huankuan =10000
allinterest =0

print(month)
print(monthRate)

def cal(balance,monthRate_this,huankuan):
    interest =  balance * monthRate_this
    global allinterest
    allinterest = allinterest+interest
    print(interest,balance)

    balance =balance - (huankuan - interest)
    return balance

n=37
while  n<= month:
    print(n)
    balance = cal(balance,monthRate,huankuan)
    n=n+1
    if balance<0:
        break

print(allinterest)
