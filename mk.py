from markdown import markdown

def mdfile2html(f):
    html = markdown(f, extensions=['fenced_code'])
    # print(html)
    return html


