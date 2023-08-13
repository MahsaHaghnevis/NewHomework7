#
##
### created by yseeva
##  jadval zarb
#    aug 14th

print("how many rows you need?")
n=int(input("ENTER HERE ->"))
print("how many rows you need?")
f=int(input("ENTER HERE ->"))

for i in range(n):
    for m in range(i):
        print(f"{m+1}*{i } = {(m+1)*(i)} ",end="\t")
        if m==f:
            break
        
    print()
