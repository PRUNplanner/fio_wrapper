import logging
from fio_wrapper import FIO

logging.basicConfig(
    level=logging.DEBUG,
    # format="%(asctime)s | %(levelname)s: %(message)s (Line: %(lineno)d) [%(filename)s]",
    # format="%(message)s",
    filename="example.log",
    filemode="w",
)

fio = FIO(api_key="dcfdf551-d8f6-4e2f-9a38-c9fbc4c04813")
# fio = FIO()

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

data = fio.Material.all(timeout=2)

groups = fio.Group.all()

for group in groups:
    detail = fio.Group.get(groupid=group.GroupModelId)
    print([user.GroupUserName for user in detail.GroupUsers])
# print(data)
