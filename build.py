ul = "<ul>"
end_ul = "</ul>"
li = "<li>"
end_li = "</li>"


import os
base_dir = "./posts"

def get_flie_names(path):
    x = os.walk(path)
    for root, dir_list, file_list in x:
        # print(root)
        # print(dir_list)
        # print(file_list)
        # print(end='\n')
        # dir = root
        for file in file_list:
            file_ab_path = os.path.join(root, file)
            new_path = file_ab_path.replace('./', 'https://blinl.github.io/')
            print(new_path.replace('\\', '/'))
    


if __name__ == "__main__":
    get_flie_names(base_dir)
        

