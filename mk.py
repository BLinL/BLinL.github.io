from markdown import markdown

def mdfile2html(f):
    html = markdown(f)
    # print(html)
    return html


