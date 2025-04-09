import random
import numpy as np

# Villes
variables_decision = [0, 1, 2, 3, 4, 5, 6]

# Distances entre les villes
distances = np.array([
    [0.00, 12.34, 45.67, 23.45, 56.78, 34.56, 29.87],
    [12.34, 0.00, 33.21, 41.23, 25.76, 48.91, 38.44],
    [45.67, 33.21, 0.00, 27.89, 36.54, 21.43, 31.32],
    [23.45, 41.23, 27.89, 0.00, 32.98, 19.76, 40.50],
    [56.78, 25.76, 36.54, 32.98, 0.00, 28.64, 44.12],
    [34.56, 48.91, 21.43, 19.76, 28.64, 0.00, 26.57],
    [29.87, 38.44, 31.32, 40.50, 44.12, 26.57, 0.00]
])

POPULATION_SIZE = 10
GENERATIONS = 5000
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

def generate_individual():
    individual = variables_decision[:]
    random.shuffle(individual)
    return individual

def initialize_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def evaluate(individual):
    return sum(distances[individual[i-1]][individual[i]] for i in range(1, len(individual)))

def roulette_wheel_selection(population):
    fitness_values = [1 / (1 + evaluate(ind)) for ind in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return random.choices(population, weights=probabilities, k=1)[0]

def tournament_selection(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return min(tournament, key=evaluate)

def crossover(parent1, parent2):
    cut = random.randint(1, len(variables_decision) - 2)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    return child

def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(selection_method="tournament"):
    population = initialize_population()

    for generation in range(GENERATIONS):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            if selection_method == "roulette":
                parent1 = roulette_wheel_selection(population)
                parent2 = roulette_wheel_selection(population)
            else:
                parent1 = tournament_selection(population)
                parent2 = tournament_selection(population)
            
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = sorted(new_population, key=evaluate)[:POPULATION_SIZE]

    best_solution = min(population, key=evaluate)
    print(f"Meilleur chemin trouvé : {best_solution}, Distance totale : {evaluate(best_solution)}")

genetic_algorithm(selection_method="tournament")