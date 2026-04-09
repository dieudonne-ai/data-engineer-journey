import csv

def weather_score(humidity):
    if humidity is None:
        return "N/A"
    elif 0 <= humidity <= 30:
        return "Low"
    elif 31 <= humidity <= 60:
        return "Moderate"
    elif 61 <= humidity <= 100:
        return "High"
    else:
        return "Invalid"

def read_weather_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        weather_data = list(reader)

    for entry in weather_data:
        try:
            entry["humidity"] = int(entry["humidity"])
        except ValueError:
            entry["humidity"] = None
        
        entry["weather_score"] = weather_score(entry["humidity"])

    return weather_data

def clean_weather_data(file_path):
    weather_data = read_weather_data(file_path)
    generate_report(weather_data)
    save_weather_data(weather_data, "clean_data/weather_cleaned.csv")

with open("data/weather.csv", "r") as file:
    reader = csv.reader(file)

#to i learn how to read csv file using csv.reader() method, and to catch the error if the value in the score column is not an integer, we can use a try-except block to handle the ValueError that may occur when trying to convert the value to an integer. Here's how you can do it:      
    for row in reader:
        print(row)
    try:
        humidity = int(row["humidity"])
    except ValueError:
        print("Invalid humidity value:", row["humidity"])

def generate_report(weather_data):
    print("=== WEATHER REPORT ===")
    for entry in weather_data:
        print(f"{entry['date']} - Humidity: {entry['humidity']} - Weather Score: {entry['weather_score']}")

def save_weather_data(weather_data, output_file):
    with open(output_file, "w", newline="") as file:
        fieldnames = ["date", "humidity", "weather_score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(weather_data)

if __name__ == "__main__":
    clean_weather_data("data/weather.csv")