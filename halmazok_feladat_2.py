reggeli = {"vaj","tea","pirítós"}
ebed = set()
ebed = set(["halászlé","kenyér",True,True])
print(type(ebed))
print(ebed)

reggeli.add("víz")
reggeli.discard("körte")
print(reggeli)

ebed = {"víz","halászlé","kenyér"}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

gyumolcskosar = ["eper","alma","szilva","eper"]
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)