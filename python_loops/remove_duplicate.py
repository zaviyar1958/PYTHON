li = [1,2,3,4,5,5,6,2,1]
uniq_li = []
seen = set()
for item in li: 
    if item not in seen: 
        uniq_li.append(item)
        seen.add(item)
print(f"Unique list is: {uniq_li}")
