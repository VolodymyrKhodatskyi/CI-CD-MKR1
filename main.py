def read_txt(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            data.append((country, float(area), int(population)))
    return data



