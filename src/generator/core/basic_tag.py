from .tag_type import *
from .enum import Item, EntityType
from .handle import random_uuid


class ItemTag:
    count: TAG_Int
    itemId: TAG_String
    tag: TAG_Compound

    def __init__(self, item_id: Item, count: int = 1, tag: list[TAG] = None):
        self.count = TAG_Int('count', count)
        self.itemId = TAG_String('id', str(item_id.value))
        self.tag = TAG_Compound('tag', tag)

    def __str__(self) -> str:
        return f'{{{self.count}, {self.itemId}, {self.tag}}}'


class EntityTag:
    pass


class EntityTag:
    air: TAG_Short
    custom_name: TAG_String
    custom_name_visible: TAG_Byte
    fall_distance: TAG_Float
    fire: TAG_Short
    glowing: TAG_Byte
    has_visual_fire: TAG_Byte
    entity_id: TAG_String
    invulnerable: TAG_Byte
    motion: TAG_List
    no_gravity: TAG_Byte
    on_ground: TAG_Byte
    passengers: TAG_List
    portal_cooldown: TAG_Int
    pos: TAG_List
    rotation: TAG_List
    silent: TAG_Byte
    tags: TAG_List
    uuid: TAG_Int_Array

    def __init__(self,
                 entity_id: EntityType,
                 air: int = 300,
                 custom_name: str = None,
                 custom_name_visible: int = 0,
                 fall_distance: float = 0.0,
                 fire: int = 0,
                 glowing: int = 0,
                 has_visual_fire: int = 0,
                 invulnerable: int = 0,
                 motion=None,
                 no_gravity: int = 0,
                 on_ground: int = 0,
                 passengers: list[EntityTag] = None,
                 portal_cooldown: int = 0,
                 pos=None,
                 rotation=None,
                 silent: int = 1,
                 tags: list[str] = None,
                 uuid=None):
        if motion is None:
            motion = [0.0, 0.0, 0.0]
        if rotation is None:
            rotation = [0.0, 0.0]
        if pos is None:
            pos = [0.0, 0.0, 0.0]
        if uuid is None:
            uuid = random_uuid()
        self.entity_id = TAG_String('id', str(entity_id.value))
        self.air = TAG_Short('Air', air)
        self.custom_name = TAG_String('CustomName', custom_name)
        self.custom_name_visible = TAG_Byte('CustomNameVisible', custom_name_visible)
        self.fall_distance = TAG_Float('FallDistance', fall_distance)
        self.fire = TAG_Short('Fire', fire)
        self.glowing = TAG_Byte('Glowing', glowing)
        self.has_visual_fire = TAG_Byte('HasVisualFire', has_visual_fire)
        self.invulnerable = TAG_Byte('Invulnerable', invulnerable)
        self.motion = TAG_List('Motion', motion)
        self.no_gravity = TAG_Byte('NoGravity', no_gravity)
        self.on_ground = TAG_Byte('OnGround', on_ground)
        self.passengers = TAG_List('Passengers', passengers)
        self.portal_cooldown = TAG_Int('PortalCooldown', portal_cooldown)
        self.pos = TAG_List('Pos', pos)
        self.rotation = TAG_List('Rotation', rotation)
        self.silent = TAG_Byte('Silent', silent)
        self.tags = TAG_List('Tags', tags)
        self.uuid = TAG_Int_Array('UUID', uuid)

    def __str__(self) -> str:
        s = '{}'
        for i in self.__dict__.values():
            s = s[:-1] + ', ' + str(i) + s[-1]
        s = s[0] + s[3:]
        return s
