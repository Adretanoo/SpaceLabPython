from label import Label
from button import Button
from panel import Panel


lb1 = Label("Hello World")
lb2 = Label("Menu")
lb3 = Label("Cars")

btn1 = Button("Click Menu")
btn2 = Button("Click Cars")

panel_menu = Panel("Main Menu")
panel_menu.add(lb2)
panel_menu.add(lb1)

panel_cars = Panel("Main Cars")
panel_cars.add(lb1)
panel_cars.add(lb3)
panel_cars.add(btn2)



root = Panel("Root")
root.add(panel_menu)
root.add(panel_cars)

root.render()

btn2.pour_completely()