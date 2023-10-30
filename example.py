from pyfio import FIO

fio = FIO()

material = fio.Material.get("DW")
print(material)
