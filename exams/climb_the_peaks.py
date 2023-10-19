from collections import deque

food_portions = [int(x) for x in input().split(', ')]
stamina_quantities = deque([int(x) for x in input().split(', ')])

peaks = [
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70)]

peaks_conquered = []
peak_index = 0

for _ in range(7):
    current_day_food = food_portions.pop()
    current_day_stamina = stamina_quantities.popleft()
    current_sum = current_day_food + current_day_stamina

    if current_sum >= peaks[peak_index][1]:
        peaks_conquered.append(peaks[peak_index][0])
        peak_index += 1

    if len(peaks_conquered) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks_conquered:
    print("Conquered peaks:")
    [print(peak) for peak in peaks_conquered]

# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2
