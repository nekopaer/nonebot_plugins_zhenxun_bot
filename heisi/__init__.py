# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 16:49
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
import nonebot
from nonebot import on_command, logger
from nonebot.adapters.onebot.v11 import Bot,  MessageEvent, MessageSegment
from nonebot.typing import T_State
import os
from os.path import dirname
import random
import httpx
from configs.config import Config




__zx_plugin_name__ = "黑丝"
__plugin_usage__ = """
usage：
    来点黑丝
    指令：
    his
""".strip()
__plugin_des__ = "来点黑丝"
__plugin_cmd__ = ["his"]
__plugin_type__ = ("来点好康的")
__plugin_version__ = 0.1
__plugin_author__ = "nekopaer"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["his"]
    }


path = dirname(__file__) + "/resources"
his = on_command("his", aliases={"黑丝"}, block=True, priority=5)

@his.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if not os.path.exists(path):
        logger.info("创建资源路径")
        os.mkdir(path)
    if not os.path.exists(path + "/heisi.txt"):
        async with httpx.AsyncClient() as client:
            where_heisi = (await client.get("https://fastly.jsdelivr.net/gh/yzyyz1387/blogimages/nonebot/heisi.txt")).text
        logger.info(f"从gayhub下载资源文件  {path}/heisi.txt")
        with open(path + "/heisi.txt", "w", encoding="utf-8") as heisitxt:
            heisitxt.write(where_heisi)
    img_list = open(path + "/heisi.txt", "r", encoding="utf-8").read().replace("\n", "").split(".jpg")
    img = random.choice(img_list) + ".jpg"
    await bot.send(
        event=event,
        message=MessageSegment.image(img)
        )
