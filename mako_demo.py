from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['./'], module_directory='/tmp/mako_modules')

def serve_template(templatename, data):
    mytemplate = mylookup.get_template(templatename)
    return mytemplate.render(**data)


# serve_template("index.html", name="wahh")