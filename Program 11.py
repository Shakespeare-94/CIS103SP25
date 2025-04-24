import datetime

def v_p(points):
    try:
        points = int(points)
    except:
        return 'Points cannot be letters'
    
    if points < 0:
        return 'Points cannot be negative'
    
    if points > 1000:
        return 'Points cannot exceed 1000'
    
    return True

def c_g(points):
    if points >= 900:
        return 'A'
    elif points >= 800:
        return 'B'
    elif points >= 700:
        return 'C'
    elif points >= 600:
        return 'D'
    else:
        return 'F'

def main():
    print('Program started at: ' + str(datetime.datetime.now()))

    pointsfile = 'c:/CIS103/points.txt'
    gradesfile = 'c:/CIS103/grades.txt'
    errorsfile = 'c:/CIS103/errors.txt'

    try:
        filepnts = open(pointsfile, 'r')
        filegrdes = open(gradesfile, 'w')
        fileerrs = open(errorsfile, 'w')
    except:
        print("Error opening one of the files.")
        return

    records_read = 0
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    graded_records = 0
    error_records = 0

    line1 = filepnts.readline()
    while line1 != '':
        line1 = line1.strip()

        student_id, name, points = line1.split(',')

        v_r = v_p(points)
        if v_r == True:
            grade = c_g(int(points))
            graded_records = graded_records + 1

            if grade == 'A':
                a_count = a_count + 1
            elif grade == 'B':
                b_count = b_count + 1
            elif grade == 'C':
                c_count = c_count + 1
            elif grade == 'D':
                d_count = d_count + 1
            elif grade == 'F':
                f_count = f_count + 1

            grade_record = student_id + ',' + name + ',' + points + ',' + grade
            filegrdes.write(grade_record + '\n')
        else:
            error_record = student_id + ',' +  name + ',' + points + ',' + v_r
            fileerrs.write(error_record + '\n')
            error_records = error_records + 1

        records_read = records_read + 1
        line1 = filepnts.readline()

    filepnts.close()
    filegrdes.close()
    fileerrs.close()

    print('\nResults:')
    print('--------')
    print('Records Read: ' + str(records_read))
    print('Graded Records: ' + str(graded_records))
    print('Error Records: ' + str(error_records))
    print("A's: " + str(a_count))
    print("B's: " + str(b_count))
    print("C's: " + str(c_count))
    print("D's: " + str(d_count))
    print("F's: " + str(f_count))

    print('\nProgram ended at: ' + str(datetime.datetime.now()))

main()
