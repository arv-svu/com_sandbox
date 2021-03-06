
def list_sum(list1):
    sum=0
    for i in list1:
        sum=sum+i
    return sum

def rec_sum(list1):
    if len(list1)==1:
        return list1[0]
    return list1[0]+rec_sum(list1[1:])

def num_to_basestr(num,base):
    look_up_str="0123456789ABCDEF"
    if num<base:
        return look_up_str[num]
    return num_to_basestr(num//base,base)+look_up_str[num%base]

def rec_str_rev(in_str):
    if len(in_str)==1:
        return in_str[0]
    return rec_str_rev(in_str[1:])+in_str[0]

def rec_min_coins(coin_val_list,change):
    
    min_coins=change
    if change in coin_val_list:
        return 1
    else:
        for i in [c for c in coin_val_list if c<=change]:
            num_coins=1+rec_min_coins(coin_val_list,change-i)
            if num_coins<min_coins:
                min_coins=num_coins
    return min_coins
   
    



list1=[1,3,5,7,9]
print("for loop sum")
print(list_sum(list1))
print("recursion sum")
print(rec_sum(list1))
print("recursion number to base string")
print(num_to_basestr(10,2))
print("recursion reverse string")
print(rec_str_rev("ashok"))
print("recursion min coins")
print(rec_min_coins([1,5,10,25],63))
