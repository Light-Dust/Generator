from TagType import *
from MinecraftEnum import Item, EntityType


class ItemTag:
    count: TAG_Int
    itemId: TAG_String
    tag: TAG_Compound

    def __init__(self, count: int, itemId: Item, tag: list[TAG]):
        self.count = TAG_Int('count', count)
        self.itemId = TAG_String('id', itemId)
        self.tag = TAG_Compound('tag', tag)

    def __str__(self) -> str:
        return f'{{{self.count}, {self.itemId}, {self.tag}}}'


class EntityTag:
    air: TAG_Short
    customName: TAG_String
    customNameVisible: TAG_Byte
    fallDistance: TAG_Float
    fire: TAG_Short
    glowing: TAG_Byte
    hasVisualFire: TAG_Byte
    entityId: TAG_String
    invulnerable: TAG_Byte
    motion: TAG_List
    noGravity: TAG_Byte
    onGround: TAG_Byte
    passengers: TAG_List
    portalCooldown: TAG_Int
    pos: TAG_List
    rotation: TAG_List
    silent: TAG_Byte
    tags: TAG_List
    uuid: TAG_Int_Array

    def __init__(self, entityId: EntityType):
        self.entityId = TAG_String('id', entityId)

    def __str__(self) -> str:
        ...
