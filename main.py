def read_txt(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            data.append((country, float(area), int(population)))
    return data

def sort_area(data):
    return sorted(data, key=lambda x: x[1])

def sort_population(data):
    return sorted(data, key=lambda x: x[2])

data = read_txt("testtext.txt")
print(sort_area(data))
print(sort_population(data))


