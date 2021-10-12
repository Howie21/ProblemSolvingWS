
from cell_phone import CellPhone

cell = CellPhone('Wes', 888-442-4551)
print(cell.contacts)
cell.recieve_text("Dan", "Hi how's it going?")
cell.recieve_text("Sarah", "I love you")
print(cell.messages)
cell.send_text("Dan", "Doing great, Thanks!")
cell.vibrate_toggle()
print(cell.vibrate)