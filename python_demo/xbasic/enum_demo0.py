import enum


class EnumClass0(enum.Enum):
    INFO = 'I'
    WARNING = 'W'
    ERROR = 'E'


# 支持for in语法
# EnumClass0.INFO
# EnumClass0.WARNING
# EnumClass0.ERROR
for e in EnumClass0:
    # e.value就是每个项的实际值，比如INFO的value就是I
    print(f"{e=}, {e.value=}")


x = EnumClass0("I")
# x=<EnumClass0.INFO: 'I'>, x.name='INFO', x.value='I'
print(f"{x=}, {x.name=}, {x.value=}")



class IntEnumClass0(enum.IntEnum):
    a = 1
    b = 2


# (IntEnumClass0.a == 1)=True, 2
print(f"{(IntEnumClass0.a == 1)=}, {int(IntEnumClass0.b)}")
