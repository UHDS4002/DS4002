

class Disk:
    def __init__(self,size):
        self.size = size

    def __repr__(self):
        return f"D{self.size}"
    __str__ = __repr__


class Tower:
    def __init__(self,name):
        self.name = name
        self.list = list()
    def push(self,disk:Disk):
        if not self.list:
            self.list.append(disk)
        else:
            if disk.size<self.list[-1].size:
                self.list.append(disk)
            else:
                raise ValueError()
    def pop(self)-> Disk:
        return self.list.pop()

    def __str__(self):
        return str(self.list)
    __repr__ = __str__


def move(a:Tower,b:Tower,c:Tower,count):
    if count==0:
        return
    move(a,c,b,count-1)
    c.push(a.pop())
    move(b,a,c,count-1)


tower1=Tower("A")
tower2=Tower("B")
tower3=Tower("C")
for i in range(5,0,-1):
    disk=Disk(i)
    tower1.push(disk)













