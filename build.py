#!/usr/bin/python
# encoding:utf-8

import os
base_dir = "./posts"

def get_flie_names(path):
    x = os.walk(path)

    files = []
    for root, dir_list, file_list in x:
        # print(root)
        # print(dir_list)
        # print(file_list)
        # print(end='\n')
        # dir = root
        for file in file_list:
            file = os.path.splitext(file)[0]
            file_ab_path = os.path.join(root, file)
            new_path = file_ab_path.replace('./', 'https://blinl.github.io/')
            # print(new_path.replace('\\', '/'))
            files.append(new_path.replace('\\', '/'))

    return files


if __name__ == "__main__":
    file_names = get_flie_names(base_dir)

    f = open('./index.md','w',encoding="utf-8")
    f.write("# 文章列表：\n\n")
    i = 0
    for name in file_names:
        i += 1
        post_name = name.split('/')[-1]
        print(f"{i}. [{post_name}]({name})")
        f.write(f"{i}. [{post_name}]({name}) \n\n")

    f.close()
        

