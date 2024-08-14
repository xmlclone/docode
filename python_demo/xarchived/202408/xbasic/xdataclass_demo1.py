from dataclasses import dataclass, field


class C:
    x = []
    def add(self, element):
        self.x.append(element)

o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
# 共享同一个实 x
print(o1.x == [1, 2]) # True
print(o1.x is o2.x) # True


@dataclass
class D:
    # x: list = []      # 不允许这样定义
    x: list = field(default_factory=list)
    def add(self, element):
        self.x.append(element)
# 不共享同一个实例
print(D().x is D().x)