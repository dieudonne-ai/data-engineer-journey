import csv

with open("data/students.csv","r") as file:
	reader = csv.DictReader(file)

	for row in reader:
		print(row)

	try:
		score = int(row["score"])
	except ValueError:
		print("Invalid score value:", row["score"])