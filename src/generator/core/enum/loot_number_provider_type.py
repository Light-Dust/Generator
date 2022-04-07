from enum import Enum


class LootNumberProviderType(Enum):
    BINOMIAL = 'minecraft:binomial'
    CONSTANT = 'minecraft:constant'
    SCORE = 'minecraft:score'
    UNIFORM = 'minecraft:uniform'
