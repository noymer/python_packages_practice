## setup.cfg only

`setup.py` 無しでwheelを作成し、install可能。なおwheelを作成せずに直接installすることは[出来ないようだ](https://discuss.python.org/t/pep-517-and-projects-that-cant-install-via-wheels/791)

``` bash
> pip install build
> cd /path/to/this_repository
> python -m build
# 生成物の確認
> tree 
.
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── mypackage
│           ├── __init__.py
│           └── hoge.py
├── dist
│   ├── mypackage-0.0.1-py3-none-any.whl
│   └── mypackage-0.0.1.tar.gz
├── mypackage.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
...
> pip install dist/mypackage-0.0.1-py3-none-any.whl 
# packageの動作確認
> python -c 'import mypackage.hoge; mypackage.hoge.hello_world()'
hello world!
```