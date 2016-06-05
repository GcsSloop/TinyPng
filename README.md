# TinyPng
### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)
图片批量压缩处理脚本(Python)

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

之后你可以将该脚本放入到需要压缩的图片的文件夹下，然后在命令行(终端)中进入到该文件夹，执行如下命令即可:

```
  tinypng.py
```

生成的文件会存入当前目录下一个名为tiny的文件夹中。

如果你觉得每次都需要复制该文件到需要压缩到目录太麻烦，可以将该脚本存储到一个文件夹中，之后将该文件夹添加进环境变量，就能在任意位置执行该脚本了。








## About Me

### 作者微博: [@GcsSloop](http://weibo.com/GcsSloop)

<a href="https://github.com/GcsSloop/README/blob/master/README.md" target="_blank"> <img src="http://ww4.sinaimg.cn/large/005Xtdi2gw1f1qn89ihu3j315o0dwwjc.jpg" width=300 height=100 /> </a>
