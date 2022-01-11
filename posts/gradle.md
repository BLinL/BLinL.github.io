## 学习gradle 第一天

> Each build script you have is associated with an object of type Project and as the build script executes, it configures this Project.

与build.gradle 关联会有一个Project对象， 当执行构建脚本时它会配置这个Project

### Project 提供的标准字段
group

version

name

Project

description

projectDir

buildDir

path



当执行build.gradle脚本的时候, gradle会把它编译为一个class, 并且实现了Script接口， 所以所有在Script里定义的字段和方法在脚本里都可用


### 本地变量和额外的变量


```gradle
//本地
def xx = __

//额外
ext {
    aa = __
    bb = __
}

```

额外变量挂在那个对象底下？

## 第二天
一个project 可以有多个task
task 
```groovy

task hello {
    doLast {
        println 'hello' // 使用groovy
    }
}
```

task 依赖
```groovy
task intro(dependsOn: hello) {
     println 'intro'
}
```

task 依赖的task 可以在声明时不存在, 也就是可以不用在意定义顺序

自定义属性
```groovy

task hello {
	ext.a = "zhangsan"
	doLast {
		println "hello name is : $hello.a"
	}
}
```
groovy脚本极大增加了构建灵活性


变量tasks 保存了所有定义的task
```
tasks.register("hello_a") {
	dependsOn tasks.intro
	doLast {
		println 'hi gradle'
	}
}
```

执行脚本
gradle -q taskname

-q 简洁输出内容

## 灵活
批量定义task
```groovy
4.times {counter->
	tasks.register("task_$counter") {
		doLast {
			println("task $counter run")
		}
	}
}
```
```groovy
// add dependencies dynamically
tasks.named("task_3") {
	dependsOn('task_2','hello')
}
```

### 牛啊
脚本可以添加依赖（编写构建脚本使用 非项目依赖）
```
import org.apache.commons.codec.binary.Base64

buildscript {
	repositories {
		mavenCentral()
		dependencies {
			classpath group: 'commons-codec', name: 'commons-codec', version: '1.2'
		}
	}
}

```

多模块项目也可以在子项目构建脚本中使用 buildScript 来声明依赖

每个Project默认有一个buildEnvironment task可以调用以报告构建脚本依赖项的解决情况。