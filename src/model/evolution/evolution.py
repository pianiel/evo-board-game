#!/usr/bin/env python

import random
from src.model.boardgame.game import *
from src.model.boardgame.boardUtils import *


class Agent(object):
    """docstring for Agent"""
    def __init__(self, energy, name, solution):
        super(Agent, self).__init__()
        self.name = name
        self.energy = energy
        self.startingEnergy = energy
        self.solution = solution

    def energy_ratio(self):
        # 0 <= ratio <= 1
        # TODO energy dependent ratio
        #return random.random()
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
        #middle field on edge
        if board[3][0] == 1:
            score = score + self.solution[3]
        if board[BoardUtils.BOARD_SIZE-1][3] == 1:
            score = score + self.solution[3]
        if board[0][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[3]
        if board[BoardUtils.BOARD_SIZE-1][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[3]
        if board[0][3] == 1:
            score = score + self.solution[3]
        if board[BoardUtils.BOARD_SIZE-4][0] == 1:
            score = score + self.solution[3]
        if board[3][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[3]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-1] == 1:
            score = score + self.solution[3]
        #next to corner, inside
        if board[1][1] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-2][1] == 1:
            score = score + self.solution[4]
        if board[1][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[4]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[4]
        #next field...
        if board[1][2] == 1:
            score = score + self.solution[5]
        if board[BoardUtils.BOARD_SIZE-2][2] == 1:
            score = score + self.solution[5]
        if board[1][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[5]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[5]
        if board[2][1] == 1:
            score = score + self.solution[5]
        if board[BoardUtils.BOARD_SIZE-3][1] == 1:
            score = score + self.solution[5]
        if board[2][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[5]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[5]
        #next field...
        if board[1][3] == 1:
            score = score + self.solution[6]
        if board[BoardUtils.BOARD_SIZE-2][3] == 1:
            score = score + self.solution[6]
        if board[1][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[6]
        if board[BoardUtils.BOARD_SIZE-2][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[6]
        if board[3][1] == 1:
            score = score + self.solution[6]
        if board[BoardUtils.BOARD_SIZE-4][1] == 1:
            score = score + self.solution[6]
        if board[3][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[6]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-2] == 1:
            score = score + self.solution[6]
        #on the diameter
        if board[2][2] == 1:
            score = score + self.solution[7]
        if board[BoardUtils.BOARD_SIZE-3][2] == 1:
            score = score + self.solution[7]
        if board[2][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[7]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[7]
        #next field...
        if board[2][3] == 1:
            score = score + self.solution[8]
        if board[BoardUtils.BOARD_SIZE-3][3] == 1:
            score = score + self.solution[8]
        if board[2][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[8]
        if board[BoardUtils.BOARD_SIZE-3][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[8]
        if board[3][2] == 1:
            score = score + self.solution[8]
        if board[BoardUtils.BOARD_SIZE-4][2] == 1:
            score = score + self.solution[8]
        if board[3][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[8]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-3] == 1:
            score = score + self.solution[8]
        #middle
        if board[3][3] == 1:
            score = score + self.solution[9]
        if board[BoardUtils.BOARD_SIZE-4][3] == 1:
            score = score + self.solution[9]
        if board[3][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[9]
        if board[BoardUtils.BOARD_SIZE-4][BoardUtils.BOARD_SIZE-4] == 1:
            score = score + self.solution[9]
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
    def __init__(self, population_size=30, iterations=40, starting_energy=20):
        super(Algorithm, self).__init__()
        self.population_size = population_size
        self.iterations = iterations
        self.population = []
        self.last_agent_id = -1
        self.starting_energy = starting_energy

        # TODO tinker :P
        self.empty_solution = []
        self.REPRODUCTION_PROB = 1.2
        self.FIGHT_ENERGY = 5
        self.REPRODUCTION_ENERGY = 7
        self.MUTATION_SEED = 0.1

    def random_solution(self):
        new_solution = []
        for i in range(10):
            new_solution.append(random.uniform(-1.0,1.0))
        return new_solution

    def mutate(self, solution):
        for i in solution:
            i=i+random.uniform(-1*self.MUTATION_SEED, self.MUTATION_SEED)
            if i < -1.0:
                i = -1.0
            if i > 1.0:
                i = 1.0
        return solution

    def child_solution(self, sol1, sol2, prob):
        new_solution = []
        # i = random.randrange(0,10)
        # for j in range(10):
        #     if j<=i:
        #         new_solution.append(sol1[j])
        #     else:
        #         new_solution.append(sol2[j])
        print "Prob:", prob
        for i in range(len(sol1)):
            if random.random() < prob:
                new_solution.append(sol1[i])
            else:
                new_solution.append(sol2[i])
        return self.mutate(new_solution)

    def generate_solution(self, energy=None, solution=None):
        if solution is None:
            solution = self.random_solution()
            print solution
        if energy is None:
            energy = self.starting_energy
        new_agent = Agent(energy, str(self.last_agent_id + 1), solution)
        self.last_agent_id += 1
        return new_agent

    def generate_population(self):
        self.population = [self.generate_solution() for _ in range(self.population_size)]
    
    def run(self):
        for i in range(self.iterations):
            print '#####'
            print 'step ' + str(i)
            self.step()

    def step(self):
        reproduction_pool = []
        fighting_pool = []

        for agent in self.population:
            if agent.energy_ratio() > self.REPRODUCTION_PROB:
                reproduction_pool.append(agent)
            else:
                fighting_pool.append(agent)

        print 'reproduction_pool: ' + str(len(reproduction_pool))
        print 'fighting_pool: ' + str(len(fighting_pool))

        for ag1, ag2 in self.get_pair_from_pool(reproduction_pool):
            self.reproduce(ag1, ag2)
        
        for ag1, ag2 in self.get_pair_from_pool(fighting_pool):
            self.fight(ag1, ag2)

    
        # remove dead solutions
        print 'pop size: ' + str(len(self.population))
        self.population = [agent for agent in self.population if agent.energy > 0]
        print 'alive pop size: ' + str(len(self.population))


    def get_pair_from_pool(self, pool):
        random.shuffle(pool)
        size = len(pool)
        size = size if size % 2 == 0 else size-1
        i = 0
        while i < size:
            # print "next pair:", pool[i], pool[i+1]
            yield pool[i], pool[i+1]
            i += 2

    def reproduce(self, agent1, agent2):
        child_solution = self.child_solution(agent1.solution, agent2.solution, agent1.energy/(0.0 + agent1.energy + agent2.energy))
        print agent1.solution
        print agent2.solution
        print child_solution
        agent1.energy = agent1.energy - self.REPRODUCTION_ENERGY
        agent2.energy = agent2.energy - self.REPRODUCTION_ENERGY
        child_energy = 2 * self.REPRODUCTION_ENERGY
        self.population.append(self.generate_solution(energy=child_energy, solution=child_solution))

    
    def fight(self, agent1, agent2):
        game = Game(agent1, agent2)
        try:
            game.play()
            if not game.getWinner() == None:
                self.transfer_energy(game.getLoser(), game.getWinner(), self.FIGHT_ENERGY)
        except IllegalMoveException as e:
            print e

        '''if random.random() < 0.5:
            self.transfer_energy(agent1, agent2, self.FIGHT_ENERGY)
        else:
            self.transfer_energy(agent2, agent1, self.FIGHT_ENERGY)'''

    def transfer_energy(self, from_agent, to_agent, energy_amount):
        energy_amount = min(energy_amount, from_agent.energy)
        from_agent.energy -= energy_amount
        to_agent.energy += energy_amount

    def take_best(self):
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
    # alg.print_solutions()
    best = alg.take_best()
    print 'BEST:'
    alg.print_solutions()
    game = Game (best[0], VeryDumbPlayer("Stach"))
    game.play()
    print 'WINNER: ',game.getWinner()


def arena():
    winning_sol = [0.137084160956074, -0.901677335187183, -0.5749441872722376, 0.4545736864652825, -0.6748748484051388, -0.7463435804098713, -0.7544998282254556, -0.30856498877213845, 0.5810020651812795, 0.039626273905303044]
    dumb = VeryDumbPlayer("test")
    agent = Agent(10, "agent", winning_sol)
    game = Game (agent, dumb)
    game.play()
    print game.getWinner()

if __name__ == '__main__':
    main()
