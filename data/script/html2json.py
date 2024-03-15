import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict

def read_and_process_file(file_path,dic):
    # Open the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    # Process the file in groups of six lines
    for i in range(0, len(lines), 7):
        # Extract a group of six lines
        group_of_six = lines[i:i+7]
        value = group_of_six[1].rstrip()
        key = group_of_six[3][1:3]
        
        # Process your group of six here
        # For example, just printing them
        print(key)
        print(value)
        dic[key] = value
        print("---- End of Group ----\n")

def parse_html_to_json(html_text,dic):
    courses = []
    current_course = None
    current_session = None

    soup = BeautifulSoup(html_text, 'html.parser')
    rows = soup.find_all('tr')

    for row in rows[1:]:  # Skip header row
        columns = row.find_all('td')
        if columns:
            course_info = [col.text.strip() for col in columns]

            if len(course_info) == 10:
                if course_info[0]:  # Course info
                    if current_course:
                        courses.append(current_course)
                    current_course = ""
                    course = course_info[0]
                    title = course_info[1]
                    units = course_info[2]
                    department = dic.get(course[:2],"None")
                    
                course_type = course_info[3]
                if course_type.startswith("Lec"):
                    course_type = "Lecture" + course_type[3:]
                else:
                    course_type = "Session" + course_type[3:]
                days = course_info[4]
                if not "TBA" in days:
                    days = " and ".join(list(days))
                    dic2 = {"M":"Monday","T":"Tuesday","W":"Wednesday","R":"Thursday","F":"Friday"}
                    for k in dic2:
                        days = days.replace(k,dic2[k])
                # print(days)
                begin = course_info[5]
                end = course_info[6]
                room = course_info[7]
                loc = course_info[8]
                # instructor = [x.strip() for x in course_info[9].split(",") if x.strip()]
                # instructor = ", ".join(instructor)
                instructor = course_info[9]
                current_course = f"The course {course} is {title} and is {units} units. It is in the {department} department. The {course_type} meets on {days} from {begin} to {end} in {room} at {loc}. The instructor is {instructor}."
    if current_course:  # Add the last course
        courses.append(current_course)

    return courses

# Example HTML link
html_link = "https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_fall.htm"
response = requests.get(html_link)
html_text = response.text
dic = dict()
read_and_process_file('department.txt',dic)

courses_data = parse_html_to_json(html_text,dic)

# Write JSON output to file
with open("fall_courses.json", "w") as json_file:
    json.dump(courses_data, json_file, indent=2)

print("JSON file 'courses.json' has been created.")


# import requests
# from bs4 import BeautifulSoup
# import json

# def parse_html_to_json(html_text):
#     soup = BeautifulSoup(html_text, 'html.parser')

#     # Parse date and semester information
#     date_info = soup.find(text="Run Date:")
#     semester_info = soup.find(text="Semester:")
#     run_date = date_info.split(':')[1].strip() if date_info else None
#     semester = semester_info.split(':')[1].strip() if semester_info else None

#     # Initialize dictionary to store data
#     data = {"run_date": run_date, "semester": semester, "subjects": {}}

#     # Parse subject and course information
#     current_subject = None
#     current_courses = []

#     rows = soup.find_all('tr')
#     for row in rows[3:]:  # Skip header rows and date/semester info
#         columns = row.find_all('td')
#         if columns:
#             info = [col.text.strip() for col in columns]

#             if len(info) == 1:  # Subject info
#                 if current_subject:
#                     data["subjects"][current_subject] = current_courses
#                     current_courses = []
#                 current_subject = info[0]
#             elif len(info) == 10:  # Course info
#                 course = {
#                     "course": info[0],
#                     "title": info[1],
#                     "units": info[2],
#                     "sessions": [{
#                         "type": info[3],
#                         "days": info[4],
#                         "begin_time": info[5],
#                         "end_time": info[6],
#                         "building_room": info[7],
#                         "location": info[8],
#                         "instructors": [x.strip() for x in info[9].split(",") if x.strip()]
#                     }]
#                 }
#                 current_courses.append(course)
#             elif len(info) == 0 and current_subject:  # End of subject
#                 data["subjects"][current_subject] = current_courses
#                 current_subject = None
#                 current_courses = []

#     # Add the last subject
#     if current_subject:
#         data["subjects"][current_subject] = current_courses

#     return data

# # Example HTML link
# html_link = "https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_summer_1.htm"
# response = requests.get(html_link)
# html_text = response.text

# data = parse_html_to_json(html_text)

# # Write JSON output to file
# with open("summer_1_course_data.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print("JSON file 'course_data.json' has been created.")
