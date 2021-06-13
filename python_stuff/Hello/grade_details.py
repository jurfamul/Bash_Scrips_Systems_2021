#!/user/bin/python3
import sys
fileName = "pretend_data.csv"
gradebook = {}
totalGrade = 0.0
countStudents = 0
maxGrade = 0
maxGName = ""
minGrade = 100
minGName = ""
with open(fileName, 'r') as inFile:
    for line in inFile:
        student = line.split(',')
        countStudents = countStudents + 1
        studentGrade = float(student[1])
        totalGrade = totalGrade + studentGrade

        if studentGrade >= maxGrade:
            maxGrade = studentGrade
            maxGName = student[0]

        if studentGrade < minGrade:
            minGrade = studentGrade
            minGName = student[0]

avgGrade = totalGrade / countStudents
fileName = "grade_details.txt"
outputTxt = ["The average grade is: {0}.\n".format(avgGrade),
             "{0} has the highest grade in the class with {1}.\n".format(maxGName, maxGrade),
             "{0} has the lowest grade in the class with {1}.\n".format(minGName, minGrade)]

with open(fileName, 'w') as outFile:
    for line in outputTxt:
        outFile.write(line)
        sys.stdout.write(line)
