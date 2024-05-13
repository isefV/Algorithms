
ITEM_TYPE = {'Phone':1, 'Refrigerator':2, 'TV':3}
ITEMS = []
ID_COUNTER = 0

class Base_Item():
    def __init__(self,type: int,price: float) -> None:
        self.__id = id_gernerator()
        self.__type = type
        self.__price = price
    
    @property
    def details(self) -> tuple:
        return (self.__id ,self.__type ,self.__price )
    
    
class Phone_Item(Base_Item):
    def __init__(self, cpu: str, ram: int, screen_ratio: str, ssd: int, price: float) -> None:
        super().__init__(ITEM_TYPE['Phone'], price)
        
        self.__cpu = cpu 
        self.__ram = ram
        self.__screen_ratio = screen_ratio
        self.__ssd = ssd
        
    @property
    def info(self) -> tuple:
        return self.details + (self.__cpu , self.__ram , self.__screen_ratio , self.__ssd)


class Tv_Item(Base_Item):
    def __init__(self, smart: bool, screen_ratio: str, brand: str, price: float) -> None:
        super().__init__(ITEM_TYPE['TV'], price)
        
        self.__smart = smart 
        self.__screen_ratio = screen_ratio
        self.__brand = brand
        
    @property
    def info(self) -> tuple:
        return self.details + (self.__smart , self.__brand , self.__screen_ratio)    


class Refrigerator_Item(Base_Item):
    def __init__(self, quality_level: int, size: int, brand: str, price: float) -> None:
        super().__init__(ITEM_TYPE['Refrigerator'], price)
        
        self.__quality_level = quality_level 
        self.__size = size
        self.__brand = brand
        
    @property
    def info(self) -> tuple:
        return self.details + (self.__quality_level , self.__brand , self.__size)   


def id_gernerator() -> int:
    global ID_COUNTER
    ID_COUNTER += 1
    return ID_COUNTER

def insert_items() -> None:
    for key,val in ITEM_TYPE.items():
        print(f'{val}-{key}')
    item = int(input('Choose item to insert:'))
    
    if item == ITEM_TYPE['Phone']:
        cpu = input('What is the cpu model?')
        ram = int(input('What is the ram capacity?'))
        screen_ratio = input('What is the screen raito?')
        ssd = int(input('What is ssd capacity?'))
        price = int(input('How much is it?'))
        obj = Phone_Item(cpu,ram,screen_ratio,ssd,price)
        ITEMS.append(obj)
    elif item == ITEM_TYPE['TV']:
        smart = bool(input('Is smart tv?'))
        screen_ratio = input('What is the screen raito?')
        brand = input('What is the brand?')
        price = int(input('How much is it?'))
        obj = Tv_Item(smart,screen_ratio,brand,price)
        ITEMS.append(obj)
    elif item == ITEM_TYPE['Refrigerator']:
        smart = int(input('What is the quality?'))
        size = int(input('What is the size?'))
        brand = input('What is the brand?')
        price = int(input('How much is it?'))
        obj = Refrigerator_Item(smart,size,brand,price)
        ITEMS.append(obj)

while True:
    opt = int(input('1-Enter Item\n2-Show Item\n:'))
    match opt:
        case 1:
            insert_items()
        case 2:
            for item in ITEMS:
                print(item.info)
            break

# base = Base_Item(5,500)
# phone = Phone_Item('Qualcum',8,'6 In',512,1200)

# print(base.details ,'\n', phone.info)