import json

dic = dict()
def read_and_process_file(file_path):
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
        
def add_department_to_courses(json_file_path, department_mapping):
    # Read the JSON data from the file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Iterate over each course in the 'courses' list
    for course in data['courses']:
        # Extract the first two digits of the course code
        course_code_prefix = course['course'][:2]
        # Find the corresponding department name; default to 'Unknown' if not found
        department_name = department_mapping.get(course_code_prefix, 'Unknown Department')
        # Add the 'department' key-value pair to the course
        course['department'] = department_name
    
    # Write the updated data back to the file
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


# Replace 'path/to/your/file.txt' with the actual file path
file_path = 'department.txt'
read_and_process_file(file_path)

file_path2 = 'fall_courses.json'
add_department_to_courses(file_path2, dic)
