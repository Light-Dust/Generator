from TagType import TAG, TAG_Int, TAG_String, TAG_Compound


class ItemTag:
    count: TAG_Int
    itemId: TAG_String
    tag: TAG_Compound

    def __init__(self, count: int, itemId: str, tag: list[TAG]):
        self.count = TAG_Int('count', count)
        self.itemId = TAG_String('id', itemId)
        self.tag = TAG_Compound('tag', tag)

    def __str__(self) -> str:
        return f'{{{self.count}, {self.itemId}, {self.tag}}}'
