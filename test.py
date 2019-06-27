from simpletable import Table, Cell

table = Table(align="center")
table.add_row([Cell("Name", align="left"), "Age", "Gender"], header=True)
table.add_row([Cell("Christopher", align="left"), 28, "M"], fgcolor="red")
table.add_row([Cell("Holly", align="left"), 24, "F"], fgcolor="yellow")
table.add_row([Cell("Patrick", align="left"), 26, Cell("M", bold=True, bgcolor="white")], fgcolor="green")
print(table)
