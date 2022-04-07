from enum import Enum


class ChunkStatus(Enum):
    BIOMES = 'minecraft:biomes'
    CARVERS = 'minecraft:carvers'
    EMPTY = 'minecraft:empty'
    FEATURES = 'minecraft:features'
    FULL = 'minecraft:full'
    HEIGHTMAPS = 'minecraft:heightmaps'
    LIGHT = 'minecraft:light'
    LIQUID_CARVERS = 'minecraft:liquid_carvers'
    NOISE = 'minecraft:noise'
    SPAWN = 'minecraft:spawn'
    STRUCTURE_REFERENCES = 'minecraft:structure_references'
    STRUCTURE_STARTS = 'minecraft:structure_starts'
    SURFACE = 'minecraft:surface'
