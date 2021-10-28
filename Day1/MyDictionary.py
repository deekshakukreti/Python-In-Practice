student_marks = {
		'alpha'  : [20,30,40],
		'beta'  : [70,60,90]
        }
for key in student_marks.keys():    
    if key == 'beta':
        average = (student_marks[key][0] + student_marks[key][1] + student_marks[key][2]) / 3
print('{0:.{1}f}'.format(average, 2))