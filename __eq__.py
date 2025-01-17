class Clock:
    
    __DAY = 86400 # кол-во сек. в сутках
    
    # Метод isinstance() в Python используется для проверки принадлежности объекта
    #к определённому классу или типу данных. Он принимает два аргумента: объект,
    #который нужно проверить, и класс или тип данных, к которому нужно проверить
    #принадлежность.
    
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int): # ПРОВЕРКА НА ЦЕЛЫЕ ЧИСЛА
            raise TypeError('СЕКУНДЫ ДОЛЖНЫ БЫТЬ ЦЕЛЫМ ЧИСЛОМ')
        self.seconds = seconds % self.__DAY # ФОРМИРУЕМ ЛОКАЛЬНОЕ СВ-ВО /
                                            # КОЛ-ВО СЕК. В СУТКАХ
        
      # для сравнения ЗНАЧЕНИЙ переменных и экземпляров  
      # класса, а не их ID, используется метод __eq__ 
    def __eq__(self, other): 
        if not isinstance(other, (int, Clock)): # other может быть int и Clock
            raise TypeError('ОПЕРАНТ СПРАВА ДОЛЖЕН ИМЕТЬ ТИП INT BKB CLOCK')
        
        # ПЕРЕМЕННАЯ sc ЯВЛЯЕТСЯ other, ЕСЛИ other ЦЕЛОЕ ЧИСЛО (INT),
        # ИНАЧЕ (else) sc ЯВЛЯЕТСЯ ЭКЗЕМПЛЯРОМ КЛАССА Clock (seconds)
        sc = other if isinstance(other, int) else other.seconds
        
        # ИЗ ЭКЗЕМПЛЯРА КЛАССА с1 (ПАРАМЕТР self), ПРОВЕРЯЕМ ЧТО seconds
        # ДОЛЖЕН БЫТЬ РАВЕН sc (КОЛ-ВО СЕК. У ПРАВОГО ОПЕРАНТА)
        return self.seconds  == sc
                              

# экземпляры класса (какое-то текущее время в сек.):
c1 = Clock(1000)
c2 = Clock(1000)
print(c1 == c2) # сравниваем с помощью __eq__ значения, а не ID экземпляров.
