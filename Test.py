from generator.core import Block, Item, META
from generator.core import Logger
from generator.core.Type import LanguageType

test = META('test', 'test', ['Gugle'], '1.0.0')
TEST = Block(blockID='test', blockCMD=14070001, itemCMD=14071001, zhCN="测试方块", zhTW="測試方塊")
TES = Block(blockID='tes', blockCMD=14070002, itemCMD=14071002, zhCN="测方块", zhTW="測方塊")
HEL = Item('test', 10000001, 'test', '测试', '測試', '測試', None)
TEST.register(test)
TES.register(test)
HEL.register(test)
Logger.logger.info(TEST.getTranslate(LanguageType.ZHCN))
Logger.logger.info(TES.getTranslate(LanguageType.ZHCN))
Logger.logger.info(HEL.getTranslate(LanguageType.ZHCN))
Logger.logger.info(test.getTranslates(LanguageType.ZHTW))
