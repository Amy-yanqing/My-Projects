"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Yanqing Zhong (Amy)
Date started:28/04

Pseudocode:

Pseudocode for main function
--------------
function main()
    display instruction
    display choice of loading plants.txt file (Y/n).
    get choice of loading file
        if choice != 'N'
            open "plants.txt" as file_in for reading
            get plants from file_in
            close file_in
        else
            get plants list

    display total days, plants ,food
    display choice menu

    get choice
    while choice != 'Q'
        if choice == 'W'
            call function  simulate_a_day()
        else if choice == 'D'
            call function  display_garden_plants()
        else if choice == 'A'
            call function  add_plants()
        else choice
            display invalid choice
            display total days, plants ,food
        display choice menu
        get choice
    call quit_choice function
--------------------------------------------
Pseudocode for simulate_a_day function

simulate_a_day function

def simulate_a_day(day, total_food):
    actual_rainfall = random.randint(0, MAXIMUM_RAIN)
    rainfall = random.randint(int(actual_rainfall * RANDOM_RATE), actual_rainfall)
    day += 1
    display rainfall
    if len(plants) > 0:
        if rainfall < PLANT_MINIMUM_SURVIVAL_RAIN:
            died_plant_index = int(random.randint(0, len(plants) - 1))
            display died plant
            delete died plant
        for each plant in plants
            food = rainfall / MAXIMUM_RAIN * len(plant)
            total_food += food
            display each plant and each plant food produced
    display total days, plants ,food
    return day, total food

    """

import random

plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
CHOICE_MENU = "(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit"
MAXIMUM_RAIN = 128
PLANT_MINIMUM_SURVIVAL_RAIN = 32
RANDOM_RATE = 1 / 3


def main():
    """ simulate a rainy day in garden, calculate the amounts of food garden plants generated,
    and determine use generated food to buy new plants or not"""
    total_food = 0
    day = 0
    get_garden_instruction()
    get_plants_file()  # loading a plants file
    display_plants(day, total_food)  # displaying all the plants
    print(CHOICE_MENU)
    choice = input("choose: ").upper()
    while choice != "Q":
        if choice == "W":
            day, total_food = simulate_a_day(day, total_food)
        elif choice == "D":
            choice_to_display_plants(day, total_food)
        elif choice == "A":
            total_food = add_plants(day, total_food)
        else:
            print("Invalid choice")
            display_plants(day, total_food)
        print(CHOICE_MENU)
        choice = input("choose: ").upper()
    quit_choice(day, total_food)  # choice"Q"function


def get_garden_instruction():
    """displaying the plants cost and generate food instruction"""
    print("Welcome to my garden. Plants cost and generate food ")
    print("according to their name length(e.g.,Sage plants cost 4).")
    print("You can buy new plants with the food your garden generates.")
    print("You get up to 128mm of rain per day. Not all plants can survive with less than 32.Enjoy :)")


def get_plants_file():
    """ loading plant line from file append to plant list"""
    get_plants_txt = input("Would you like to load your plants from plants.txt(Y/n)? ").upper()

    if get_plants_txt != "N":
        in_file = open("plants.txt", "r")
        print(f"You start with these plants:")
        for line in in_file:
            print(line.strip("\n"), ',', end=" ")
        in_file.close()
    else:
        print(f"You start with these plants:")
        print(", ".join(plants))


def display_plants(day, total_food):
    """displaying the numbers of plants and the numbers of food in garden for the day"""
    print(f"\nAfter {day} days, you have {len(plants)}"
          f" plants and your total food is {total_food}")


def simulate_a_day(day, total_food):
    """Simulate a day, get random rainfall to generate food,
     if rainfall < minimum plant survival rain, delete a random plant in the garden"""
    actual_rainfall = random.randint(0, MAXIMUM_RAIN)  # get rainfall within the range of maximum rain
    rainfall = random.randint(int(actual_rainfall * RANDOM_RATE), actual_rainfall)  # from rainfall get random rainfall
    day += 1
    print("Rainfall:", rainfall)
    if len(plants) > 0:  # Exit the function when no plants are available
        if rainfall < PLANT_MINIMUM_SURVIVAL_RAIN:
            died_plant_index = int(random.randint(0, len(plants) - 1))  # determine index of randomly dead plants
            print(f"Sadly, your plant  {plants[died_plant_index]} has died.")
            del plants[died_plant_index]  # remove randomly dead plants

        for plant in plants:  # get plant from plants
            food = int(rainfall / MAXIMUM_RAIN * len(plant))  # food produced
            total_food += food  # food produced total
            print(f"{plant} produced {food:<4}", end="")
    display_plants(day, total_food)
    return day, total_food


def choice_to_display_plants(day, total_food):
    """displaying all the plants in garden"""
    print(f"{', '.join(plants)}")
    display_plants(day, total_food)


def add_plants(day, total_food):
    """ add new plants"""
    plant = input("Enter plant name : ").title()
    while plant != "":
        if plant not in plants:
            if total_food >= len(plant):
                plants.append(plant)  # add new plant to plants
                total_food -= len(plant)  # calculate food balance
                display_plants(day, total_food)
                break  # finish adding new plants, back to main function
            else:
                print(f"{plant} would cost {len(plant)} food. with only {total_food} food, you can't afford it")
                display_plants(day, total_food)
                break  # finish adding new plants, back to main function
        else:
            print(f"you already have a {plant} plant")
        plant = input("Enter plant name: ").title()
    return total_food


def quit_choice(day, total_food):
    """finish simulate a day, determine save plants data or not"""
    if len(plants) != 0:
        print(f"You finished with these plants: {', '.join(plants)}", "Now I Have Lots")
        display_plants(day, total_food)
        is_saved = input("Would you like to save your plants to plants.txt(Y/n)?").upper()
        if is_saved != "N":  # if not "N", any others input always is saved
            out_file = open("plants.txt", "w")
            for plant in plants:  # save plants to file
                print(plant, file=out_file)
            print("Saved")
            out_file.close()
        print("Thank you for simulating. Now enjoy some real plants.")
    else:
        print("You finished with no plants")


main()
