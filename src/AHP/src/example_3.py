from itertools import combinations
from pprint import pprint  # noqa

from ahpy import Compare

criteria_comparisons = {
    ('Cost', 'Safety'): 3,
    ('Cost', 'Style'): 7,
    ('Cost', 'Capacity'): 3,
    ('Safety', 'Style'): 9,
    ('Safety', 'Capacity'): 1,
    ('Style', 'Capacity'): 1/7
}

criteria = Compare('Criteria', criteria_comparisons, precision=3)
#report = criteria.report(show=True)

cost_comparisons = {
    ('Price', 'Fuel'): 2,
    ('Price', 'Maintenance'): 5,
    ('Price', 'Resale'): 3,
    ('Fuel', 'Maintenance'): 2,
    ('Fuel', 'Resale'): 2,
    ('Maintenance', 'Resale'): 1/2
}

capacity_comparisons = {('Cargo', 'Passenger'): 1/5}

vehicles = ('Accord Sedan', 'Accord Hybrid', 'Pilot', 'CR-V', 'Element', 'Odyssey')
vehicle_pairs = list(combinations(vehicles, 2))
#print(vehicle_pairs)

price_values = (9, 9, 1, 1/2, 5, 1, 1/9, 1/9, 1/7, 1/9, 1/9, 1/7, 1/2, 5, 6)
price_comparisons = dict(zip(vehicle_pairs, price_values))

safety_values = (1, 5, 7, 9, 1/3, 5, 7, 9, 1/3, 2, 9, 1/8, 2, 1/8, 1/9)
safety_comparisons = dict(zip(vehicle_pairs, safety_values))

passenger_values = (1, 1/2, 1, 3, 1/2, 1/2, 1, 3, 1/2, 2, 6, 1, 3, 1/2, 1/6)
passenger_comparisons = dict(zip(vehicle_pairs, passenger_values))

fuel_values = (1/1.13, 1.41, 1.15, 1.24, 1.19, 1.59, 1.3, 1.4, 1.35, 1/1.23, 1/1.14, 1/1.18, 1.08, 1.04, 1/1.04)
fuel_comparisons = dict(zip(vehicle_pairs, fuel_values))

resale_values = (3, 4, 1/2, 2, 2, 2, 1/5, 1, 1, 1/6, 1/2, 1/2, 4, 4, 1)
resale_comparisons = dict(zip(vehicle_pairs, resale_values))

maintenance_values = (1.5, 4, 4, 4, 5, 4, 4, 4, 5, 1, 1.2, 1, 1, 3, 2)
maintenance_comparisons = dict(zip(vehicle_pairs, maintenance_values))

style_values = (1, 7, 5, 9, 6, 7, 5, 9, 6, 1/6, 3, 1/3, 7, 5, 1/5)
style_comparisons = dict(zip(vehicle_pairs, style_values))

cargo_values = (1, 1/2, 1/2, 1/2, 1/3, 1/2, 1/2, 1/2, 1/3, 1, 1, 1/2, 1, 1/2, 1/2)
cargo_comparisons = dict(zip(vehicle_pairs, cargo_values))

cost = Compare('Cost', cost_comparisons, precision=3)
capacity = Compare('Capacity', capacity_comparisons, precision=3)
price = Compare('Price', price_comparisons, precision=3)
safety = Compare('Safety', safety_comparisons, precision=3)
passenger = Compare('Passenger', passenger_comparisons, precision=3)
fuel = Compare('Fuel', fuel_comparisons, precision=3)
resale = Compare('Resale', resale_comparisons, precision=3)
maintenance = Compare('Maintenance', maintenance_comparisons, precision=3)
style = Compare('Style', style_comparisons, precision=3)
cargo = Compare('Cargo', cargo_comparisons, precision=3)

cost.add_children([price, fuel, maintenance, resale])
capacity.add_children([cargo, passenger])
criteria.add_children([cost, safety, style, capacity])

#pprint(criteria.target_weights)
report = criteria.report(show=True)
#report = cost.report(show=True)
#report = price.report(show=True)
