from generator.core.BasicTag import EntityTag
from generator.core.enum.EntityType import EntityType

a = EntityTag(EntityType.BEE, customName="shy bee", pos=[1.0, 2.0, 3.0], tags=["6666"])
print(a)
