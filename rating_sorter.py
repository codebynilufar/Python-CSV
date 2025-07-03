import csv
with open("students.csv",  newline="") as f:
    students = list(csv.DictReader(f))
    students.sort(key=lambda x: int(x["score"]), reverse=True)


with open("rating.csv", "w", newline="") as f2:
    fieldnames = ["name", "score"]

    writer = csv.DictWriter(f2, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(students)





       
