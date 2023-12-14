input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n\n')

def get_int_map(input):
  return [list(group) for group in list(map(lambda x: map(int, x.split()), input.split("\n")[1:]))]

def is_match(target, source, destination, delta):
  if source <= target and target <= source + delta - 1:
    diff = target - source
    return destination + diff
  return None

def get_corresponds(source, map):
  for t in map:
    match = is_match(source, t[1], t[0], t[2])
    if match is not None:
      return match
  return source

# part one
# seeds = list(map(int, input_data[0].split(": ")[1].split()))

# seed_to_soils = get_int_map(input_data[1])
# soil_to_fertilizers = get_int_map(input_data[2])
# fertilizer_to_waters = get_int_map(input_data[3])
# water_to_lights = get_int_map(input_data[4])
# lights_to_temperatures = get_int_map(input_data[5])
# temperature_to_humidities = get_int_map(input_data[6])
# humidity_to_locations = get_int_map(input_data[7])

# min = None
# for seed in seeds:
#   soil = get_corresponds(seed, seed_to_soils)
#   fertilizer = get_corresponds(soil, soil_to_fertilizers)
#   water = get_corresponds(fertilizer, fertilizer_to_waters)
#   light = get_corresponds(water, water_to_lights)
#   temperature = get_corresponds(light, lights_to_temperatures)
#   humidity = get_corresponds(temperature, temperature_to_humidities)
#   location = get_corresponds(humidity, humidity_to_locations)

#   if min is None or min > location:
#     min = location

# print('MIN_LOCATION: %d' % min)

# part two
parsed = list(map(int, input_data[0].split(": ")[1].split()))
seed_ranges = [parsed[i:i + 2] for i in range(0, len(parsed), 2)]

seed_to_soils = get_int_map(input_data[1])
soil_to_fertilizers = get_int_map(input_data[2])
fertilizer_to_waters = get_int_map(input_data[3])
water_to_lights = get_int_map(input_data[4])
lights_to_temperatures = get_int_map(input_data[5])
temperature_to_humidities = get_int_map(input_data[6])
humidity_to_locations = get_int_map(input_data[7])

min = None
for seed_range in seed_ranges:
  for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
    soil = get_corresponds(seed, seed_to_soils)
    fertilizer = get_corresponds(soil, soil_to_fertilizers)
    water = get_corresponds(fertilizer, fertilizer_to_waters)
    light = get_corresponds(water, water_to_lights)
    temperature = get_corresponds(light, lights_to_temperatures)
    humidity = get_corresponds(temperature, temperature_to_humidities)
    location = get_corresponds(humidity, humidity_to_locations)

    if min is None or min > location:
      min = location

print('MIN_LOCATION: %d' % min)
