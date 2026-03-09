import os
import re

dir_path = r'E:\IT\my Lab\re'
replacements = [
    (r'href=([\'"])https?://(?:www\.)?bistroloft\.nl/menu/?\1', r'href=\1original_menu.html\1'),
    (r'href=([\'"])https?://(?:www\.)?bistroloft\.nl/evenementen/?\1', r'href=\1original_evenementen.html\1'),
    (r'href=([\'"])https?://(?:www\.)?bistroloft\.nl/verblijf/?\1', r'href=\1original_verblijf.html\1'),
    (r'href=([\'"])https?://(?:www\.)?bistroloft\.nl/contact/?\1', r'href=\1original_contact.html\1'),
    (r'href=([\'"])https?://(?:www\.)?bistroloft\.nl/?\1', r'href=\1original_index.html\1'),
]

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_pattern, new_replacement in replacements:
            content = re.sub(old_pattern, new_replacement, content)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Processed " + filename)
    
print("Done")
