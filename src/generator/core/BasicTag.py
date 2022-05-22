from .TagType import *
from .enum import Item, EntityType
from .Handle import randomUUID


class ItemTag:
    count: TAG_Int
    itemId: TAG_String
    tag: TAG_Compound

    def __init__(self, itemId: Item, count: int = 1, tag: list[TAG] = None):
        self.count = TAG_Int('count', count)
        self.itemId = TAG_String('id', itemId)
        self.tag = TAG_Compound('tag', tag)

    def __str__(self) -> str:
        return f'{{{self.count}, {self.itemId}, {self.tag}}}'


class EntityTag:
    pass


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

    def __init__(self,
                 entityId: EntityType,
                 air: int = 300,
                 customName: str = None,
                 customNameVisible: int = 0,
                 fallDistance: float = 0.0,
                 fire: int = 0,
                 glowing: int = 0,
                 hasVisualFire: int = 0,
                 invulnerable: int = 0,
                 motion: list[float] = [0.0, 0.0, 0.0],
                 noGravity: int = 0,
                 onGround: int = 0,
                 passengers: list[EntityTag] = None,
                 portalCooldown: int = 0,
                 pos: list[float] = [0.0, 0.0, 0.0],
                 rotation: list[float] = [0.0, 0.0],
                 silent: int = 1,
                 tags: list[str] = None,
                 uuid: list[int] = randomUUID()):
        self.entityId = TAG_String('id', entityId.value)
        self.air = TAG_Short('Air', air)
        self.customName = TAG_String('CustomName', customName)
        self.customNameVisible = TAG_Byte('CustomNameVisible', customNameVisible)
        self.fallDistance = TAG_Float('FallDistance', fallDistance)
        self.fire = TAG_Short('Fire', fire)
        self.glowing = TAG_Byte('Glowing', glowing)
        self.hasVisualFire = TAG_Byte('HasVisualFire', hasVisualFire)
        self.invulnerable = TAG_Byte('Invulnerable', invulnerable)
        self.motion = TAG_List('Motion', motion)
        self.noGravity = TAG_Byte('NoGravity', noGravity)
        self.onGround = TAG_Byte('OnGround', onGround)
        self.passengers = TAG_List('Passengers', passengers)
        self.portalCooldown = TAG_Int('PortalCooldown', portalCooldown)
        self.pos = TAG_List('Pos', pos)
        self.rotation = TAG_List('Rotation', rotation)
        self.silent = TAG_Byte('Silent', silent)
        self.tags = TAG_List('Tags', tags)
        self.uuid = TAG_Int_Array('UUID', uuid)

    def __str__(self) -> str:
        s = f'{{{str(self.entityId)}}}'

        def append(x: TAG, a: str):
            a = a[:-1] + ', ' + str(x) + a[-1]
            return a

        s = append(self.air, s)
        s = append(self.customName, s)
        s = append(self.customNameVisible, s)
        s = append(self.fallDistance, s)
        s = append(self.fire, s)
        s = append(self.glowing, s)
        s = append(self.hasVisualFire, s)
        s = append(self.invulnerable, s)
        s = append(self.motion, s)
        s = append(self.noGravity, s)
        s = append(self.onGround, s)
        s = append(self.passengers, s)
        s = append(self.portalCooldown, s)
        s = append(self.pos, s)
        s = append(self.rotation, s)
        s = append(self.silent, s)
        s = append(self.tags, s)
        s = append(self.uuid, s)
        return s
