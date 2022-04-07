from enum import Enum


class LootPoolEntryType(Enum):
    ALTERNATIVES = 'minecraft:alternatives'
    DYNAMIC = 'minecraft:dynamic'
    EMPTY = 'minecraft:empty'
    GROUP = 'minecraft:group'
    ITEM = 'minecraft:item'
    LOOT_TABLE = 'minecraft:loot_table'
    SEQUENCE = 'minecraft:sequence'
    TAG = 'minecraft:tag'
