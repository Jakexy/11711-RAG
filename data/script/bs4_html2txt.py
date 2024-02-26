from bs4 import BeautifulSoup
import json

# Load the HTML content
def html_parser(addr):
    with open(addr, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    faculty_data = []

    # Extract faculty details
    for cell in soup.select('td.col-1.col-first, td.col-2'):
        # person_info = {}
        # person_info['name'] = cell.find('div', class_='views-field-nothing').get_text(strip=True) if cell.find('div', class_='views-field-nothing') else None
        # person_info['title'] = cell.find('div', class_='views-field-field-computed-prof-title').get_text(strip=True) if cell.find('div', class_='views-field-field-computed-prof-title') else None
        
        # # Loop through all divs to find additional info
        # for info_div in cell.find_all('div'):
        #     label = info_div.find('span', class_='label')
        #     # If there's a label, process accordingly
        #     if label:
        #         info_type = label.get_text(strip=True).replace(':', '').lower()
        #         # Directly get the text for the div, then remove the label part
        #         full_text = info_div.get_text(strip=True)
        #         info_content = full_text.replace(label.get_text(), '').strip()
        #         person_info[info_type] = "".join(info_content.split(":")[1:])

        # faculty_data.append(person_info)
        personal_info = ""
        name = cell.find('div', class_='views-field-nothing').get_text(strip=True) if cell.find('div', class_='views-field-nothing') else None
        if not name:
            continue
        title = cell.find('div', class_='views-field-field-computed-prof-title').get_text(strip=True) if cell.find('div', class_='views-field-field-computed-prof-title') else None
        if title:
            personal_info += f"The title of {name} is {title}. "
        for info_div in cell.find_all('div'):
            label = info_div.find('span', class_='label')
            if label:
                info_type = label.get_text(strip=True).replace(':', '').lower()
                full_text = info_div.get_text(strip=True)
                info_content = full_text.replace(label.get_text(), '').strip()
                personal_info += f"The {info_type} of {name} is {info_content}. "
        faculty_data.append(personal_info)

    # Save the data to a JSON file
    with open('../parsed_data/faculty_info.txt', 'a') as txt_file:
        json.dump(faculty_data, txt_file, indent=4)

html_parser('../raw_data/lti_faculty_page1.html')
html_parser('../raw_data/lti_faculty_page2.html')
print("Faculty information has been saved to 'faculty_info.txt'.")
