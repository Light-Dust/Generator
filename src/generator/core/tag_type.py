from .handle import LOGGER


class TAG:
    __value__: str
    __key__: str

    def __init__(self, key):
        self.__key__ = key

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}'


class TAG_End(TAG):
    ...


class TAG_Byte(TAG):
    __value__: int

    def __init__(self, key: str, value: int):
        super().__init__(key)
        if 127 >= value >= -128:
            self.__value__ = value
        else:
            LOGGER.error('Byte的范围为-128~127')

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}b'


class TAG_Short(TAG):
    __value__: int

    def __init__(self, key: str, value: int):
        super().__init__(key)
        if 32767 >= value >= -32768:
            self.__value__ = value
        else:
            LOGGER.error('Short的范围为-32768~32767')

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}s'


class TAG_Int(TAG):
    __value__: int

    def __init__(self, key: str, value: int):
        super().__init__(key)
        if 2147483647 >= value >= -2147483648:
            self.__value__ = value
        else:
            LOGGER.error('Int的范围为-2147483648~2147483647')

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}'


class TAG_Long(TAG):
    __value__: float

    def __init__(self, key: str, value: float):
        super().__init__(key)
        if 9223372036854775807 >= value >= -9223372036854775808:
            self.__value__ = value
        else:
            LOGGER.error('Long的范围为-9223372036854775808~9223372036854775807')

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}l'


class TAG_Float(TAG):
    __value__: float

    def __init__(self, key: str, value: float):
        super().__init__(key)
        self.__value__ = value

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}f'


class TAG_Double(TAG):
    __value__: float

    def __init__(self, key: str, value: float):
        super().__init__(key)
        self.__value__ = value

    def __str__(self) -> str:
        return f'{self.__key__}: {str(self.__value__)}d'


class TAG_Byte_Array(TAG):
    __value__: list[int] = []

    def __init__(self, key: str, value: list[int]):
        super().__init__(key)
        for i in value:
            if 127 >= i >= -128:
                self.__value__.append(i)
            else:
                LOGGER.error('Byte的范围为-128~127')
                break

    def __str__(self) -> str:
        x: str = f'{self.__key__}: [B;'
        for i in self.__value__:
            x = x + f' {i},'
        x = x[:-1] + ']'
        return x


class TAG_String(TAG):
    __value__: str

    def __init__(self, key: str, value: str):
        super().__init__(key)
        self.__value__ = value

    def __str__(self) -> str:
        if self.__value__ is not None:
            return f'{self.__key__}: "{str(self.__value__)}"'
        else:
            return f'{self.__key__}: ""'


class TAG_List(TAG):
    __value__: list

    def __init__(self, key: str, value: list):
        super().__init__(key)
        self.__value__ = value

    def append(self, value):
        self.__value__.append(value)

    def remove(self, pos: int):
        self.__value__.remove(self.__value__[pos])

    def __index__(self, value):
        return self.__value__.index(value)

    def __count__(self, value):
        return self.__count__(value)

    def change(self, pos: int, value):
        self.__value__[pos] = value

    def replace(self, value1, value2):
        for i in range(self.__value__.count(value1)):
            self.__value__.remove(value1)
            self.__value__.append(value2)

    def __str__(self) -> str:
        x: str = f'{self.__key__}: ['

        if self.__value__ is not None:
            for i in self.__value__:
                if type(i) == str:
                    x = x + f'"{str(i)}", '
                else:
                    x = x + f'{str(i)}, '
            x = x[:-2] + ']'
        else:
            x = x + ']'
        return x


class TAG_Compound(TAG):
    __value__: list[TAG] = []

    def __init__(self, key: str, value: list[TAG] = None):
        super().__init__(key)
        self.__value__ = value

    def __str__(self) -> str:
        x: str = f'{self.__key__}: {{'
        for i in self.__value__:
            x = x + f'{str(i)}, '
        x = x[:-2] + '}'
        return x


class TAG_Int_Array(TAG):
    __value__: list[int] = []

    def __init__(self, key: str, value: list[int]):
        super().__init__(key)
        for i in value:
            if 2147483647 >= i >= -2147483648:
                self.__value__.append(i)
            else:
                LOGGER.error('Int的范围为-2147483648~2147483647')
                break

    def __str__(self) -> str:
        x: str = f'{self.__key__}: [I;'
        for i in self.__value__:
            x = x + f' {i},'
        x = x[:-1] + ']'
        return x


class TAG_Long_Array(TAG):
    __value__: list[int] = []

    def __init__(self, key: str, value: list[int]):
        super().__init__(key)
        for i in value:
            if 9223372036854775807 >= i >= -9223372036854775808:
                self.__value__.append(i)
            else:
                LOGGER.error('Long的范围为-9223372036854775808~9223372036854775807')
                break

    def __str__(self) -> str:
        x: str = f'{self.__key__}: [L;'
        for i in self.__value__:
            x = x + f' {i},'
        x = x[:-1] + ']'
        return x
