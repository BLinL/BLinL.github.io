
## Dockerfile
描述如何构建镜像

image 镜像， 可以在容器运行的应用 就像安装包
## make image
docker build [-t name] .

## RUN
docker run -dp port:port image_name

## enter container
docker exec <container-id> cat /data.txt

-p host map container
## cmd
docker ps
docker stop
docker rm

-- stop and rm
docker rm -rf

## volume 持久化存储
保证容器重启后数据不会丢失
docker volume crate volume_name

docker run -dp 3000:3000 -v todo-db:/etc/todos todo-app

查看volumn信息

docker volume inspect volume_name
```
[
    {
        "CreatedAt": "2021-11-08T11:21:08+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/todo-db/_data",
        "Name": "todo-db",
        "Options": {},
        "Scope": "local"
    }
]

```

Mountpoint 就是本地挂载点