# What is a genetic algorithm?
- It's an algorithm that utilizes gene sequences and simulated populations to arrive at a solution to the presented problem

## Gene Sequences
- ATCGGTGACTATCG - real gene example
- 01101001001011 - simulated gene (0 off, 1 on)
- 748b56c6b3a939 - simulated gene (weight [0:2], color [2:9], position [9:])

## Example problem
- Loading items in a backpack for a day out
  - Carrier can only handle so much weight
  - Maximize weight limit utilized
  - Maximize value added of items
- Weight limit: 2.5 kg
- Items
  - Bottle of water
    - Weight: 0.680389 kg
    - Value:  15
  - Snacks
    - Weight: 0.136078 kg
    - Value:  8
  - Hat
    - Weight: 0.453592 kg
    - Value:  10
  - Sunglasses
    - Weight: 0.3175147 kg
    - Value:  10
  - Camera
    - Weight: 0.907185 kg
    - Value:  9
  - Umbrella
    - Weight: 1.36078 kg
    - Value:  2
  - Laptop
    - Weight: 1.13398 kg
    - Value: 5
- Total weight of items: 4.9895187 kg
- Example combination
  - [0, 1, 1, 0, 0, 1, 0]
    - Snacks, Hat, Umbrella
    - Total weight: 1.95045 kg
    - Total value: 20
  - [1, 1, 0, 1, 0, 0, 1]
    - Bottle of water, Snacks, Sunglasses, Laptop
    - Total weight: 2.2679617 kg
    - Total value: 38

## Pieces of genetic algorithm
- Individual
  - This is a single genetic combination
- Population
  - Group of individuals
- Generation
  - Current population
- Constraint(s)
  - Some piece of information for which to account when analzying the value of a solution
- Value to optimize
  - Known as cost, this is the value for which you want to maximize or minimize