### main分支向后移动
``git rebase side main``

### 合并分支
``merge or rebase( clean )``

### 本地分支跟踪远程分支
``git checkout -b totallyNotMain o/main``
一般不需要这么做，因为clone时 git已经自动将远程分支在本地创建，然后创建一个跟踪远程活动分支的main分支
或者使用
``git branch -u o/main foo``

### HEAD
HEAD可以指向分支也可以指向具体的提交


