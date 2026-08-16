import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Hero avatar
content = re.sub(
    r'<div class="avatar-placeholder has-photo">[\s\S]*?</div>',
    '<div class="avatar-placeholder has-photo">\n        <img src="aboutme.jpeg" alt="Muhammed Favas" style="width:100%; height:100%; object-fit:cover;">\n      </div>',
    content
)

# Replace About portrait
content = re.sub(
    r'<div class="about-portrait has-photo">[\s\S]*?</div>',
    '<div class="about-portrait has-photo">\n        <img src="aboutme.jpeg" alt="Muhammed Favas" style="width:100%; height:100%; object-fit:cover;">\n      </div>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
