#!/usr/bin/env python

import random


class Agent(object):
	"""docstring for Agent"""
	def __init__(self, energy, name, solution):
		super(Agent, self).__init__()
		self.name = name
		self.energy = energy
		self.solution = solution

	def energy_ratio(self):
		# 0 <= ratio <= 1
		# TODO energy dependent ratio
		return random.random()

	def move(self, board):
		# callback letting the agent play the game
		# TODO
		pass

	def __str__(self):
		return 'A#' + self.name + " | En: " + str(self.energy) + ' | ' + str(self.solution)


class Algorithm(object):
	"""docstring for Algorithm"""
	def __init__(self, population_size=5, iterations=5, starting_energy=10):
		super(Algorithm, self).__init__()
		self.population_size = population_size
		self.iterations = iterations
		self.population = []
		self.last_agent_id = -1
		self.starting_energy = starting_energy

		# TODO tinker :P
		self.empty_solution = []
		self.REPRODUCTION_PROB = 0.2
		self.FIGHT_ENERGY = 3

	def random_solution(self):
		# TODO fix
		return self.empty_solution[:]

	def child_solution(self, sol1, sol2):
		# TODO fix
		return self.empty_solution[:]

	def generate_solution(self, energy=None, solution=None):
		if solution is None:
			solution = self.random_solution() 
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
			if agent.energy_ratio() < self.REPRODUCTION_PROB:
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
		child_solution = self.child_solution(agent1.solution, agent2.solution)
		child_energy = (agent1.energy + agent2.energy)/2
		self.population.append(self.generate_solution(energy=child_energy, solution=child_solution))

	
	def fight(self, agent1, agent2):
		if random.random() < 0.5:
			self.transfer_energy(agent1, agent2, self.FIGHT_ENERGY)
		else:
			self.transfer_energy(agent2, agent1, self.FIGHT_ENERGY)

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
	alg.take_best()
	print 'BEST:'
	alg.print_solutions()


if __name__ == '__main__':
	main()