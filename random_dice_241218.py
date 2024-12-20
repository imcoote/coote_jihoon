list = []
while True:
    try: 
        first_dice, second_dice, third_dice=map(int,input().split())
    except ValueError:
        continue
    if first_dice < 1 or second_dice < 1 or third_dice < 1 or first_dice > 6 or second_dice > 6 or third_dice > 6 :
            continue
    else:
            break
list.append(first_dice)
list.append(second_dice)
list.append(third_dice)
high_dice = max(list)
if len(list) == 3: 
    if first_dice == second_dice == third_dice:
        print(10000 + first_dice * 1000)
    elif (first_dice == second_dice) and first_dice != third_dice:
        print(1000 + first_dice * 100)
    elif (second_dice == third_dice) and second_dice != first_dice:
        print(1000 + second_dice * 100)
    elif (first_dice == third_dice) and first_dice != second_dice:
        print(1000 + first_dice * 100)
    else: 
        print(high_dice * 100)
else:
    print()
