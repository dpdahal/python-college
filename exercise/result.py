num_of_student = int(input("Enter number of students: "))

increment = 1

student_mark = []

while increment <= num_of_student:
    print(f"======= Student {increment} =======")
    for a in range(1):
        nep = int(input("Enter nep: "))
        eng = int(input("Enter eng: "))
        sic = int(input("Enter sic: "))
        pop = int(input("Enter pop: "))
        mat = int(input("Enter mat: "))
        marks = [nep, eng, sic, pop, mat]
        student_mark.append(marks)
    increment += 1

x = 1
for marks in student_mark:
    total = 0
    for item in marks:
        total += item

    pre = total / 5
    division = ''

    if pre > 35 and pre < 45:
        division += 'pass'
    elif pre > 45 and pre < 60:
        division += 'second'

    elif pre > 60 and pre < 75:
        division += 'first'

    elif pre > 75 and pre < 100:
        division += 'top'
    else:
        division += "next time"

    print(f"Student: {x} Tot: {total} Pre : {pre} Div: {division}")
    x += 1
