#def strcounter(s: str):
#    for symbol in set(s):
#        counter = 0
#        for sub_sumbol in s:
#            if symbol == sub_sumbol:
#                counter += 1
#                print(symbol, counter)

def strcounter(s: str):
    symvols_disk = {}
    for symvol in s:
        if symvol in symvols_disk:
            symvols_disk[symvol] += 1
        else:
            symvols_disk[symvol] = 1
    print(symvols_disk)
strcounter("бурааан")