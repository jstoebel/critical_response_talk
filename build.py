import datetime
import time

from jinja2 import Template
from watchdog.observers import Observer

class MarkdownBuilder:

    def __init__(self, md_loc, template_loc, output_loc):
        self.md_loc = md_loc
        self.template_loc = template_loc
        self.output_loc = output_loc

    def dispatch(self, _):

        print('[{}] building...'.format(str(datetime.datetime.now())), end='')
        with open(self.md_loc, 'r') as slides_reader, open(self.template_loc, 'r') as index_reader, open(self.output_loc, 'w+') as index_writer:
            
            template = Template(index_reader.read())
            slides = slides_reader.read()
            index_writer.write(template.render({'slides': slides}))

        print(' -> done!')

if __name__ == '__main__':
    path = '.'
    print('watching...')
    observer = Observer()
    md_builder = MarkdownBuilder('slides.md', 'index.html.j2', 'index.html')
    md_builder.dispatch('_') # initial build incase file changed while I was offline
    observer.schedule(md_builder, path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()