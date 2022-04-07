from .Type import LanguageType
from .META import META


class Block:
    __meta__: META
    __itemCMD__: int
    __blockCMD__: int
    __blockID__: str
    __enUS__: str
    __zhCN__: str
    __zhTW__: str
    __zhHK__: str
    __hadSide__: bool
    __hadTop__: bool
    __hadBottom__: bool
    __oreDict__: list[str]
    __haveGUI__: bool

    def __init__(self, blockID: str, itemCMD: int, blockCMD: int, enUS: str = None, zhCN: str = None,
                 zhTW: str = None, zhHK: str = None, hadSide: bool = True, hadTop: bool = False,
                 hadBottom: bool = False,
                 oreDict: list[str] = None, haveGUI: bool = False):
        """
        最常见的用法: ``Block('test', 10000001, 10001001, 'test', '测试', '測試', '測試', True, False, False, None, False)``

        创建一个基本的方块对象

        :param blockID:方块的ID
        :param itemCMD:方块物品的CustomModelData
        :param blockCMD:方块的CustomModelData
        :param enUS:英文的翻译文本
        :param zhCN:简体中文的翻译文本
        :param zhTW:繁体中文（台湾）的翻译文本
        :param zhHK:繁体中文（香港的翻译文本）
        :param hadSide:是否具有侧面贴图
        :param hadTop:是否具有单独的顶部贴图
        :param hadBottom:是否具有单独的底部贴图
        :param oreDict:该方块具有的矿物词典列表
        :param haveGUI:该方块是否具有GUI
        """
        self.__blockID__ = blockID
        self.__itemCMD__ = itemCMD
        self.__blockCMD__ = blockCMD
        self.__enUS__ = enUS
        self.__zhCN__ = zhCN
        self.__zhTW__ = zhTW
        self.__zhHK__ = zhHK
        self.__hadSide__ = hadSide
        self.__hadTop__ = hadTop
        self.__hadBottom__ = hadBottom
        self.__oreDict__ = oreDict
        self.__haveGUI__ = haveGUI

    def getTranslate(self, language: LanguageType = LanguageType.ENUS) -> dict:
        """
        最常见的用法: ``getTranslate(LanguageType.ENUS)``

        获取方块的translate

        :param language: 设定所获取translate键值对的语言
        :return: 该方块的translate
        """
        key: str = f'block.{self.__meta__.__nameSpace__}.{self.__blockID__}'
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
        meta.registerBlock(self)
