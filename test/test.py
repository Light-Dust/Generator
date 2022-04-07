from generator.core.basic_tag import EntityTag
from generator.core.enum.entity_type import EntityType

e = EntityTag(entity_id=EntityType.BAT, passengers=[EntityTag(EntityType.BEE), EntityTag(EntityType.CAT)])
print(e)
