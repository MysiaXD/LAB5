class Ammunition:
    def __init__(self, name: str, weight: float, price: float):
        #ініцбазпол
        if weight <= 0 or price <= 0:
            #помвідємдан
            raise ValueError("вага/ціна мають бути > 0")
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, вага:{self.weight}, ціна:{self.price})"


class Armor(Ammunition):
    def __init__(self, name: str, weight: float, price: float, defense: int):
        #ініцполдоч
        super().__init__(name, weight, price)
        if defense < 0:
            #помзахист
            raise ValueError("захист >= 0")
        self.defense = defense


class Weapon(Ammunition):
    def __init__(self, name: str, weight: float, price: float, damage: int):
        #ініцполдоч
        super().__init__(name, weight, price)
        if damage < 0:
            #помшкода
            raise ValueError("шкода >= 0")
        self.damage = damage


class Shield(Ammunition):
    def __init__(self, name: str, weight: float, price: float, block: int):
        #ініцполдоч
        super().__init__(name, weight, price)
        if block < 0:
            #помблок
            raise ValueError("блок >= 0")
        self.block = block


class Knight:
    def __init__(self):
        #ініцмас
        self.equipment = []

    def equip(self, item: Ammunition):
        #доделм
        if not isinstance(item, Ammunition):
            #помтипу
            raise TypeError("треба об амун")
        self.equipment.append(item)

    def get_total_cost(self) -> float:
        #рахсумварт
        return sum(item.price for item in self.equipment)

    def sort_by_weight(self):
        #сортвагзрос
        self.equipment.sort(key=lambda x: x.weight)

    def find_by_price_range(self, min_p: float, max_p: float) -> list[Ammunition]:
        #пошдіапцін
        if min_p > max_p or min_p < 0:
            #помнекдіап
            raise ValueError("некоректний діап")
        return [item for item in self.equipment if min_p <= item.price <= max_p]


if __name__ == "__main__":
    try:
        #ствліц
        knight = Knight()

        #екіппредм
        knight.equip(Armor("Сталевий нагрудник", 15.5, 500.0, 50))
        knight.equip(Weapon("Меч-кладенець", 3.2, 350.0, 45))
        knight.equip(Shield("Ростовий щит", 8.0, 200.0, 30))

        print("--- Початкове екіпірування ---")
        for item in knight.equipment:
            print(item)

        #друксумварт
        print(f"\nЗагальна вартість амуніції: {knight.get_total_cost()}")

        #виксерт
        knight.sort_by_weight()
        print("\n--- Сортування за вагою ---")
        for item in knight.equipment:
            print(item)

        #викпош
        min_price, max_price = 250.0, 600.0
        print(f"\nПошук амуніції в діапазоні цін [{min_price} - {max_price}]:")
        found_items = knight.find_by_price_range(min_price, max_price)

        for item in found_items:
            #друкзнайд
            print(item)

    except ValueError as e:
        #обрпомдан
        print(f"помилка даних: {e}")
    except TypeError as e:
        #обрпомтипу
        print(f"помилка типу: {e}")
    except Exception as e:
        #обрневідом
        print(f"непередбачувана помилка: {e}")