# Python packages practice
* packageの作成を試す
* see
  * [setuptools Quickstart — setuptools 55.0.0 documentation](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html)
  * [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/)

## setup.cfg only

* `setup.py` 無しでwheelを作成し、install可能。なおwheelを作成せずに直接installすることは[出来ないようだ](https://discuss.python.org/t/pep-517-and-projects-that-cant-install-via-wheels/791)
  * 現状のrepository内には `setup.py` が存在するが、ファイルを削除して実行可能

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

## setup.py

* `setup.cfg`だけではDevelopment modeでのinstallは不可能。
  * [setuptools Quickstart — setuptools 55.0.0 documentation](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html#development-mode)
* 以下のように書くだけで `setup.py` の作成は完了。 `setup.cfg` の項目が自動で反映される。


``` py
import setuptools
setuptools.setup()
```

* 後は以下のようにすれば、wheelを作らず直接install可能

``` sh
> cd /path/to/this_repository
> pip install .
# or install development mode
# > pip install -e .

# packageの動作確認
> python -c 'import mypackage.hoge; mypackage.hoge.hello_world()'
hello world!
```