# Python packages practice
* packageの作成を試す
* see
  * [setuptools Quickstart — setuptools 55.0.0 documentation](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html)
  * [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/)
  * [navdeep-G/setup.py: 📦 A Human's Ultimate Guide to setup.py.](https://github.com/navdeep-G/setup.py)
  * [Python パッケージングの標準を知ろう - Tech Blog - Recruit Engineer](https://engineer.recruit-lifestyle.co.jp/techblog/2019-12-25-python-packaging-specs/)
  * [PEP 517 -- A build-system independent format for source trees | Python.org](https://www.python.org/dev/peps/pep-0517/)
  * [PEP 518 -- Specifying Minimum Build System Requirements for Python Projects | Python.org](https://www.python.org/dev/peps/pep-0518/)


## 実装
### PEP517

* `setup.cfg`と`pyproject.toml` を使い `setup.py` 無しでwheelを作成しinstall可能。なおPEP517に従う場合、wheelを作成せずに直接installすることは[出来ないようだ](https://discuss.python.org/t/pep-517-and-projects-that-cant-install-via-wheels/791)
  * 現状のrepository内には `setup.py` が存在するが、ファイルを削除して実行可能

``` bash
> pip install build
> cd /path/to/this_repository/with_pep517
> python -m build
# 生成物の確認
> tree 
.
├── dist
│   ├── mypackage-0.0.1-py3-none-any.whl
│   └── mypackage-0.0.1.tar.gz
├── mypackage
│   ├── __init__.py
│   └── hoge.py
├── mypackage.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── pyproject.toml
└── setup.cfg
...
> pip install dist/mypackage-0.0.1-py3-none-any.whl 
# packageの動作確認
> cd ../
> python -c 'import mypackage.hoge; mypackage.hoge.hello_world()'
hello world!
```

### without PEP517

* ~~PEP517に従う方法ではDevelopment modeでのinstallは不可能。~~ そうでもなくなった？
  * [setuptools Quickstart — setuptools 55.0.0 documentation](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html#development-mode)
* `setup.py` を書いて setuptools の方法でDevelopment modeでinstall出来る。
* 以下のように書くだけで `setup.py` の作成は完了。 `setup.cfg` の項目が自動で反映される。

``` py
import setuptools
setuptools.setup()
```

* 後は以下のようにすれば、wheelを作らず直接install可能

``` sh
> cd /path/to/this_repository
> pip install -e without_pep517

# packageの動作確認
> python -c 'import without_pep517.hoge; without_pep517.hoge.hello_world()'
hello world!
```

### CPython C Extension

C,C++実装をCPythonから利用する。

``` bash
> cd /path/to/this_repository
> pip install ./python_c_extension
# packageの動作確認
> pip list | grep spam
spam-package 0.0.1
> pip freeze | grep spam
spam-package @ file:///path/to/setuptools_practice/python_c_extension

> python -c "import spam; spam.system('ls')"
README.md  python_c_extension  with_pep517  without_pep517
```

`build` を使えばWheelの作成も可能

```
> cd python_c_extension
> python -m build
> tree
.
├── README.md
├── dist
│   ├── spam_package-0.0.1-cp38-cp38-linux_x86_64.whl
│   └── spam_package-0.0.1.tar.gz
├── pyproject.toml
├── setup.cfg
├── setup.py
├── spam_package.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
└── spammodule.c

2 directories, 11 files

> pip install dist/spam_package-0.0.1-cp38-cp38-linux_x86_64.whl
> python -c "import spam; spam.system('ls')"
README.md  dist  pyproject.toml  setup.cfg  setup.py  spam_package.egg-info  spammodule.c
```

#### refs
* Practice https://docs.python.org/3/extending/extending.html. 
* Install c extension with setuptools. These are references, using distutils instead of setuptools.
  * https://docs.python.org/ja/3/extending/building.html#building-c-and-c-extensions-with-distutils
  * https://docs.python.org/ja/3/distutils/setupscript.html#describing-extension-modules
* see:
  * https://packaging.python.org/guides/packaging-binary-extensions/#introduction-to-c-c-extension-modules 

### CPython C Extension with Stable ABI

* C Extensionは通常はbuildに使ったpyhonの（マイナー）バージョンのみで利用可能。しかし[Stable ABI](https://docs.python.org/ja/3/c-api/stable.html)に基づいて実装・compileすれば複数バージョンで利用可能。
* 具体的な実装としては以下。Extensionの引数として `py_limited_api=True` と [Py_LIMITED_API](https://docs.python.org/ja/3/c-api/stable.html) のdefineが必要。

```
# setup.py
module1 = Extension(
    'spam2',
    sources=['spammodule.c'],
    py_limited_api=True,
    define_macros=[('Py_LIMITED_API', 0x03060000)]
)
```

## その他情報
* `setup.py` `setup.cfg` での項目の説明は以下
  * https://setuptools.readthedocs.io/en/latest/references/keywords.html
  * https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
