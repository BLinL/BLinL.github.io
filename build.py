#!/usr/bin/python
# encoding:utf-8

import os
from mk import mdfile2html
from mako_demo import serve_template

base_dir = "./posts"

def get_flie_names(path):
    x = os.walk(path)

    items = {}
    for root, dir_list, file_list in x:
        files = [file for file in file_list if file.endswith('.md')]

        try:
            for i in files:
                file = os.path.join(root, i)
                html = mdfile2html(open(file, encoding='utf-8'))
                items[i] = html
        except TypeError:
            print("err")
       

    return items


if __name__ == "__main__":
    # print(files)
    # buid index
    items = get_flie_names(base_dir)
    #print(items)
    html = serve_template('index_template.html', {'data': items})
    

    f = open('./index.html','w',encoding="utf-8")
    f.write(html)


    # i = 0
    # for name in file_names:
    #     i += 1
    #     post_name = name.split('/')[-1]
    #     print(f"{i}. [{post_name}]({name})")
    #     f.write(f"{i}. [{post_name}]({name}) \n\n")

    # f.close()
        

