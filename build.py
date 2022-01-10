#!/usr/bin/python
# encoding:utf-8

import os
import pathlib
from shutil import Error
from sys import stdout
from mk import mdfile2html
from mako_demo import serve_template
from datetime import datetime
base_dir = "./posts"



class FileNotFound(Exception):
  pass


class Resources(object):

  def __init__(self, resource_dir=None):
    self._path = resource_dir
    if not self._path:
      path = os.path.dirname(os.path.realpath(__file__))
      self._path = os.path.join(path, 'resources')

  def GetResourceFileName(self, file_name):
    """Returns the full path to a resource file.

    Args:
      file_name: A file to search for under the installer resource directory.

    Returns:
      The full path to the resource on disk.

    Raises:
      FileNotFound: No file exists at the determined path.
    """
    # file_name = file_name.strip('/')
    path = os.path.join(self._path, file_name)

    if os.path.exists(path):
      return path
    raise FileNotFound('Could not locate a resource with path %s.' % path)

class Post(object):
    def __init__(self, title, content, create_at):
        self.title = title
        self.content = content
        self.create_at = create_at

    def __str__(self):
        return f"{self.title} create at {self.create_at}"

def get_flie_names(path):
    x = os.walk(path)
    items = []
    for root, dir_list, file_list in x:
        files = [file for file in file_list if file.endswith('.md')]

        try:
            for i in files:
                # file = os.path.join(root, i)
                file = Resources(root).GetResourceFileName(i)
                p = pathlib.Path(file)
                try:
                    with open(file, encoding='utf-8') as f:
                        html = mdfile2html(f.read())
                        items.append(Post(i, html, datetime.fromtimestamp(p.stat().st_ctime)))
                except IOError:
                    print("read file err...")
               
        except Error:
            print("Error", Error)
       

    return items

def split_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    # buid index
    items = get_flie_names(base_dir)
    # print(items)
   

    page_genetetor  = split_list(items, 3)
    pagelist = list(page_genetetor)
    page = len(pagelist)
    pagenum = 0
    # print(pagelist)
    for i in pagelist:
      print(i)
      # i is pagenum
      if pagenum == 0:
        filename = './index.html'
      else:
        filename = f'./index_{pagenum}.html'
      html = serve_template('index_template.html', {'data': i, 'page': page})
      f = open(filename,'w',encoding="utf-8")
      f.write(html)
      pagenum = pagenum + 1

    for post in items:
      f = open(post.title.replace('.md','.html'),'w',encoding="utf-8")
      html = serve_template('post_template.html', {'data': post})
      f.write(html)

        

