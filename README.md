- [wsxk\_fuzzer introduction](#wsxk_fuzzer-introduction)
- [install](#install)
- [How to use](#how-to-use)
- [TODO](#todo)
- [License](#license)


# wsxk_fuzzer introduction<br>
简易的，可定制的auto fuzz框架（看了许多关于fuzz的论文后，发现auto-fuzz最大的问题不是`auto`，是如何hook`function`<br>

# install<br>
进入[https://github.com/AFLplusplus/AFLplusplus](https://github.com/AFLplusplus/AFLplusplus)进行AFL++的安装<br>

```
    git clone https://github.com/AFLplusplus/AFLplusplus.git
    make
    make install 
```
PS: 可以考虑安装`llvm`使afl提供更加强大的功能<br>
在安装完成后，使用如下命令<br>
```
    cd unicorn_mode
    ./build_unicorn_support.sh
```
安装完成后，你已经具备了该框架的使用能力<br>

# How to use<br>
本次使用已经给出样例，目录下的`target.yml`文件包含的是一个你想fuzz的目标程序的基本信息，`target.yml`请放在当前目录下，而`target`目标程序，你可以放在硬盘中的任意位置。<br>
最关键的是`target.yml`中的`handlers`部分，这部分要求你对每一个你想要hook的function编写相应的替代函数，本工具中已经给出示例<br>

# TODO<br>
`arm x86 arm64`的支持还没写（😄<br>

# License<br>
这个框架属于[license](./LICENSE.txt)

