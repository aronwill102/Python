
CP = 729.31
BuyQty = 475
SP = 835.00
SellQty = 306
FinChrg = 4.6
ExtWarrQty = 41
ExtWarrRate = 59.99

print('Cost of computer')
print(BuyQty*CP)

print('finance charges ')
print(BuyQty*CP*FinChrg/100)

print('Total cost ')
print(BuyQty*CP+BuyQty*CP*FinChrg/100)

print('Sales Total')
print(SellQty*SP)

print('Warranty Sales ')
print(ExtWarrRate*ExtWarrQty)

print('Total Sales')
print(SellQty*SP+ExtWarrRate*ExtWarrQty)

print('Total Loss')
print(SellQty*SP+ExtWarrRate*ExtWarrQty-BuyQty*CP+BuyQty*CP*FinChrg/100)
