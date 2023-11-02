from fio_wrapper import FIO

fio = FIO(api_key="55a39a35-a65f-4713-bc92-0e2ae344a177")

# material = fio.Material.get("DW")
# print(material)
# print(material.model_dump_json())


# print(fio.LocalMarket.planet_buy("Promitor"))
# print(fio.LocalMarket.planet_sell("Promitor"))
# print(fio.LocalMarket.planet_shipping("ANT"))


# print(fio.LocalMarket.company("SKYP"))

data = fio.Planet.search(
    materials=["FEO", "LST"],
    include_rocky=True,
    must_be_fertile=True,
    distance_checks=["Katoa", "Promitor", "Montem"],
)

print(data)
