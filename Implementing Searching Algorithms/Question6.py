def update_record(student_records, ID, record_title, data):
    
    if record_title == "ID":
        return "ID cannot be updated"
    
    l = 0
    h = len(student_records) - 1
    found = None

    while l <= h:
        m = (l + h) // 2
        if student_records[m][0] == ID:
            found = m
            break
        elif ID < student_records[m][0]:
            h = m - 1
        else:
            l = m + 1

    if found == None:
        return "Record not found"

    if record_title == "Email":
        student_records[found] = (student_records[found][0], data, student_records[found][2], student_records[found][3])
    elif record_title == "Mid1":
        student_records[found] = (student_records[found][0], student_records[found][1], data, student_records[found][3])
    elif record_title == "Mid2":
        student_records[found] = (student_records[found][0], student_records[found][1], student_records[found][2], data)

    return "Record updated"


if __name__ == "__main__":
    # Output should be [('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)]
    print(update_record([('aa02822', 'ea02822', 80, 65), ('ea02822', 'ea02822@st.habib.edu.pk', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'ea02822', 'Email', 'updated@gmail.com'))
