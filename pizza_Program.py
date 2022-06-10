import tkinter as tk
from tkinter import ttk

def transport():
    if transport_method.get() == 0:
        print("Delivery")
        address_entry.configure(state=tk.ACTIVE)
    elif transport_method.get() == 1:
        print("Pick Up")
        address_entry.configure(state=tk.DISABLED)

def complete_order():
    customer_detail.configure(text="Customer Details:\n{}\n{}\n".format(name_entry.get(), address_entry.get()))



root=tk.Tk()

selected_pizza_1 = tk.StringVar()
selected_pizza_1.set("Select a pizza")

selected_pizza_2 = tk.StringVar()
selected_pizza_2.set("Select a pizza")

selected_pizza_3 = tk.StringVar()
selected_pizza_3.set("Select a pizza")

selected_pizza_4 = tk.StringVar()
selected_pizza_4.set("Select a pizza")

selected_pizza_5 = tk.StringVar()
selected_pizza_5.set("Select a pizza")

transport_method = tk.IntVar()
transport_method.set(0)

regular_pizza=["peperoni","cheese & garlic" , "Buffalo Pizza" , "Beef supreme" , "veggie" , "BBQ Beef" , "cheese pizza" , "Beef & Onion"]
gourmet = ["aboli", "margirita", "stella", "salmon", "vegetariano" ]


tkb_button=ttk.Label(root, text ="148 TKB PIZZA SHOP")
tkb_button.grid(row=0, column=1, columnspan=2)
regular_label=ttk.Label(root, text="REGULAR PIZZA")
regular_label.grid(row=1, column=0)
gourmet_Button=ttk.Label(root, text="Gourmet PIZZA")
gourmet_Button.grid(row=1, column=3)
peperoni_Label=ttk.Label(root, text ="*peperoni(8.50c)\n*cheese &garlic(8.50c)\n*buffalopizza(8.50c)\n*Beefsupreme(8.50c)\n*veggie(8.50c)\n*BBQBeef(8.50c)\n*cheesePizza(8.50c)\n*Beef&onion(8.50c)")
peperoni_Label.grid(row=2, column=0)

aboli_Label=ttk.Label(root, text="*aboli(13.50c)\n*margirita(13.50c)\n*stella(13.50c)\nsalmon(13.50c)\nvegetariano(13.50c)")
aboli_Label.grid(row=2, column=3)


select_menu_1=ttk.Combobox(root,textvariable=selected_pizza_1)
select_menu_1.grid(row=2, column=1, columnspan=2)
select_menu_1['values'] =  regular_pizza + gourmet
select_menu_1['state'] = 'readonly'

select_menu_1=ttk.Combobox(root,textvariable=selected_pizza_2)
select_menu_1.grid(row=3, column=1, columnspan=2)
select_menu_1['values'] = regular_pizza + gourmet
select_menu_1['state'] = 'readonly'

select_menu_1=ttk.Combobox(root,textvariable=selected_pizza_3)
select_menu_1.grid(row=4, column=1, columnspan=2)
select_menu_1['values'] = regular_pizza + gourmet
select_menu_1['state'] = 'readonly'

select_menu_1=ttk.Combobox(root,textvariable=selected_pizza_4)
select_menu_1.grid(row=5, column=1, columnspan=2)
select_menu_1['values'] = regular_pizza + gourmet
select_menu_1['state'] = 'readonly'

select_menu_1=ttk.Combobox(root,textvariable=selected_pizza_5)
select_menu_1.grid(row=5, column=1, columnspan=2)
select_menu_1['values'] = regular_pizza + gourmet
select_menu_1['state'] = 'readonly'


delivery_RadioButton=ttk.Radiobutton(root, text="delivery $3.00", variable=transport_method, value=0, command=transport)
delivery_RadioButton.grid(row=6, column=1)
pickup_RadioButton=ttk.Radiobutton(root, text="pick up", variable=transport_method, value=1, command=transport)
pickup_RadioButton.grid(row=7, column=1)

name_Label=ttk.Label(root, text="NAME:")
name_Label.grid(row=8, column=1)

name_entry=ttk.Entry(root)
name_entry.grid(row=8, column=2)

name_Label=ttk.Label(root, text="ADDRESS:")
name_Label.grid(row=9, column=1)

address_entry=ttk.Entry(root)
address_entry.grid(row=9, column=2)

tkb_label=ttk.Label(root, text="148 TKB PIZZA ODERING SYSTEM")
tkb_label.grid(row=11, column=1)

order_label=ttk.Label(root, text="*Order\n*cheese pizza\n*Beef&Onion\n*BBQ Beef\n*Veggie\n*Peperoni")
order_label.grid(row=12, column=1)

customer_detail = ttk.Label(root, text="Customer Details:")
customer_detail.grid(row=13, column=1, columnspan=2)

cancel_Button=ttk.Button(root, text="CANCEL ORDER")
cancel_Button.grid(row=14, column=0)

submit_button = ttk.Button(root, text="SUBMIT ORDER", command=complete_order)
submit_button.grid(row = 14, column=1)

start_button=ttk.Button(root, text="Start Over")
start_button.grid(row=14, column=3)
root.mainloop()