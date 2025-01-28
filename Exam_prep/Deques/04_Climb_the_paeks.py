from collections import deque

all_the_conquered_peaks = []
food = list(map(int, input().split(", ")))
stamina = deque(map(int, input().split(", ")))
counter = 0

for _ in range(0, 7):
    try_climb = food.pop() + stamina.popleft()

    if try_climb >= 80 and "Vihren" not in all_the_conquered_peaks and counter == 0:
        all_the_conquered_peaks.append("Vihren")
        counter += 1
        continue
    elif try_climb >= 90 and "Kutelo" not in all_the_conquered_peaks and counter == 1:
        all_the_conquered_peaks.append("Kutelo")
        counter += 1
        continue
    elif try_climb >= 100 and "Banski Suhodol" not in all_the_conquered_peaks and counter == 2:
        all_the_conquered_peaks.append("Banski Suhodol")
        counter += 1
        continue
    elif try_climb >= 60 and "Polezhan" not in all_the_conquered_peaks and counter == 3:
        all_the_conquered_peaks.append("Polezhan")
        counter += 1
        continue
    elif try_climb >= 70 and "Kamenitza" not in all_the_conquered_peaks and counter == 4:
        all_the_conquered_peaks.append("Kamenitza")
        counter += 1
        continue

if len(all_the_conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if all_the_conquered_peaks:
    print("Conquered peaks:")

for peak in all_the_conquered_peaks:
    print(peak)
