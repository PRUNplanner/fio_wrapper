from pyfio.fio import FIO

fio = FIO()

material = fio.Material.get("DW")
print(material.Ticker)
