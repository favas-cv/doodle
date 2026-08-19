import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the base64 images in projects
projects_images = ['rentout.webp', 'peakpack.webp']
def replace_img(match):
    img = projects_images.pop(0) if projects_images else 'peakpack.webp'
    return f"background-image:url('{img}')"

content = re.sub(r"background-image:url\('data:image/[^']+'\)", replace_img, content)

# Add Experience section before Projects
if 'id="experience"' not in content:
    experience_html = """
  <!-- ============ EXPERIENCE ============ -->
  <section id="experience" class="services">
    <div class="sec-head">
      <div class="kicker">MY JOURNEY</div>
      <h2 class="sec-title">EXPERIENCE</h2>
    </div>
    <div class="services-grid">
      <div class="service-card">
        <div class="num">01</div>
        <h3>Python Full Stack Developer Intern</h3>
        <p>Bridgeon Solutions, Kozhikode. Building production-grade REST APIs, AI chatbots, and cloud-native deployments on AWS with Docker and Terraform.</p>
      </div>
    </div>
  </section>
"""
    content = content.replace('  <!-- ============ PROJECTS ============ -->', experience_html + '\n  <!-- ============ PROJECTS ============ -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
