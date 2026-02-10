s={2,3,5,7,7,5,8,4,2,6}
print(s)
#set mai ek element agr repeat ho rha ho toh wo ek hi baar print hota hai
#sets are immutable
for i in s:
    print(i)

s2={2,434,35,5,3,6,7,8,889,7,4}
print(s.union(s2))

#s1.update(s2) se s1 mai s2 ki values add ho jaengi
#.union ke jese .intersection bhi juse kr skte hai
#.symmetric_difference
#.difference
#.isdisjoint
#.issuperset
#.issubset
#.add
#.remove
#.discard
#.pop - selects a random element from the set 
#.del mai pura set deleteho jaega 
#.clear mai set delete nhi hoga but saari values delete ho jaengi 

