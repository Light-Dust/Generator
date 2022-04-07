from generator.core.tag_type import *


class ItemTag(list[TAG]):
    pass


class UniversallyTag(ItemTag):
    def __init__(self, damage: int, unbreakable: bool, can_destroy: list[TAG_String], custom_model_data: int):
        super().__init__()
        self.append(TAG_Int('Damage', damage))
        self.append(TAG_Byte('Unbreakable', int(unbreakable)))
        self.append(TAG_List('CanDestroy', can_destroy))
        self.append(TAG_Int('CustomModelData', custom_model_data))


class BlockTag(ItemTag):
    def __init__(self, can_place_on: list[TAG_String], block_entity_tag: list[TAG], block_state_tag: list[TAG]):
        super().__init__()
        self.append(TAG_List('CanPlaceOn', can_place_on))
        self.append(TAG_Compound('BlockEntityTag', block_entity_tag))
        self.append(TAG_Compound('BlockStateTag', block_state_tag))


class EnchantmentsTag(ItemTag):
    def __init__(self, enchantments: list[TAG_Compound], repair_cost: int):
        super().__init__()
        self.append(TAG_List('Enchantments', enchantments))
        self.append(TAG_Int('RepairCost', repair_cost))
