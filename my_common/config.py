import json
import os
import re


def get_config(size):
    m = re.search(r'(\d+)x(\d+)', size)
    if m:
        screen_size = "{height}x{width}".format(height=m.group(2), width=m.group(1))
    else:
        screen_size = "1920x1080"

    config_file = "{path}/config/{screen_size}/config.json".format(
        path=get_project_path(),
        screen_size=screen_size
    )
    if not os.path.exists(config_file):
        config_file = "{path}/config/config.json".format(
            path=get_project_path()
        )
    with open(config_file, 'r') as f:
        return json.load(f)


def get_project_path():
    """得到项目路径"""
    project_path = os.path.join(
        os.path.dirname(__file__),
        "..",
    )
    return project_path


# 获取评论消息库
def get_base_config():
    file = "{path}/config/base_config.json".format(
        path=get_project_path()
    )
    with open(file, 'r', encoding='UTF-8') as f:
        return json.load(f)
