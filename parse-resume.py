import PyPDF2
import json

def parse_resume(text):
    lines = text.split('\n')
    json_resume = {}

    for line in lines:
        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            if key and value:
                json_resume[key] = value

    return json_resume

resume_path = 'resume.pdf'

with open(resume_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages) 
    text = ''

    for page_num in range(num_pages):
        page = reader.pages[page_num] 
        text += page.extract_text() 

    json_resume = parse_resume(text)

    print(json.dumps(json_resume, indent=2))