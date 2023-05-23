import random
import tkinter as tk
import turtle
from tkinter import messagebox
from tkinter import ttk
from turtle import Turtle, Screen


# Constants
COW_SIZE = 20
BARN_SIZE = 200
MILKING_PARLOR_SIZE = 200
MILK_PRICE_PER_LITER = 1
CLEANING_COST = 10
UPGRADE_COST = 100
SELLING_PRICE = 2

# Define the Cow class
class Cow:
    def __init__(self, breed):
        self.breed = breed
        self.age = 0
        self.health = 100
        self.milk_capacity = random.randint(15, 35)
        self.pen = None

    def age_cow(self):
        self.age += 1

    def is_adult(self):
        return self.age >= 2

    def produce_milk(self):
        fat_percentage = random.uniform(2, 5)
        milk_production = random.randint(15, 35)
        fat_in_milk = milk_production * (fat_percentage / 100)
        return milk_production, fat_in_milk
    
    def draw(self):
        if self.pen is None:
            self.pen = Turtle()
            self.pen.shape("circle")
            self.pen.color("black")
            self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.pendown()

# Define the Barn class
class Barn:
    def __init__(self, x, y, capacity):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.cows = []
        self.cleanliness = 100

    def add_cow(self, cow):
        if len(self.cows) < self.capacity:
            self.cows.append(cow)
            cow.x = random.uniform(self.x - (BARN_SIZE / 2) + COW_SIZE, self.x + (BARN_SIZE / 2) - COW_SIZE)
            cow.y = random.uniform(self.y - (BARN_SIZE / 2) + COW_SIZE, self.y + (BARN_SIZE / 2) - COW_SIZE)
            cow.draw()

    def draw(self):
        barn_drawer = Turtle()
        barn_drawer.penup()
        barn_drawer.goto(self.x - (BARN_SIZE / 2), self.y - (BARN_SIZE / 2))  # Gehe zur linken unteren Ecke des Stalls
        barn_drawer.pendown()
        barn_drawer.pensize(3)
        barn_drawer.color("brown")

        for _ in range(4):
            barn_drawer.forward(BARN_SIZE)  # Zeichne eine Seite des Stalls
            barn_drawer.left(90)  # Drehe um 90 Grad nach links

        for cow in self.cows:
            cow.draw()

        barn_drawer.penup()
        barn_drawer.hideturtle()
        barn_drawer.goto(0, 0)  # Gehe zur Ausgangsposition

    def clean_stable(self):
        if self.cleanliness == 100:
            messagebox.showinfo("Clean Stable", "The stable is already clean.")
        else:
            self.cleanliness = 100
            messagebox.showinfo("Clean Stable", "The stable has been cleaned.")

# Define the Farm class
class Farm:
    def __init__(self):
        self.cows = []
        self.barns = []
        self.pastures = []
        self.milking_parlors = []
        self.money = 0

    def add_cow(self, cow):
        self.cows.append(cow)

    def add_barn(self, barn):
        self.barns.append(barn)

    def add_pasture(self, pasture):
        self.pastures.append(pasture)

    def add_milking_parlor(self, milking_parlor):
        self.milking_parlors.append(milking_parlor)

    def milk_cows(self):
        total_milk = 0
        money_earned = 0

        for cow in self.cows:
            if cow.is_adult():
                milk_production, fat_in_milk = cow.produce_milk()
                total_milk += milk_production
                money_earned += milk_production * MILK_PRICE_PER_LITER

        return total_milk, money_earned

    def feed_cows(self):
        for cow in self.cows:
            cow.health = 100

    def breed_cows(self):
        if len(self.cows) < 2:
            messagebox.showinfo("Breeding Cows", "You need at least 2 cows to breed.")
        else:
            parent1, parent2 = random.sample(self.cows, 2)
            breed = parent1.breed
            child = Cow(breed)
            self.add_cow(child)
            messagebox.showinfo("Breeding Cows", "A new cow has been bred.")

    def sell_milk_products(self):
        total_milk, _ = self.milk_cows()
        money_earned = total_milk * SELLING_PRICE
        self.money += money_earned
        messagebox.showinfo("Sell Milk Products", f"You earned ${money_earned} by selling {total_milk} liters of milk.")

    def clean_stable(self, barn):
        if self.money < CLEANING_COST:
            messagebox.showinfo("Clean Stable", "You don't have enough money to clean the stable.")
        else:
            self.money -= CLEANING_COST
            barn.clean_stable()
            self.update_labels()

    def upgrade_farm(self):
        if self.money < UPGRADE_COST:
            messagebox.showinfo("Upgrade Farm", "You don't have enough money to upgrade the farm.")
        else:
            self.money -= UPGRADE_COST
            messagebox.showinfo("Upgrade Farm", "Congratulations! Your farm has been upgraded.")
            self.update_labels()

    def update_labels(self):
        label_cows.config(text="Cows: " + str(len(self.cows)))
        label_barns.config(text="Barns: " + str(len(self.barns)))
        label_pastures.config(text="Pastures: " + str(len(self.pastures)))
        label_milking_parlors.config(text="Milking Parlors: " + str(len(self.milking_parlors)))
        label_total_milk.config(text="Total Milk: " + str(self.milk_cows()[0]) + " liters")
        label_money_earned.config(text="Money Earned: $" + str(self.milk_cows()[1]))
        label_money.config(text="Money: $" + str(self.money))

