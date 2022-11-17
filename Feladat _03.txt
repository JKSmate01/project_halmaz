out = open("H:\out.txt","w")
halmaz = {}
halmaz.clear()
halmaz = {"a","b","c",13}
halmaz2 = halmaz.copy()
print(halmaz)
print(halmaz2)
out.write(f"{halmaz}\n")
out.write(f"{halmaz2}\n")
halmaz3 = {2,5,4,1}
halmaz4 = {2,6,5,7}
#3
print(halmaz3.difference(halmaz4))
out.write(f"{halmaz3.difference(halmaz4)}\n")
#4
halmaz3 = {2,5,4,1}
halmaz4 = {2,6,5,7}
mind_kettoben = halmaz3.difference_update(halmaz4)
print(mind_kettoben)
out.write(f"{mind_kettoben}\n")
#5
halmaz3 = {2,5,4,1}
halmaz4 = {2,6,5,7}
print(halmaz3.intersection(halmaz4))
out.write(f"{halmaz3.intersection(halmaz4)}\n")
#6
halmaz3 = {2,5,4,1}
halmaz4 = {2,6,5,7}
nem_szerepelnek = halmaz3.intersection_update(halmaz4)
print(nem_szerepelnek)
out.write(f"{nem_szerepelnek}\n")
#7 Megadja hogy van-e bennük egyező érték(True)
halmaz3 = {2,5,4,1}
halmaz4 = {2,6,5,7}
print(halmaz3.isdisjoint(halmaz4))
out.write(f"{halmaz3.isdisjoint(halmaz4)}\n")
#8 Az értéke True lesz ha a halmaz3 minden eleme megvan a halmaz4-ben.
halmaz3 = {2,5}
halmaz4 = {2,6,5,7}
print(halmaz3.issubset(halmaz4))
out.write(f"{halmaz3.issubset(halmaz4)}\n")
#9 Az értéke True lesz ha a halmaz4 minden eleme megvan a halmaz3-ban is.
halmaz3 = {2,5,6,7}
halmaz4 = {2,5}
print(halmaz3.issuperset(halmaz4))
out.write(f"{halmaz3.issuperset(halmaz4)}\n")
#10 Ki írja a két halmaz értékeit kivéve az egyezőeket.
halmaz3 = {2,5,6,7}
halmaz4 = {2,5,4}
print(halmaz3.symmetric_difference(halmaz4))
out.write(f"{halmaz3.symmetric_difference(halmaz4)}\n")
#11 
halmaz = {1,2,3}
halmaz.add(4) #Hozzá tesz a halmazhoz.
print(halmaz)
out.write(f"{halmaz}\n")
halmaz.pop() #Kivesz a halmazból egy meg nem határozott elemet.
print(halmaz)
out.write(f"{halmaz}\n")
halmaz3 = {2,5,6,7}
halmaz4 = {2,5,4}
egyutt = halmaz3.union(halmaz4)
print(egyutt)
out.write(f"{egyutt}\n")
out.close()
