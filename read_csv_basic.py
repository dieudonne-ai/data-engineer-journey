import csv

with open("data/weather.csv", "r") as file:
    reader = csv.reader(file)

#to i learn how to read csv file using csv.reader() method, and to catch the error if the value in the score column is not an integer, we can use a try-except block to handle the ValueError that may occur when trying to convert the value to an integer. Here's how you can do it:      
    for row in reader:
        print(row)
    try:
        humidity = int(row["humidity"])
    except ValueError:
        print("Invalid humidity value:", row["humidity"])