from src.model import *
import src.gui

from src.model.evolution.evolution import main, arena, humanarena, monkeyrun, experiments

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

# list of parameter sets
params = [
    (15, 30,  0.2, 1.5, 10, 2, 5),
    ( 5, 50,  0.2, 1.5, 10, 2, 5),
    (10, 40, 0.15, 1.2, 10, 2, 5),
    (10, 40,  0.3, 1.8, 10, 2, 5)
]

# how many random genotypes
n_randoms = 200


if __name__ == '__main__':
	# run experiments
	# experiments(params, n_randoms)
	
	# in order to play as a human
	humanarena(agent_sol=[1.0,-0.5,0.8,-0.5,0.1,0.2])
