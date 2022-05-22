from generator.core.TagType import *


class ItemTag(list[TAG]):
    pass


class UniversallyTag(ItemTag):
    def __init__(self, damage: int, unbreakable: bool, canDestroy: list[TAG_String], customModelData: int):
        super().__init__()
        self.append(TAG_Int('Damage', damage))
        self.append(TAG_Byte('Unbreakable', int(unbreakable)))
        self.append(TAG_List('CanDestroy', canDestroy))
        self.append(TAG_Int('CustomModelData', customModelData))


class BlockTag(ItemTag):
    def __init__(self, canPlaceOn: list[TAG_String], blockEntityTag: list[TAG], blockStateTag: list[TAG]):
        super().__init__()
        self.append(TAG_List('CanPlaceOn', canPlaceOn))
        self.append(TAG_Compound('BlockEntityTag', blockEntityTag))
        self.append(TAG_Compound('BlockStateTag', blockStateTag))


class EnchantmentsTag(ItemTag):
    def __init__(self, enchantments: list[TAG_Compound], repairCost: int):
        super().__init__()
        self.append(TAG_List('Enchantments', enchantments))
        self.append(TAG_Int('RepairCost', repairCost))
