from random import random


class Item:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
  # END __init__
# END Item


class Individual:
  def __init__(self, items, chromosome=[], generation=0):
    self.items = items
    self.chromosome = chromosome
    self.generation = generation
    self.value = float('-inf') # maximize value
    self.weight = 0

    if len(chromosome) == 0:
      for _ in range(len(items)):
        if random() > 0.5:
          self.chromosome.append(1)
        else:
          self.chromosome.append(0)
  # END __init__

  def fitness(self, weight_limit):
    weight, value = 0, 0

    for i in range(len(self.chromosome)):
      if self.chromosome[i] == 1:
        weight += self.items[i].weight
        value += self.items[i].value

        if weight > weight_limit:
          self.value = float('-inf')
          return

    self.value = value
    self.weight = weight
  # END fitness

  def single_point_crossover(self, other_individual):
    midpoint = round(len(self.chromosome) / 2)

    child_chromosomes = [other_individual.chromosome[0:midpoint] + self.chromosome[midpoint:],
                        self.chromosome[0:midpoint] + other_individual.chromosome[midpoint:]]
    
    children = [Individual(self.items, child_chromosomes[0], self.generation+1),
                Individual(self.items, child_chromosomes[1], self.generation+1)]

    return children
  # END single_point_crossover

  def mutation(self, rate=0.01):
    for i in range(len(self.chromosome)):
      if random() < rate:
        if self.chromosome[i] == 0:
          self.chromosome[i] = 1
        else:
          self.chromosome[i] = 0
  # END mutation
# END Individual


class GeneticAlgorithm:
  def __init__(self):
    self.population_size = 0
    self.population = []
    self.generation = 0
    self.best_solution = None
  # END __init__

  def initialize_population(self, population_size, items):
    self.population_size = population_size
    self.items = items

    for _ in range(self.population_size):
      self.population.append(Individual(self.items))

    self.calculate_fitness()
    self.order_population()

    self.best_solution = self.population[0]
  # END initialize_population

  def calculate_fitness(self):
    for individual in self.population:
      individual.fitness(self.weight_limit)
  # END calculate_fitness

  def order_population(self):
    self.population = sorted(self.population, key=lambda individual: individual.value)
  # END order_population

  def select_best_individual(self):
    if self.population[0].value > self.best_solution.value:
      self.best_solution = self.population[0]
  # END select_best_individual

  def sum_values(self):
    sum = 0

    for individual in self.population:
      sum += individual.value

    return sum
  # END sum_values

  def select_parent_cutoff(self, sum_value):
    index = -1
    random_value = random() * sum_value

    sum, i = 0, 0
    while i < len(self.population) and sum < random_value:
      sum += self.population[i].value
      index += 1
      i += 1

    return index
  # END select_parent_cutoff

  def visualize_generation(self):
    best = self.best_solution
    print('Generation: ', self.generation,
          '- Total Value: ', best.value,
          '- Total Weight: ', best.weight,
          '- Chromosome: ', best.chromosome)
  # END visualize_generation

  def solve(self, mutation_probability, number_of_generations, population_size, weight_limit, items):
    self.weight_limit = weight_limit
    self.initialize_population(population_size, items)

    for _ in range(number_of_generations):
      sum = self.sum_values()

      new_population = []
      for _ in range(0, self.population_size, 2):
        parents = [self.select_parent_cutoff(sum),
                   self.select_parent_cutoff(sum)]
        
        children = self.population[parents[0]].single_point_crossover(self.population[parents[1]])

        children[0].mutation(mutation_probability)
        children[1].mutation(mutation_probability)

        new_population.append(children[0])
        new_population.append(children[1])

      self.population = new_population
      self.calculate_fitness()
      self.order_population()
      self.select_best_individual()

      self.generation += 1
      self.visualize_generation()

    print('\n**** Best Solution ****',
          '\nGeneration: ', self.best_solution.generation,
          '\nTotal Value: ', self.best_solution.value,
          '\nTotal Weight: ', self.best_solution.weight,
          '\nChromosome: ', self.best_solution.chromosome)

    return self.best_solution.chromosome
  # END solve
# END GeneticAlgorithm


items = []

items.append(Item('Bottle of water', 0.680389, 15))
items.append(Item('Snacks', 0.136078, 8))
items.append(Item('Hat', 0.453592, 10))
items.append(Item('Sunglasses', 0.3175147, 10))
items.append(Item('Camera', 0.907185, 9))
items.append(Item('Umbrella', 1.36078, 2))
items.append(Item('Laptop', 1.13398, 5))

mutation_probability = 0.01
number_of_generation = 1000 # optimal is 1000
population_size = 20
weight_limit = 2.5

ga = GeneticAlgorithm()

result = ga.solve(mutation_probability,
                  number_of_generation,
                  population_size,
                  weight_limit,
                  items)

print('\n**** Items Packed ****')
for i in range(len(result)):
  if result[i] == 1:
    print(items[i].name)