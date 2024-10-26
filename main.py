
field_line_offsets = {
    "Created": 4,
    "Not Signed": 3,
    "Name": 3,
    "Date of Birth": 3,
    "Medicare Number": 3
}


def extract_values_based_on_offsets(text, field_line_offsets):
    extracted_data = {}
    
    
    lines = text.strip().split('\n')


    for field, offset in field_line_offsets.items():
        for i, line in enumerate(lines):
            if field in line:
                
                value_index = i + offset
                
                if value_index < len(lines):
                    
                    value_line = lines[value_index].strip()
                    
                    parts = value_line.split(':')
                    if len(parts) >= 4:
                        
                        value = ':'.join(parts[3:]).strip()

                        
                        if field in ["Created", "Not Signed"]:
                            
                            if value_index + 1 < len(lines):
                                next_line = lines[value_index + 1].strip()
                                
                                value += " " + next_line.split(':')[-1].strip()

                        
                        extracted_data[field] = value
                    else:
                        extracted_data[field] = value_line

    return extracted_data


def main(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    
    extracted_data = extract_values_based_on_offsets(text, field_line_offsets)

    
    formatted_data = {
        "Date of Birth": extracted_data["Date of Birth"],
        "Created": extracted_data["Created"],
        "Name": extracted_data["Name"],
        "Not Signed": extracted_data["Not Signed"],
        "Medicare Number": extracted_data["Medicare Number"]
    }

    
    print(formatted_data)  


file_path = 'archivo1.txt'
main(file_path)
