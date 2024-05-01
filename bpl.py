from textx import metamodel_from_file

# Importing grammar from textX file
bpl_mm = metamodel_from_file('bpl.tx')

# Creating metamodels from each sample program
bpl_program1 = bpl_mm.model_from_file('game1.bpl')
bpl_program2 = bpl_mm.model_from_file('game2.bpl')
bpl_program3 = bpl_mm.model_from_file('game3.bpl')
# Defining the interpreter and passing in the model created above
def basketballInterpreter(model):
    # Creating statsDictionary to hold game stats
    statsDictionary = {
        'points': 0,
        'turnovers': 0,
        'assists': 0,
        'offensive_rebounds': 0,
        'defensive_rebounds': 0,
        'blocks': 0,
        'fouls': 0,
        'free_throws_made': 0,
        'free_throws_attempted': 0
    }

    for command in model.commands:
        if command.__class__.__name__ == "Shot":
            if command.result == 'made':
                statsDictionary['points'] += command.points
        elif command.__class__.__name__ == "Turnover":
            statsDictionary['turnovers'] += 1
        elif command.__class__.__name__ == "Assist":
            statsDictionary['assists'] += 1
        elif command.__class__.__name__ == "Rebound":
            if command.type == 'offensive':
                statsDictionary['offensive_rebounds'] += 1
            elif command.type == 'defensive':
                statsDictionary['defensive_rebounds'] += 1
        elif command.__class__.__name__ == "Block":
            statsDictionary['blocks'] += 1
        elif command.__class__.__name__ == "FreeThrow":
            statsDictionary['free_throws_attempted'] += 1
            if command.result == 'made':
                statsDictionary['free_throws_made'] += 1
                statsDictionary['points'] += 1  # Assuming 1 point per free throw
        elif command.__class__.__name__ == "Foul":
            statsDictionary['fouls'] += 1
        elif command.__class__.__name__ == "Stats":
            print("Current Stats:")
            for stat, value in statsDictionary.items():
                print(f"{stat.replace('_', ' ').title()}: {value}")

# Running the interpreter with the loaded program
print("Running program 1:")
basketballInterpreter(bpl_program1)
print("Running program 2:")
basketballInterpreter(bpl_program2)
print("Running program 3:")
basketballInterpreter(bpl_program3)
