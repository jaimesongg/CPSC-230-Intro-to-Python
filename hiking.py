pockets = []
backpack = []
pocket_max = 4
backpack_max = 20

def storage_check(mypocket, mybackpack, item):
    if len(mypocket) == pocket_max:
        print("Pocket is full, adding to backpack")
        if(len(backpack) == backpack_max):
            print("Backpack is full")
        

        else:
            print(f"adding {item} to backpack")
            mybackpack.append(item)
            print("backpack items:", mybackpack)

    else:
        print(f"adding {item} to pocket")
        mypocket.append(item)
        print("pocket items:", mypocket)

    item_remove = input("Choose an item to remove from your backpack: ")
    while True:
        if item_remove in backpack:
            mybackpack.remove(item_remove)
            break
        item_remove = input("Enter a valid item to remove: ")
    print ("Your backpack now has this:", mybackpack)

storage_check(pockets,backpack, 'flashlight')
storage_check(pockets,backpack, 'water')
storage_check(pockets,backpack, 'food')
storage_check(pockets,backpack, 'sleeping bag')
storage_check(pockets,backpack, 'tent')
storage_check(pockets,backpack, 'shoes')
storage_check(pockets,backpack, 'pillow')




