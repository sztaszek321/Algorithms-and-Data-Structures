from CalendarAlgorithms.easter_gauss import easter_gauss_main
from CalendarAlgorithms.easter_meeus_jones_butcher import easter_mjb_main
from CalendarAlgorithms.leap_year import leap_year_main

""" 
-------------------------
1. CALENDAR ALGORITHMS
-------------------------
"""

data_calendar = [1600, 1700, 1800, 1900, 1954, 1977, 1981, 1988, 1991, 2000, 2010, 2015, 2019, 2022, 2024, 2025, 2026, 2038, 2040, 2056]

for item in data_calendar:
    print(item, leap_year_main(item))
    eg = easter_gauss_main(item)
    emjb = easter_mjb_main(item)
    f = True if eg == emjb else False
    print(eg , emjb, f)