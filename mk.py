from markdown import markdown

def mdfile2html(file):
    file = open('posts/docker.md', encoding='utf-8').read()

    html = markdown(file)

    # print(html)

    return html


