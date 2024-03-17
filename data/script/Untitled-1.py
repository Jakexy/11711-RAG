import json
input_path = 'spring_course_data.json'
output_path = 'spring_courses.md'
with open(input_path, 'r') as file:
    data = json.load(file)
    
semester = data['semester']
courses = data['courses']

with open(output_path, 'w') as file:
    for course in courses:
        res = f"\"Semester\": \"{semester}\", "
        for key in course:
            key2 = key[0].upper() + key[1:]
            if key != 'sessions':
                res += f"\"{key2}\": \"{course[key]}\", "
        if 'sessions' not in course:
            res += "sessions: None"
            file.write(res + '\n')
        else:
            for session in course['sessions']:
                res2 = ""
                for key in session:
                    key2 = key[0].upper() + key[1:]
                    if key == "type":
                        res2 += f"\"Session {key2}\": \"{session[key]}\", "
                    elif key == "instructors":
                        names = ", ".join(session[key])
                        res2 += f"\"Session {key2}\": \"{names}\", "
                    else:
                        res2 += f"\"{key2}\": \"{session[key]}\", "
                file.write(res + res2 + '\n')
        
        
