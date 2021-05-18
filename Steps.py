exercise = input(
    "What kind of exercise do you want to do? \n\nOPTIONS:\n Walk\n Run\n Bike\n I'm not sure\n\n").lower()


def output_step_instructions(steps, goal):
    steps_before_turn_around = (goal-steps)//2+steps
    if exercise == 'walk':
        print(
            f'\nYou need {goal-steps} more steps. To get that many, walk until you have {steps_before_turn_around} steps and then turn around.')
    elif exercise == 'run':
        print(
            f'\nYou need {goal-steps} more steps. To get that many, run until you have {steps_before_turn_around} steps and then turn around.')


def output_step_instructions2(steps, goal):
    steps_before_turn_around = (goal-steps)//2+steps
    if exercisechoice2 == 'walk':
        print(
            f'\nYou need {goal-steps} more steps. To get that many, walk until you have {steps_before_turn_around} steps and then turn around.')
    elif exercisechoice2 == 'run':
        print(
            f'\nYou need {goal-steps} more steps. To get that many, run until you have {steps_before_turn_around} steps and then turn around.')


if exercise == 'run' or exercise == 'walk':
    steps = int(input('\nHow many steps do you have? \n'))
    goal = int(input('\nHow many steps do you need in total? \n'))
    steps_needed = goal - steps

    if exercise == 'run':
        run_speed = float(input(
            '\nWhat is your average running speed in mph? If you don\'t know, enter a 0.\n'))
        if run_speed == 0.0:
            run_speed = 4.0

        hours = float(steps_needed)/(2000.0*run_speed)
        minutes = hours * 60.0

        if minutes >= 60.0:
            minute_calc = minutes - 60.0*float(int(hours))
        else:
            minute_calc = minutes

        output_step_instructions(steps, goal)
        print(
            f'This will take around {int(hours)} hours and {round(minute_calc)} minutes.\n')

    if exercise == 'walk':
        walk_speed = float(input(
            '\nWhat is your average walking speed in mph? If you don\'t know, enter a 0.\n'))
        if walk_speed == 0.0:
            walk_speed = 3.0

        hours = float(steps_needed)/(2000.0*walk_speed)
        minutes = hours * 60.0

        if minutes >= 60.0:
            minute_calc = minutes - 60.0*float(int(hours))
        else:
            minute_calc = minutes

        output_step_instructions(steps, goal)
        print(
            f'This will take around {int(hours)} hours and {round(minute_calc)} minutes.\n')

elif exercise == 'bike':
    steps = int(input('\nHow many steps do you have? \n'))
    goal = int(input('\nHow many steps do you need in total? \n'))
    total_ride = 0.0075 * float(goal)
    hours = total_ride / 60.0

    if float(steps) >= 0.75 * float(goal):
        total_ride *= 0.25
    elif float(steps) >= 0.5 * float(goal):
        total_ride *= 0.5
    elif float(steps) >= 0.25 * float(goal):
        total_ride *= 0.75

    minute_calc = total_ride / 2.0
    hour_calc = minute_calc / 60.0

    if total_ride >= 60.0:
        minutes = total_ride - 60.0 * float(int(hours))
    else:
        minutes = total_ride
    if minute_calc >= 60.0:
        minute_calc = minute_calc - 60.0 * float(int(hour_calc))

    print(
        f'\nGo on a bike ride for {int(hours)} hours and {round(minutes)} minutes. \nTo do this, ride for {int(hour_calc)} hours and {round(minute_calc)} minutes and then turn around.\n')

elif exercise == "i'm not sure":
    steps = int(input('\nHow many steps do you have? \n'))
    goal = int(input('\nHow many steps do you need in total? \n'))
    steps_needed = goal - steps

    total_ride = 0.0075 * float(goal)
    hours = total_ride / 60.0

    walk_speed = float(input(
        '\nWhat is your average walking speed in mph? If you don\'t know, enter a 0.\n'))
    if walk_speed == 0.0:
        walk_speed = 3.1

    walk_hours = float(steps_needed)/(2000.0*walk_speed)
    walk_minutes = walk_hours * 60.0

    if walk_minutes >= 60.0:
        walk_minute_calc = walk_minutes - 60.0*float(int(walk_hours))
    else:
        walk_minute_calc = walk_minutes

    run_speed = float(input(
        '\nWhat is your average running speed in mph? If you don\'t know, enter a 0.\n'))
    if run_speed == 0.0:
        run_speed = 4.0

    run_hours = float(steps_needed)/(2000.0*run_speed)
    run_minutes = run_hours * 60.0

    if run_minutes >= 60.0:
        run_minute_calc = run_minutes - 60.0*float(int(run_hours))
    else:
        run_minute_calc = run_minutes

    if float(steps) >= 0.75 * float(goal):
        total_ride *= 0.25
    elif float(steps) >= 0.5 * float(goal):
        total_ride *= 0.5
    elif float(steps) >= 0.25 * float(goal):
        total_ride *= 0.75

    minute_calc = total_ride / 2.0
    hour_calc = minute_calc / 60.0

    if total_ride >= 60.0:
        minutes = total_ride - 60.0 * float(int(hours))
    else:
        minutes = total_ride
    if minute_calc >= 60.0:
        minute_calc = minute_calc - 60.0 * float(int(hour_calc))

    print(
        f'\nWaling will take around {int(walk_hours)} hours and {round(walk_minute_calc)} minutes.')
    print(
        f'Running will take around {int(run_hours)} hours and {round(run_minute_calc)} minutes.')
    print(
        f'Biking will take {int(hours)} hours and {round(minutes)} minutes.\n')

    exercisechoice2 = input(
        "\nWhich one do you want to do?\n\nOPTIONS: \n Walk\n Run\n Bike\n\n").lower()

    if exercisechoice2 == 'walk' or exercisechoice2 == 'run':
        output_step_instructions2(steps, goal)

    if exercisechoice2 == 'bike':
        print(
            f'Ride for {int(hour_calc)} hours and {round(minute_calc)} minutes and then turn around.\n')

else:
    print("That isn't a valid option.")

print("\nPress enter to exit.")
input()
