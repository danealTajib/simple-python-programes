print("if you don't need anythings then press 0")
#-------------------variable declaration------------------
items_list=[]
qty_list=[]
unit_cost_list=[]
tota_cost_list=[]
sum=0.0
item=''
qty=0
unit_cost=0.0
total_cost=0.0
i=0
payment=0.0
#-----------------input section--------------
while True:
    item=input('item name :')
    if item=='0':
        break
    qty=int(input('item qty :'))
    unit_cost=float(input('unit cost'))
 #-------------processing part--------------
    items_list.append(item)
    qty_list.append(qty)
    unit_cost_list.append(unit_cost)
    total_cost=qty*unit_cost
    tota_cost_list.append(total_cost)
    sum = sum+total_cost
    print('\n')
#--------------output part---------------
for i in range(len(items_list)):
    print(f"item name:{items_list[i]} ")
    print(f"item qty:{qty_list[i]}")
    print(f"unit price:{unit_cost_list[i]}")
    print(f"total price{tota_cost_list[i]}")
    print('\n')
print(f'total bill :{sum}\n')
#----------input payment--------------------
payment=float(input(f'your bill :{sum} payment please..:'))
#----------output payment------------------
if payment>=sum:
    print(f'change : {payment-sum}')
else:
    print(f'due {sum-payment}')
print('..............thank you for shopping...............')



