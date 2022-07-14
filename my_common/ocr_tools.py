from paddleocr import PaddleOCR
from my_common import config

# 基础配置信息
base_config = config.get_base_config()


# 图片文字识别
def ocr_fun(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(img_path, cls=True)
    return result


# 首页推荐截图结果过滤
def video_image_ocr_result_analyse(result):
    if result is None:
        return None
    # 有效结果
    valid_res = []
    # 遍历结果数组
    for line in result:
        # 文字坐标
        point = line[0]
        # 文字坐标点
        left_top = point[0]
        right_bottom = point[2]

        # 顶部及底部文字丢弃
        if left_top[1] > 2220 or right_bottom[1] < 200:
            continue
        # 有效结果添加到结果数组
        valid_res.append(line)
    return valid_res


# 判断是否符合规则
def is_conform_rules(res):
    if res is None:
        return False
    is_conform = False
    for line in res:
        # 文字
        text = line[1][0]
        # 黑名单直接返回-不符合规则
        if is_exists_blacklist(text):
            print(False)
            return False
        # 存在白名单内，结果置为True
        if is_exists_white_list(text):
            is_conform = True
    print(is_conform)
    return is_conform


# 文字内容是否在白名单内
def is_exists_white_list(content):
    white_list = base_config['white_list']
    for s in white_list:
        if s.find(content) != -1 or content.find(s) != -1:
            return True
    return False


# 文字内容是否在黑名单内
def is_exists_blacklist(content):
    blacklist = base_config['blacklist']
    for s in blacklist:
        if s.find(content) != -1 or content.find(s) != -1:
            return True
    return False
