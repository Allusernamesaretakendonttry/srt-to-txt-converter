import os
import re

def srt_to_txt(input_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.srt', '.txt'))
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    text_lines = []
    
    for line in content:
        if not re.match(r'^\d+$', line.strip()) and not re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line.strip()):
            text_lines.append(line.strip())
    
    text = '\n'.join([line for line in text_lines if line])
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
    
    print(f'Converted {input_file} to {output_file}')

if __name__ == "__main__":
    input_srt = input("Enter the path to the SRT file: ").strip().strip('"')
    output_folder = "txts"
    srt_to_txt(input_srt, output_folder)
