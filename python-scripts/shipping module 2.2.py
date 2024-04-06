#we establish the general outline of cost for weight
#0-2 lb cost $1.25 per lb
#2-6 lb $4.00 per lb
#6-10 lb $5.00 per lb
#anything over 10 lbs $7.00 per lb

#if a customer's order defined by weight, is 8 lb
order_weight = 1

if order_weight <= 2:
    ship_cost = order_weight * 1.25
elif order_weight <= 6:
    ship_cost = order_weight * 4.00
elif order_weight <= 10:
    ship_cost = order_weight * 5.00
else:
    ship_cost = order_weight * 7.00

print('Shipping total $' + format(ship_cost, '.2f') )

#one of the calculations above will fire depending on the order's weight, in this case 8lbs
#our order's weight would fire calulation elif order_weight <= 10
#ship_cost = 8 * 5.00 
#which would print Shipping total $40.00