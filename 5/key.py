periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

# 新しいキーと値の挿入(更新はない)
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)

print(periodic_table)

from collections import defaultdict
# 存在しないキーに対する値はintの0
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1

print(periodic_table)
periodic_table['Lead']
print(periodic_table)


# カウンタ
food_counter = defaultdict(int)
for food in ['spam','spam','eggs','spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)