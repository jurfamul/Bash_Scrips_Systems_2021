#!/user/bin/python3
import sys
import json
import pprint as pp
inFileName = "grades.json"

with open(inFileName, 'r') as json_inFile:
    input_data = json.load(json_inFile)

for student in input_data["students"]:
    totalGrade = 0.0
    assignmentCount = 0

    for assignment in student["grades"]:
        assignmentCount = assignmentCount + 1
        totalGrade = totalGrade + assignment["assn{0}".format(assignmentCount)]

    avgGrade = totalGrade / assignmentCount
    student["grade_avg"] = avgGrade

outFileName = "grades_with_avg.json"

with open(outFileName, 'w') as outFile:
    json.dump(input_data, outFile)

