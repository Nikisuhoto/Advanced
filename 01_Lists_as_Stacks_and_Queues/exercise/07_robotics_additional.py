from collections import deque
from datetime import datetime, timedelta

robots_input = input()
start_time = input()

robots = []
for robot_data in robots_input.split(";"):
    name, process_time = robot_data.split("-")
    robots.append({"name": name, "process_time": int(process_time), "available_at": datetime.strptime(start_time, "%H:%M:%S")})

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

current_time = datetime.strptime(start_time, "%H:%M:%S")

while products:

    current_time += timedelta(seconds=1)
    product = products.popleft()

    for robot in robots:
        if current_time >= robot["available_at"]:
            robot["available_at"] = current_time + timedelta(seconds=robot["process_time"])
            print(f"{robot['name']} - {product} [{current_time.strftime('%H:%M:%S')}]")
            break
    else:
        products.append(product)
