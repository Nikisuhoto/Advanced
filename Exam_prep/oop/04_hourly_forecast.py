def forecast(*args):
    final_result = ""
    weather_priority = {"Sunny": 1, "Cloudy": 2, "Rainy": 3}
    weather_dict = {}
    for i in range(len(args)):
        town = args[i][0]
        weather = args[i][1]

        weather_dict[town] = weather

    result = sorted(weather_dict.items(), key=lambda kv: (weather_priority[kv[1]], kv[0]))

    for i in range(len(result)):
        final_result += f"{result[i][0]} - {result[i][1]}\n"

    return final_result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
