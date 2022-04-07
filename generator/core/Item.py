from . import META
from .Type import LanguageType


class Item:
    __meta__: META
    __itemCMD__: int
    __itemID__: str
    __enUS__: str
    __zhCN__: str
    __zhTW__: str
    __zhHK__: str
    __oreDict__: str
    __customTag__: dict

    def __init__(self, itemID: str, itemCMD: int, enUS: str = None, zhCN: str = None, zhTW: str = None,
                 zhHK: str = None, oreDict: str = None, customTag: dict = {}):
        """
        最常见的用法: ``Item('test', 10000001, 'test', '测试', '測試', '測試', None)``

        创建一个基本的物品对象

        :param itemID: 物品的ID
        :param itemCMD:物品的CustomModelData
        :param enUS:英文的翻译文本
        :param zhCN:简体中文的翻译文本
        :param zhTW:繁体中文（台湾）的翻译文本
        :param zhHK:繁体中文（香港的翻译文本）
        :param oreDict:该物品具有的矿物词典列表
        :param customTag:该物品具有的自定义NBT
        """
        self.__itemID__ = itemID
        self.__itemCMD__ = itemCMD
        self.__enUS__ = enUS
        self.__zhCN__ = zhCN
        self.__zhTW__ = zhTW
        self.__zhHK__ = zhHK
        self.__oreDict__ = oreDict
        self.__customTag__ = customTag

    def getTranslate(self, language: LanguageType = LanguageType.ENUS) -> dict:
        """
        最常见的用法: ``getTranslate(LanguageType.ENUS)``

        获取方块的translate

        :param language: 设定所获取translate键值对的语言
        :return: 该方块的translate
        """
        key: str = f'item.{self.__meta__.__nameSpace__}.{self.__itemID__}'
        value: str = ''
        if language == LanguageType.ENUS:
            value = self.__enUS__
        if language == LanguageType.ZHCN:
            value = self.__zhCN__
        if language == LanguageType.ZHHK:
            value = self.__zhHK__
        if language == LanguageType.ZHTW:
            value = self.__zhTW__
        return {key: value}

    def register(self, meta: META):
        """
        向数据包中注册方块

        :param meta: 数据包对象
        """
        meta.registerItem(self)
