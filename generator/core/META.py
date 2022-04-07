from . import Block, Item
from .Logger import logger
from .Type import LanguageType


class META:
    __Name__: str
    __nameSpace__: str
    __Author__: list[str]
    __Version__: str
    __description__: str
    __blockList__: list[Block]
    __itemList__: list[Item]

    def __init__(self,
                 name: str,
                 nameSpace: str,
                 author: list[str] = None,
                 description: str = '',
                 version: str = '1.0.0'):
        """
        最常见的用法: ``META('尘光','lightdust',['Gugle'],'示例数据包','1.0.0')``

        创建一个基本的数据包对象

        :param name: 数据包名称
        :param nameSpace: 命名空间
        :param author: 作者列表
        :param description: 数据包描述
        :param version: 数据包版本号
        """
        self.__Name__ = name
        self.__nameSpace__ = nameSpace
        self.__Author__ = author
        self.__description__ = description
        self.__Version__ = version
        self.__blockList__ = []
        self.__itemList__ = []

    def registerBlock(self, block: Block):
        """
        向数据包中注册方块

        :param block: 方块对象
        """
        if block not in self.__blockList__:
            self.__blockList__.append(block)
        else:
            logger.warning("请勿重复注册")
        block.__meta__ = self

    def registerItem(self, item: Item):
        """
        向数据包中注册物品

        :param item: 物品对象
        """
        if item not in self.__itemList__:
            self.__itemList__.append(item)
        else:
            logger.warning("请勿重复注册")
        item.__meta__ = self

    def getTranslates(self, language: LanguageType = LanguageType.ENUS):
        """
        最常见的用法: ``getTranslates(LanguageType.ENUS)``

        获取所有的translate键值对

        :param language: 设定所获取translate键值对的语言
        :return: 所有的translate键值对
        """
        __trans__: dict
        __trans__ = {}
        for i in range(len(self.__blockList__)):
            __trans__.update(self.__blockList__[i].getTranslate(language))
        for i in range(len(self.__itemList__)):
            __trans__.update(self.__itemList__[i].getTranslate(language))
        return __trans__
