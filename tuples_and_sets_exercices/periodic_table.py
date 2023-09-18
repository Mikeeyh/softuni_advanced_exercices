n = int(input())
chemical_compounds = set()

for _ in range(n):
    chemical_compound = input().split()
    for current_chemical_compound in range(len(chemical_compound)):
        chemical_compounds.add(chemical_compound[current_chemical_compound])

for chemical in chemical_compounds:
    print(chemical)

# OR -------------------------------------------------------------------

n = int(input())
chemicals = set()

for _ in range(n):
    chemical_compound = input().split()
    for element in chemical_compound:
        chemicals.add(element)

print(*chemicals, sep='\n')

# 4
# Ce O
# Mo O Ce
# Ee
# Mo