# Create the farm
farm = Farm()

# Create the GUI window
window = tk.Tk()
window.title("Cow Farm Game")

# Create the turtle screen
screen = Screen()
screen.title("Cow Farm Game")
screen.bgcolor("green")
screen.setup(800, 600)

# Create the barns
barn1 = Barn(-300, 0, 70)
barn1.draw()
farm.add_barn(barn1)

barn2 = Barn(-300, -150, 70)
barn2.draw()
farm.add_barn(barn2)

# Create the cows as dots
for _ in range(70):
    cow = Cow("Holstein")
    farm.add_cow(cow)
    barn1.add_cow(cow)
    cow.x = random.uniform(barn1.x - (BARN_SIZE / 2) + COW_SIZE, barn1.x + (BARN_SIZE / 2) - COW_SIZE)  # Zufällige x-Koordinate im Stallbereich
    cow.y = random.uniform(barn1.y - (BARN_SIZE / 2) + COW_SIZE, barn1.y + (BARN_SIZE / 2) - COW_SIZE)  # Zufällige y-Koordinate im Stallbereich
    cow.pen = turtle.Turtle()
    cow.pen.shape("circle")
    cow.pen.color("black")
    cow.pen.penup()
    cow.pen.goto(cow.x, cow.y)  # Setze die Startposition der Kuh auf ihre Koordinaten im Stall
    cow.pen.pendown()

# Function to update the turtle screen
def update_screen():
    screen.clear()

    for barn in farm.barns:
        barn.draw()

    screen.update()

def create_new_barn():
    x = random.randint(-300, 300)  # Zufällige x-Koordinate für den neuen Stall
    y = random.randint(-300, 300)  # Zufällige y-Koordinate für den neuen Stall
    capacity = random.randint(50, 100)  # Zufällige Kapazität für den neuen Stall
    barn = Barn(x, y, capacity)  # Erzeuge einen neuen Stall
    farm.add_barn(barn)  # Füge den neuen Stall zur Farm hinzu
    barn.draw()  # Zeichne den neuen Stal

# Function to simulate a day in the game
def simulate_day():
    farm.feed_cows()
    farm.breed_cows()
    total_milk, money_earned = farm.milk_cows()
    farm.sell_milk_products()
    for cow in farm.cows:
        cow.age_cow()
    farm.update_labels()
    update_screen()

# Function to handle the "Next Day" button click event
def next_day():
    simulate_day()

# Function to handle the "Clean Stable" button click event
def clean_stable():
    selected_barn = barn_combobox.get()
    if selected_barn == "":
        messagebox.showinfo("Clean Stable", "Please select a barn to clean.")
    else:
        barn_index = int(selected_barn) - 1
        barn = farm.barns[barn_index]
        farm.clean_stable(barn)

# Function to handle the "Upgrade Farm" button click event
def upgrade_farm():
    farm.upgrade_farm()



# Function to update the labels
def update_labels():
    label_cows.config(text="Cows: " + str(len(farm.cows)))
    label_barns.config(text="Barns: " + str(len(farm.barns)))
    label_pastures.config(text="Pastures: " + str(len(farm.pastures)))
    label_milking_parlors.config(text="Milking Parlors: " + str(len(farm.milking_parlors)))
    label_total_milk.config(text="Total Milk: " + str(farm.milk_cows()[0]) + " liters")
    label_money_earned.config(text="Money Earned: $" + str(farm.milk_cows()[1]))
    label_money.config(text="Money: $" + str(farm.money))

# Create the GUI labels
label_cows = tk.Label(window, text="Cows: " + str(len(farm.cows)))
label_cows.pack()

label_barns = tk.Label(window, text="Barns: " + str(len(farm.barns)))
label_barns.pack()

label_pastures = tk.Label(window, text="Pastures: " + str(len(farm.pastures)))
label_pastures.pack()

label_milking_parlors = tk.Label(window, text="Milking Parlors: " + str(len(farm.milking_parlors)))
label_milking_parlors.pack()

label_total_milk = tk.Label(window, text="Total Milk: " + str(farm.milk_cows()[0]) + " liters")
label_total_milk.pack()

label_money_earned = tk.Label(window, text="Money Earned: $" + str(farm.milk_cows()[1]))
label_money_earned.pack()

label_money = tk.Label(window, text="Money: $" + str(farm.money))
label_money.pack()

# Create the GUI buttons
next_day_button = tk.Button(window, text="Next Day", command=next_day)
next_day_button.pack()

clean_stable_button = tk.Button(window, text="Clean Stable", command=clean_stable)
clean_stable_button.pack()

upgrade_farm_button = tk.Button(window, text="Upgrade Farm", command=upgrade_farm)
upgrade_farm_button.pack()

new_barn_button = tk.Button(window, text="New Barn", command=create_new_barn)
new_barn_button.pack()

# Create the barn selection combobox
barn_combobox = ttk.Combobox(window)
barn_combobox['values'] = [str(i + 1) for i in range(len(farm.barns))]
barn_combobox.set("")
barn_combobox.pack()

# Start the GUI event loop
window.mainloop()
