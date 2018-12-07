from colorama import init
init()

from colorama import Fore, Back, Style

# Variables

# Stores Colorama methods to appropriate hex values
colors_dict = {
    Fore.RED    : (0xFF0000, 0x8B0000),
    Fore.GREEN  : (0x008000, 0x006400, 0x9ACD32),
    Fore.WHITE  : (0xFFFFFF),
    Fore.YELLOW : (0xFFFF00),
    Fore.BLACK + Back.WHITE : (0xC0C0C0) # Silver
    }

colors_list = []

###

# appends all colors_dict values into colors_list to sort
for value in colors_dict.values():

    # iterable values are unpacked then appended
    if hasattr(value, '__iter__') is True:
        for iter_val in value:
            colors_list.append(iter_val)
    # non iterable values (where the key has one value) are appended as is
    else:
        colors_list.append(value)

colors_list.sort()
#for item in colors_list: print(hex(item))

# 1. compares colors_list items to colors_dict values, one at a time
# 2. when item and a value match, terminal output is colored hex of the item

for item in colors_list:
    for key in colors_dict:
        #print('Item: '+str(hex(item)))
        # if the colors_dict value is iterable
        if hasattr(colors_dict[key], '__iter__') is True and item in colors_dict[key]:
            print(key + hex(item))
        elif item == colors_dict[key]:
            print(key + str(hex(item)))
        else:
            continue
        print(Style.RESET_ALL, end='')
