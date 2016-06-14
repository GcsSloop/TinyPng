# <img src="http://ww1.sinaimg.cn/large/005Xtdi2jw1f4v3ht2r2ij3074074jrl.jpg" width=32 /> TinyPng
[![License](https://img.shields.io/badge/license-Apache%202-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
![version](https://img.shields.io/badge/version-1.0.1-brightgreen.svg)

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

![](http://ww4.sinaimg.cn/large/005Xtdi2gw1f4kksnoy72j313y07yjuk.jpg)

## 前言
我们在写文章或者建网站时，经常需要对图片压缩处理，以便帮助用户节省流量和提升网站加载速度。

图片压缩有很多方法，这里推荐的是[TinyPNG](https://tinypng.com/)。TinyPNG 是一个在线压缩工具，主要优点是在视觉上没有明显变化的情况下达到很高的压缩比(如我手机截屏图片大小一般为110k，压缩后能达到30k左右)。

TinyPNG官网: https://tinypng.com/

>
TinyPNG支持一次最多上传20张图片，图片最大5M。

如果处理的图片比较少则使用在线压缩即可，非常方便，但如果图片处理量比较大，使用在线压缩一次一次的上传下载则显得有些麻烦了，因此用Python写了一个简单的脚本，用于批量压缩图片。

## 使用方法

### 一.配置环境

**Python:** 保证电脑中存在 Python 环境，(如果是Mac，则自带的有Python环境)。

**Tinify:** 导入Tinify
```
  pip install --upgrade tinify
```

### 二.申请 API key

到此处申请 API key: https://tinypng.com/developers

>
一个 key 每个月可以免费压缩500张图片，可以申请多个 key。

### 三.配置脚本并运行

**[点击此处下载脚本(右键 -> 另存为)](https://raw.githubusercontent.com/GcsSloop/TinyPng/master/tinypng.py)**

下载完该脚本后，你需要简单编辑一下该脚本，将申请到到API key 填写进去。

```
tinify.key = "你申请到的API key"
```

之后你可以将该脚本放入到需要压缩的图片的文件夹下，然后在命令行(终端)中进入到该文件夹，执行如下命令即可:

```
python tinypng.py
```

生成的文件会存入当前目录下一个名为tiny的文件夹中。

**运行示例及大小对比(有图有真相):**

![](http://ww3.sinaimg.cn/large/005Xtdi2jw1f4mdtld2r9j30rs0hctcc.jpg)

![](http://ww2.sinaimg.cn/large/005Xtdi2jw1f4mdy2e8zjj30rs0hcwir.jpg)

### 四.支持参数

在 v1.0.1 版本中进行了参数支持，详情见下表:

参数  | 参数类型 | 摘要                               | 示例
:----:|----------|------------------------------------|-----------------------------
 无参 |          | 压缩当前文件夹下所有图片文件       | `tinypng.py` 
`－f` | 图像文件 | 压缩指定的单个文件                 | `tinypng.py -f /User/GcsSloop/demo.jpg`
`－d` | 文件夹   | 压缩指定文件夹下所有图片文件       | `tinypng.py -d /User/GcsSloop/DemoDir`
 `-w` | 整型数字 | 压缩后图片的宽度，不指定则宽度不变 | `tinypng.py -w 300`

**参数优先级:**
```
  －f > －d > 无参
```
如果指定了 `－f` 则只会压缩指定文件，即使后续跟了 `－d` 也不会压缩指定的文件夹

```
 －w 无冲突，均可使用
```

`－w` 用于指定压缩后图片的宽度(width)高度自适应缩放，所以均可使用，(选项没有先后顺序)示例如下:

```
tinypng.py －w 300                              // 压缩当前目录所有图片文件，压缩后文件跨度为300

tinypng.py －w 300 -f /User/GcsSloop/demo.jpg   // 指定压缩一个文件，压缩后文件宽度为300
```

### 五.辅助优化

这一步不是必要的步骤，只是帮助你优化一些内容:

**任意位置启动(适用于 Linux 和 OS X 平台):**

如果你觉得每次都需要复制 `tinypng.py` 文件到需要压缩到目录太麻烦， 可以将该脚本存储到一个文件夹中， 之后将该文件夹添加进环境变量，就能在任意位置执行该脚本了,(仅适用于 Linux 和 OS X 平台)
使用命令直接是文件名，前面无需加python,如:
```
tinypng.py
```

如果使用直接使用文件名无法执行，则说明文件没有可执行权限，使用如下命令添加可执行权限:
```
chmod +x tinypng.py
```

[Mac 配置环境变量](https://github.com/GcsSloop/MacDeveloper/blob/master/Skill/Path.md)


**从当前目录启动(适用于 OS X 平台):**

如果从命令行中进入到某个目录比较麻烦，所以在 Mac 上你可以使用 XtraFinder 插件来给你的右键添加一个从当前目录启动选项，直接在当前目录下启动终端，添加方式在 XtraFinder 到偏好设置里面。

[点击这里查看Finder增强插件到安装方法](https://github.com/GcsSloop/MacDeveloper/blob/master/Tools/XtraFinder.md)

![](http://ww3.sinaimg.cn/large/005Xtdi2gw1f4kl9j34vij30rs0hcabg.jpg)

## 更新日志

* v1.0.0 支持压缩当前目录下文件
* v1.0.1 添加参数支持，支持压缩单个文件，压缩指定目录所有图片文件(不包含子目录)，默认压缩当前目录的所有图片文件(不包括子目录)

## About Me

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

<a href="https://github.com/GcsSloop/README/blob/master/README.md" target="_blank"> <img src="http://ww4.sinaimg.cn/large/005Xtdi2gw1f1qn89ihu3j315o0dwwjc.jpg" width=300 height=100 /> </a>


## License
```
Copyright (c) 2015 GcsSloop

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

