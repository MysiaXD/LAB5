from unittest import TestCase
from main import Armor, Weapon, Shield, Knight


class TestKnightEquipment(TestCase):

    def setUp(self):
        # автзапмет
        # ствліцпредм
        self.knight = Knight()
        self.armor = Armor("Обладунок", 10.0, 300.0, 40)
        self.weapon = Weapon("Меч", 2.0, 150.0, 25)

    def test_equip_and_cost(self):
        # доделекіп
        self.knight.equip(self.armor)
        self.knight.equip(self.weapon)

        # персумварт
        self.assertEqual(self.knight.get_total_cost(), 450.0)

    def test_sorting(self):
        # доделекіп
        self.knight.equip(self.armor)
        self.knight.equip(self.weapon)

        # виксертваг
        self.knight.sort_by_weight()

        # персортмас
        self.assertEqual(self.knight.equipment[0], self.weapon)
        self.assertEqual(self.knight.equipment[1], self.armor)

    def test_search_range(self):
        # доделекіп
        self.knight.equip(self.armor)
        self.knight.equip(self.weapon)

        # викпошдіап
        found = self.knight.find_by_price_range(100.0, 200.0)

        # перрезпош
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], self.weapon)

    def test_errors(self):
        # первикпомдан
        with self.assertRaises(ValueError):
            Armor("Тест", -5.0, 100.0, 10)

        with self.assertRaises(ValueError):
            self.knight.find_by_price_range(200.0, 100.0)