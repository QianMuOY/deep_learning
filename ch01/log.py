import logging

x = 1
assert x == 0, "x!=0"


print("this is print")

logging.basicConfig(format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',  # 输出格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
                    # filename='demo.log',  # 输出到文件
                    # filemode='w',  # 写入方式 w:先清空再写入 a:在后方追加
                    level=logging.DEBUG)  # 默认等级

logging.debug(x)
logging.debug("debug_msg")
logging.info("info_msg")
logging.warning("warning_msg")
logging.error("error_msg")
logging.critical("critical_msg")
