# Helper function to write the insert 
def write_to_file(db, values):
    insert = "INSERT INTO " + db + " VALUES ("
    for val in values: 
        try:
            val = int(val)
            insert += str(val) + ", "
        except:
            insert += "'" + val + "'" + ", "

    insert = insert[ : len(insert) - 2] # trim off last comma
    insert += ");"
    out_db.write(insert + "\n")

    
raw_db = open("enrollment_raw.txt", "r")
out_db = open("sql_insertions.txt", "w")

fst = raw_db.readline()
snd = raw_db.readline()

if "-" not in snd:
    print("Invalid file structure!")
    exit()

attributes = []
while ',' in fst:
    attributes.append(fst[ : fst.index(',')])
    fst = fst[ fst.index(',') + 1 : ]
attributes.append(fst[ : len(fst) - 1])

all_course = []
all_dept = []
all_enroll = []
all_major = []
all_student = []
all_primary_keys = []

for line in raw_db:
    values = []
    while ',' in line:
        atom = line[0:line.index(',')]
        values.append(atom)
        line = line[line.index(',')+1:]
    values.append(atom)

    if len(values) != len(attributes):
        print("Error parsing file!")
        exit()

    # check for "student" values
    student = []
    for i in range(4):
        if len(values[i]) == 0: break
        if i == 0: # studentID is a primary key
            all_primary_keys.append(values[i])
        # corrections for check
        if i == 2: 
            if "F" in values[i] and values[i] != "Freshman": 
                values[i] = "Freshman"
            elif "SO" in values[i] and values[i] != "Sophomore": 
                values[i] = "Sophomore"
            elif "J" in values[i] and values[i] != "Junior": 
                values[i] = "Junior"
            elif "SR" in values[i] and values[i] != "Senior": 
                values[i] = "Senior"
        if i == 3 and values[i] < "0.0": values[i] = "0.0"
        if i == 3 and values[i] > "4.0": values[i] = "4.0"
        student.append(values[i])
    if len(student) == 4: all_student.append(student)

    # check for "Dept" values
    dept = []
    if len(values[6]) != 0: # get deptID, which is a primary key
        dept.append(values[6]) 
        all_primary_keys.append(values[6])
    if len(values[11]) != 0: dept.append(values[11]) # get deptName
    if len(values[12]) != 0: dept.append(values[12]) # get building
    if len(dept) == 3: all_dept.append(dept)

    # check for "major" values
    major = []
    # get studentID, which is a foreign key
    studentID = -1;
    if len(values[0]) != 0:
        studentID = values[0]
    # majors need to be separated.. so funky checks ensue
    current_major = values[4]
    if len(current_major) != 0:
        if ";" in current_major:
            buff = []
            first_major = current_major[ : current_major.index(";")]
            if first_major in all_primary_keys:
                buff.append([studentID, first_major])
            second_major = current_major[ current_major.index(";") + 1 : ]
            if second_major in all_primary_keys:
                buff.append([studentID, second_major])
            all_major.extend(buff)
        elif studentID != -1: all_major.append([studentID, current_major])

    # check for "Course" values
    course = []
    for i in range(6):
        if len(values[i+5]) == 0: break
        course.append(values[i+5])
    if len(course) == 6: all_course.append(course)

    # check for "Enroll" values
    enroll = []
    if len(values[5]) != 0: enroll.append(values[5]) # get courseNum
    if len(values[6]) != 0 and values[6] in all_major: enroll.append(values[6]) # get deptID
    if len(values[0]) != 0: enroll.append(values[0]) # get studentID
    if len(enroll) ==3: all_enroll.append(enroll)

# floss out dups and order inserts
already_covered = []
for dept in all_dept: 
    if dept not in already_covered: 
        write_to_file("Dept", dept)
        already_covered.append(dept)
for student in all_student: 
    if student not in already_covered:
        write_to_file("Student", student)
        already_covered.append(student)
for major in all_major: 
    if major not in already_covered:
        write_to_file("Major", major)
        already_covered.append(major)
for course in all_course: 
    if course not in already_covered:
        write_to_file("Course", course)
        already_covered.append(course)
for enroll in all_enroll: 
    if enroll not in already_covered:
        write_to_file("Enroll", enroll)
        already_covered.append(enroll)

raw_db.close()
out_db.close()