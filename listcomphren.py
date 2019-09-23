num_of_items=int(input("Enter the no of items "))
inventory = {}

def display_inventory(num_of_items):

    for i in range(num_of_items):
        name = input("Enter the name of items ")
        values = int(input("Enter the value of item "))
        inventory[name] = values
        # print(inventory.values())
        for name,values in inventory.items():
            print(f"{name} {values}")
        total_items=sum(inventory.values())
    print("total number of items are ",total_items)

display_inventory (num_of_items)





