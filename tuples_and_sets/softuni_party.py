number_of_guests = int(input())
vip = set()
regular = set()

for _ in range(number_of_guests):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip.add(reservation_code)
    else:
        regular.add(reservation_code)

code = input()
while code != 'END':
    if code in vip:
        vip.remove(code)
    else:
        regular.remove(code)
    code = input()

vip = sorted(vip)
regular = sorted(regular)

print(len(vip) + len(regular))
for guest in vip:
    print(guest)
for guest in regular:
    print(guest)

# OR -------------------------------------------------------------

n = int(input())
reservation = set()

for _ in range(n):
    rev_number = input()
    reservation.add(rev_number)

guest = input()
while guest != 'END':
    reservation.remove(guest)

print(len(reservation))

for num in sorted(reservation):
    print(num)

# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END