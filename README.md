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

### without PEP517

* PEP517に従う方法ではDevelopment modeでのinstallは不可能。
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
> pip install .
# or install development mode
# > pip install -e .

# packageの動作確認
> python -c 'import mypackage.hoge; mypackage.hoge.hello_world()'
hello world!
```

## その他情報
* `setup.py` `setup.cfg` での項目の説明は以下
  * https://setuptools.readthedocs.io/en/latest/references/keywords.html
  * https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
