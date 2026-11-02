# CLAUDE.md

本仓库是《Python-100-Days》学习教程，`Day*/` 等目录是原教程内容，自己的练习代码放在 `practice/` 下。

## Python 环境

- 使用 conda 环境 `python100`（Python 3.12，含 jupyterlab、numpy、pandas、matplotlib）
- 环境定义：`practice/env/environment.yml`
- 不要用系统自带的 `/usr/bin/python3`（3.9）
- 运行脚本：`conda run -n python100 python xxx.py`
- 安装依赖：`conda run -n python100 pip install xxx`，新增的依赖同步写进 `practice/env/environment.yml`
