from CalendarAlgorithms1 import *
from CalendarAlgorithms1.easter_gauss import easter_gauss_main
from CalendarAlgorithms1.easter_meeus_jones_butcher import easter_mjb_main
from CalendarAlgorithms1.leap_year import leap_year_main

data1 = [1600, 1700, 1800, 1900, 1954, 1977, 1981, 1988, 1991, 2000, 2010, 2015, 2019, 2022, 2024, 2025, 2026, 2038, 2040, 2056]

for item in data1:
    print(item, leap_year_main(item))
    print(easter_gauss_main(item) , easter_mjb_main(item))