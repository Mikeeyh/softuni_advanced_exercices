from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gifts = {}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    products_sum = current_material + current_magic

    if products_sum < 100:
        if products_sum % 2 == 0:
            products_sum = ((2 * current_material) + (3 * current_magic))
        else:
            products_sum *= 2
    elif products_sum > 499:
        products_sum /= 2

    if 100 <= products_sum <= 199:
        if 'Gemstone' not in gifts.keys():
            gifts['Gemstone'] = 0
        gifts['Gemstone'] += 1
    elif 200 <= products_sum <= 299:
        if 'Porcelain Sculpture' not in gifts.keys():
            gifts['Porcelain Sculpture'] = 0
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= products_sum <= 399:
        if 'Gold' not in gifts.keys():
            gifts['Gold'] = 0
        gifts['Gold'] += 1
    elif 400 <= products_sum <= 499:
        if 'Diamond Jewellery' not in gifts.keys():
            gifts['Diamond Jewellery'] = 0
        gifts['Diamond Jewellery'] += 1
    else:
        continue

if "Gemstone" in gifts.keys() and 'Porcelain Sculpture' in gifts.keys() or \
        'Gold' in gifts.keys() and 'Diamond Jewellery' in gifts.keys():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

sorted_gifts = sorted(gifts.items(), key=lambda x: x[0])

for gift in sorted_gifts:
    print(f"{gift[0]}: {gift[1]}")

# 105 20 30 25
# 120 60 11 400 10 1
