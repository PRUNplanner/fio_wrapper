from pyfio import FIO

fio = FIO()

material = fio.Material.get("DW")
print(material)
print(material.model_dump_json())
