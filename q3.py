#
##
### created by yseeva
##  list user
#    aug 14th

def getter():
    n=int(input("how many objectsyou have? "))
    arr=[]
    for i in range(n): 
        whatever=int(input(f"enter object {i+1} = "))
        arr.append(whatever)
    return arr
        
def is_sorted(lst):
    n = len(lst)
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            return False
        else:
            i+=1
    return True

while True:
    option=int(input("you wanna enter again?  enter 0 to stop and any other key to continue"))
    if option==0:
        print("hope tp see u again")
        break
    else:
        if is_sorted(getter()):
            print("YES it is sorted from low to high !")
        else:
            print("IT IS NOT SORTED ")
        
        