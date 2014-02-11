from src.model import *
import src.gui

from src.model.evolution.evolution import main, arena, humanarena, monkeyrun, experiments
# from src.gui.tkinter_demo import main

'''
params_names = [
    'POPULATION_SIZE',
    'ITERATIONS',
    'MUTATION_SEED', # mutated dimension +/- random(0,MUTATION_SEED)
    'REPRODUCTION_THRESH', # energy / starting energy
    'STARTING_ENERGY',
    'FIGHT_ENERGY', # energy transferred during fights
    'REPRODUCTION_ENERGY' # energy transferred during reproductions
]
'''

params = [
    (15, 30,  0.2, 1.5, 10, 2, 5),
    ( 5, 50,  0.2, 1.5, 10, 2, 5),
    (10, 40, 0.15, 1.2, 10, 2, 5),
    (10, 40,  0.3, 1.8, 10, 2, 5)
]
n_randoms = 200


if __name__ == '__main__':
	# main()
	# arena()
	# humanarena()
	# monkeyrun(50)
	experiments(params, n_randoms)
