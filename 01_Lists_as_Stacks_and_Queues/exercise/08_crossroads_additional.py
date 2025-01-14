from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_queue = deque()
total_cars_passed = 0

while True:
    command = input()
    if command == "END":
        break
    elif command == "green":
        current_green = green_light_duration

        while cars_queue and current_green > 0:
            current_car = cars_queue.popleft()
            car_length = len(current_car)

            if car_length <= current_green:
                current_green -= car_length
                total_cars_passed += 1
            else:
                remaining_length = car_length - current_green
                current_green = 0

                if remaining_length <= free_window_duration:
                    total_cars_passed += 1
                else:
                    hit_char = current_car[car_length - remaining_length + free_window_duration]
                    print("A crash happened!")
                    print(f"{current_car} was hit at {hit_char}.")
                    exit()
    else:
        cars_queue.append(command)

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")
