from pyfio import FIO

fio = FIO()

# material = fio.Material.get("DW")
# print(material)
# print(material.model_dump_json())


# print(fio.LocalMarket.planet_buy("Promitor"))
# print(fio.LocalMarket.planet_sell("Promitor"))
# print(fio.LocalMarket.planet_shipping("ANT"))


print(fio.LocalMarket.company("SKYP"))
