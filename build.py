from jinja2 import Template

with open('slides.md', 'r') as slides_reader, open('index.html.j2', 'r') as index_reader, open('index.html', 'w+') as index_writer:
    
    template = Template(index_reader.read())
    slides = slides_reader.read()
    index_writer.write(template.render({'slides': slides}))