# douyinTools
抖音自动辅助工具

### 使用手册
* 安装anaCodan
  * 安装包下载
    ```shell
    https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D
    ```
  * 安装完成后创建新的虚拟环境,打开Anaconda Prompt命令窗口
    ```shell
    conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  # 这是一行命令
    ```
  * 激活新的虚拟环境
  ```shell
    # 激活paddle_env环境
    conda activate paddle_env
    # 查看当前python的位置
    where python
   ```
  * 安装paddlepaddle
  ```shell
  python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
  ```
  * 安装PaddleOCR whl
  ```shell
  pip install "paddleocr>=2.0.1"
  # 可能遇到Microsoft Visual C++ 14.0 or greater is required.的报错，需要安装 Microsoft Visual C++ Build Tools
  ```
  * 执行main目录下的功能脚本