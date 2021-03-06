#!/usr/bin/env python

import random
import json
from src.model.boardgame.game import *
from src.model.boardgame.boardUtils import *


DEBUG = True
DEBUG = False


class Agent(object):
    """docstring for Agent"""
    def __init__(self, energy, name, solution):
        super(Agent, self).__init__()
        self.name = name
        self.energy = energy
        self.startingEnergy = energy
        self.solution = solution
        self.fights_won = 0
        self.fights_lost = 0

    def energy_ratio(self):
        return self.energy / float (self.startingEnergy)

    def calculateScore(self, board, color):
        score = 0
        #points are given only for my fields
        for x in range(BoardUtils.BOARD_SIZE):
            for y in range(BoardUtils.BOARD_SIZE):
                if not board[x][y] == color:
                    board[x][y] = 0
                else:
                    board[x][y] = 1
        #corners
        if board[0][0] == 1:
            score = score + self.solution[0]
        if board[BoardUtils.BOARD_SIZE-1][0] == 1:
            score = score + self.solution[0]
        if board[0][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[0]
        if board[BoardUtils.BOARD_SIZE-1][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[0]
        #next to corners, on edge
        if board[1][0] == 1:
            score = score + self.solution[1]
        if board[BoardUtils.BOARD_SIZE-1][1] == 1:
            score = score + self.solution[1]
        if board[0][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[1]
        if board[BoardUtils.BOARD_SIZE-1][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[1]
        if board[0][1] == 1:
            score = score + self.solution[1]
        if board[BoardUtils.BOARD_SIZE-2][0] == 1:
            score = score + self.solution[1]
        if board[1][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[1]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[1]
        #next field on edge
        if board[2][0] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-1][2] == 1:
            score = score + self.solution[2]
        if board[0][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-1][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[2]
        if board[0][2] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-3][0] == 1:
            score = score + self.solution[2]
        if board[2][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[2]
        #middle field on edge #changed solution index from 3 to 2 [unified these fields]
        if board[3][0] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-1][3] == 1:
            score = score + self.solution[2]
        if board[0][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-1][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[2]
        if board[0][3] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-4][0] == 1:
            score = score + self.solution[2]
        if board[3][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[2]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[2]
        #next to corner, inside #changed solution index from 4 to 3
        if board[1][1] == 1:
            score = score + self.solution[3]
        if board[BoardUtils.BOARD_SIZE-2][1] == 1:
            score = score + self.solution[3]
        if board[1][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[3]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[3]
        #next field... #changed solution index from 5 to 4 [unified these fields]
        if board[1][2] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-2][2] == 1:
            score = score + self.solution[4]
        if board[1][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[4]
        if board[2][1] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-3][1] == 1:
            score = score + self.solution[4]
        if board[2][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[4]
        #next field... #changed solution index from 6 to 4 [unified these fields]
        if board[1][3] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-2][3] == 1:
            score = score + self.solution[4]
        if board[1][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[4]
        if board[3][1] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-4][1] == 1:
            score = score + self.solution[4]
        if board[3][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[4]
        #on the diameter #changed solution index from 7 to 4 [unified these fields]
        if board[2][2] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-3][2] == 1:
            score = score + self.solution[4]
        if board[2][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[4]
        #next field... #changed solution index from 8 to 4 [unified these fields]
        if board[2][3] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-3][3] == 1:
            score = score + self.solution[4]
        if board[2][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[4]
        if board[3][2] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-4][2] == 1:
            score = score + self.solution[4]
        if board[3][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[4]
        #middle #changed solution index from 9 to 5
        if board[3][3] == 1:
            score = score + self.solution[5]
        if board[BoardUtils.BOARD_SIZE-4][3] == 1:
            score = score + self.solution[5]
        if board[3][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[5]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[5]
        return score
            


    # callback letting the agent play the game
    def move(self, board, color):
        bestMove = None
        bestMoveScore = -10000000
        for x in range (BoardUtils.BOARD_SIZE):
            for y in range (BoardUtils.BOARD_SIZE):
                if BoardUtils.isLegalMove([x,y], board, color):
                     score = self.calculateScore(BoardUtils.applyMove([x,y], board, color), color)
                     if (bestMoveScore < score or bestMove == None):
                        bestMove = [x,y]
                        bestMoveScore = score
        return bestMove

    def __str__(self):
        return 'A#' + self.name + " | En: " + str(self.energy) + ' | ' + str(self.solution)


class Algorithm(object):
    """docstring for Algorithm"""
    def __init__(self, **kw):
        super(Algorithm, self).__init__()
        self.population = []
        self.last_agent_id = -1
        self.empty_solution = []

        self.starting_energy = kw.get('STARTING_ENERGY', 10)
        self.population_size = kw.get('POPULATION_SIZE', 12)
        self.iterations = kw.get('ITERATIONS', 30)

        self.REPRODUCTION_THRESH = kw.get('REPRODUCTION_THRESH', 1.5)
        self.FIGHT_ENERGY = kw.get('FIGHT_ENERGY', 2)
        self.REPRODUCTION_ENERGY = kw.get('REPRODUCTION_ENERGY', 5)
        self.MUTATION_SEED = kw.get('MUTATION_SEED', 0.2)

    def random_solution(self):
        new_solution = []
        for i in range(6):
            new_solution.append(random.uniform(-1.0,1.0))
        return new_solution

    def mutate(self, solution):
        mutated = []
        for i in solution:
            i=i+random.uniform(-1*self.MUTATION_SEED, self.MUTATION_SEED)
            if i < -1.0:
                i = -1.0
            if i > 1.0:
                i = 1.0
            mutated.append(i)
        return mutated

    def child_solutions(self, sol1, sol2, prob = 0.5):
        new_solution1 = []
        new_solution2 = []
        for i in range(len(sol1)):
            if random.random() < prob:
                new_solution1.append(sol1[i])
                new_solution2.append(sol2[i])
            else:
                new_solution1.append(sol2[i])
                new_solution2.append(sol1[i])
        return [self.mutate(new_solution1), self.mutate(new_solution2)]

    def generate_solution(self, energy=None, solution=None):
        if solution is None:
            solution = self.random_solution()
            if DEBUG: print solution
        if energy is None:
            energy = self.starting_energy
        new_agent = Agent(energy, str(self.last_agent_id + 1), solution)
        self.last_agent_id += 1
        return new_agent

    def generate_population(self):
        self.population = [self.generate_solution() for _ in range(self.population_size)]
    
    def run(self):
        for i in range(self.iterations):
            if DEBUG: print '---'
            if DEBUG: print 'step ' + str(i)
            if i % 10 == 0: print i,
            self.step()
        print

    def step(self):
        reproduction_pool = []
        fighting_pool = []

        for agent in self.population:
            if agent.energy_ratio() > self.REPRODUCTION_THRESH:
                reproduction_pool.append(agent)
            else:
                fighting_pool.append(agent)

        if DEBUG: print 'reproduction_pool: ' + str(len(reproduction_pool))
        if DEBUG: print 'fighting_pool: ' + str(len(fighting_pool))

        for ag1, ag2 in self.get_pair_from_pool(reproduction_pool):
            self.reproduce(ag1, ag2)
        
        for ag1, ag2 in self.get_pair_from_pool(fighting_pool):
            self.fight(ag1, ag2)

    
        # remove dead solutions
        if DEBUG: print 'pop size: ' + str(len(self.population))
        self.population = [agent for agent in self.population if agent.energy > 0]
        if DEBUG: print 'alive pop size: ' + str(len(self.population))


    def get_pair_from_pool(self, pool):
        random.shuffle(pool)
        size = len(pool)
        size = size if size % 2 == 0 else size-1
        i = 0
        while i < size:
            yield pool[i], pool[i+1]
            i += 2

    def reproduce(self, agent1, agent2):
        child_solutions = self.child_solutions(agent1.solution, agent2.solution)#, agent1.energy/(0.0 + agent1.energy + agent2.energy))
        if DEBUG: 
            print 'PARENTS:'
            print agent1.solution
            print agent2.solution
            print 'CHILDREN:'
            print child_solutions[0]
            print child_solutions[1]
        agent1.energy = agent1.energy - self.REPRODUCTION_ENERGY
        agent2.energy = agent2.energy - self.REPRODUCTION_ENERGY
        self.population.append(self.generate_solution(energy=self.REPRODUCTION_ENERGY, solution=child_solutions[0]))
        self.population.append(self.generate_solution(energy=self.REPRODUCTION_ENERGY, solution=child_solutions[1]))

    
    def fight(self, agent1, agent2):
        game = Game(agent1, agent2)
        try:
            game.play()
            if not game.getWinner() == None:
                self.transfer_energy(game.getLoser(), game.getWinner(), self.FIGHT_ENERGY)
        except IllegalMoveException as e:
            print e

    def transfer_energy(self, from_agent, to_agent, energy_amount):
        energy_amount = min(energy_amount, from_agent.energy)
        from_agent.energy -= energy_amount
        from_agent.fights_lost = from_agent.fights_lost + 1
        to_agent.energy += energy_amount
        to_agent.fights_won = to_agent.fights_won + 1

    def take_best_win_ratio(self):
        self.population = sorted(self.population, key=lambda ag: ag.fights_won/(ag.fights_won+ag.fights_lost+2), reverse=True)#constant added to push those who won i.e 1 fight and lost none lower
        return self.population

    def take_best_energy(self):
        self.population = sorted(self.population, key=lambda ag: ag.energy, reverse=True)
        return self.population

    def print_solutions(self):
        for solution in self.population:
            print solution


def main():
    alg = Algorithm()
    alg.generate_population()
    alg.print_solutions()
    alg.run()
    best_ratio = alg.take_best_win_ratio()
    print 'BEST ratio:'
    alg.print_solutions()
    dumb = VeryDumbPlayer("Stach")
    game = Game (best_ratio[0], dumb)
    game.play()
    print 'WINNER: ',game.getWinner()
    best_energy = alg.take_best_energy()
    print 'BEST energy:'
    alg.print_solutions()
    dumb = VeryDumbPlayer("Stach")
    game = Game (best_energy[0], dumb)
    game.play()
    print 'WINNER: ',game.getWinner()



def arena():
    winning_sol = [0.5297582973441479, -0.18090435710351122, 0.806078127357504, 0.11273029578377121, 0.22446989193277034, 0.3408969647586671]
    dumb = VeryDumbPlayer("test")
    agent = Agent(10, "agent", winning_sol)
    game = Game (agent, dumb)
    game.play()
    print "WINNER:", game.getWinner()


def humanarena(agent_sol=[1.0,-0.5,0.8,-0.5,0.1,0.2]):
    # winning_sol = [0.5297582973441479, -0.18090435710351122, 0.806078127357504, 0.11273029578377121, 0.22446989193277034, 0.3408969647586671]
    # winning_sol2 = [0.8431720537249556, -0.4896664324024035, 0.9398321632961153, -1.0, 0.002145266660614681, -0.3451639380375208]
    # perfect_sol = [1.0,-0.5,0.8,-0.5,0.1,0.2]
    human = HumanPlayer("human")
    agent = Agent(10, "agent", agent_sol)
    game = Game (human,agent)
    game.play()
    print "WINNER:", game.getWinner()


def monkeyrun(n):
    perfect_sol = [1.0,-0.5,0.8,-0.5,0.1,0.2]
    perfect = Agent(10, "Mr. Perfect", perfect_sol)
    alg = Algorithm()
    draws = []
    fails = []
    for i in range(n):
        candidate = Agent(10, "Mr. Random", alg.random_solution())
        game = Game(perfect, candidate)
        game.play()
        winner = game.getWinner()
        if winner == None:
            draws.append(candidate)
        elif winner != perfect:
            fails.append(winner)
    print 'Lost to:'
    for agent in fails:
        print agent
    print 'Drew with:'
    for agent in draws:
        print agent
    solutions = [agent.solution for agent in fails]
    print perfect, "Won", n - len(fails), "out of", n
    # mean = [sum(group)/len(group) for group in zip(*solutions)]
    # print 'mean:', mean


def get_evolved_agents(params_dict):
    alg = Algorithm(**params_dict)
    alg.generate_population()
    if DEBUG: alg.print_solutions()
    alg.run()
    best_ratio = alg.take_best_win_ratio()[0]
    best_energy = alg.take_best_energy()[0]
    return best_ratio, best_energy

def benchmark_randoms(n_agents, tested_agent):
    alg = Algorithm()
    draws = []
    fails = []
    print "benchmarking against %d randoms. agent:" % n_agents
    print tested_agent
    for i in range(n_agents):
        if i % 10 == 0: print i,
        candidate = Agent(10, "Mr. Random", alg.random_solution())
        game = Game(tested_agent, candidate)
        game.play()
        winner = game.getWinner()
        if winner is None:
            draws.append(candidate)
        elif str(winner) != str(tested_agent):
            fails.append(winner)
    print
    won = n_agents - len(fails) - len(draws)
    if DEBUG: print tested_agent
    if DEBUG: print "Won:", won, "/", n_agents
    return float(won)/n_agents


def experiments(params, n_randoms):
    params_names = [
        'POPULATION_SIZE',
        'ITERATIONS',
        'MUTATION_SEED', # mutated dimension +/- random(0,MUTATION_SEED)
        'REPRODUCTION_THRESH', # energy / starting energy
        'STARTING_ENERGY',
        'FIGHT_ENERGY', # energy transferred during fights
        'REPRODUCTION_ENERGY' # energy transferred during reproductions
    ]
    # params = [
    #     (15, 30,  0.2, 1.5, 10, 2, 5),
    #     ( 5, 50,  0.2, 1.5, 10, 2, 5),
    #     (10, 40, 0.15, 1.2, 10, 2, 5),
    #     (10, 40,  0.3, 1.8, 10, 2, 5)
    # ]
    # n_randoms = 200
    '''
    [(params_dict, best_ratio_agent, best_energy_agent), ...]
    '''
    agent_tuples = []

    for pars in params:
        params_dict = dict(zip(params_names, pars))
        print params_dict
        print 'evolving:'
        agents = get_evolved_agents(params_dict)
        agent_tuples.append((params_dict, agents))

    results_randoms = {}
    for params_dict, (ratio_agent, energy_agent) in agent_tuples:
        pars = json.dumps(params_dict)
        perf_ratio = benchmark_randoms(n_randoms, ratio_agent)
        perf_energy = benchmark_randoms(n_randoms, energy_agent)
        perfs = {'ratio': perf_ratio, 'energy': perf_energy}
        results_randoms[pars] = perfs

    print '######'
    for params, perfs in results_randoms.items():
        print '###'
        print params
        print perfs



if __name__ == '__main__':
    # main()
    params_names = [
        'POPULATION_SIZE',
        'ITERATIONS',
        'MUTATION_SEED', # mutated dimension +/- random(0,MUTATION_SEED)
        'REPRODUCTION_THRESH', # energy / starting energy
        'STARTING_ENERGY',
        'FIGHT_ENERGY', # energy transferred during fights
        'REPRODUCTION_ENERGY' # energy transferred during reproductions
    ]
    params = [
        (15, 30,  0.2, 1.5, 10, 2, 5),
        ( 5, 50,  0.2, 1.5, 10, 2, 5),
        (10, 40, 0.15, 1.2, 10, 2, 5),
        (10, 40,  0.3, 1.8, 10, 2, 5)
    ]
    n_randoms = 200
    experiments(params, n_randoms)
