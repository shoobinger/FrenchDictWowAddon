import csv
import sys
import itertools

words = []

with open(sys.argv[1], newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        orig = row[0]

        term = orig.lower()
        # Remove accents from the original word.
        term = term.replace('à', 'a')
        term = term.replace('è', 'e')
        term = term.replace('ì', 'i')
        term = term.replace('ò', 'o')
        term = term.replace('ù', 'u')
        term = term.replace('ç', 'c')
        term = term.replace('é', 'e')
        term = term.replace('â', 'a')
        term = term.replace('ê', 'e')
        term = term.replace('î', 'i')
        term = term.replace('ô', 'o')
        term = term.replace('û', 'u')
        term = term.replace('ë', 'e')
        term = term.replace('ï', 'i')
        term = term.replace('ü', 'u')
        words.append((term, orig, row[3]))

with open('DB.lua', 'w', encoding='utf-8') as output:
    output.write('words = {\n')
    
    grouped_by_search_term = itertools.groupby(sorted(words, key=lambda x: x[0]), lambda x: x[0])
    for search_term, definitions in grouped_by_search_term:        
        grouped_by_orig = itertools.groupby(sorted(definitions, key=lambda x: x[1]), lambda x: x[1])
        def_str = ', '.join('"' + orig + ': ' + ', '.join(set(d[2] for d in defs)) + '"' for orig, defs in grouped_by_orig)
        output.write(f'    ["{search_term}"] = {{ {def_str} }},\n')

    output.write('}')