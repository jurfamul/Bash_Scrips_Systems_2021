#!/user/bin/python3
gradeDict = {"phred": 88.7774, "Aeva": 95.4443, "Ralphie": 65.00}
print(gradeDict)
grade = gradeDict['Aeva']
print("Aeva's grade is: {:.2f}".format(grade))
gradeDict["Leon"] = 55.5555
print(gradeDict)
