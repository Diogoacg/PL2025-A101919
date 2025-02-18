import re

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    row_pattern = re.compile(r'^[^\s].*(?:\n\s.*)*', re.MULTILINE)
    rows = row_pattern.findall(content)
    
    headers = [header.strip() for header in rows[0].split(';')]
    num_headers = len(headers)
    
    data = []
    field_pattern = re.compile(r';(?=(?:[^"]*"[^"]*")*[^"]*$)')
    
    for row in rows[1:]:
        fields = [field.strip() for field in field_pattern.split(row)]
        
        if len(fields) != num_headers:
            print(f"Aviso: linha ignorada - esperados {num_headers} campos, encontrados {len(fields)}")
            continue
            
        data.append(fields)
    
    return headers, data

def get_composers(data):
    composers = sorted(set(row[4] for row in data if len(row) > 4))
    return composers

def get_period_distribution(data):
    period_distribution = {}
    for row in data:
        if len(row) > 3:
            period = row[3]
            if period in period_distribution:
                period_distribution[period] += 1
            else:
                period_distribution[period] = 1
    return period_distribution

def get_titles_by_period(data):
    titles_by_period = {}
    for row in data:
        if len(row) > 3:
            period = row[3]
            title = row[0]
            if period in titles_by_period:
                titles_by_period[period].append(title)
            else:
                titles_by_period[period] = [title]
    for period in titles_by_period:
        titles_by_period[period].sort()
    return titles_by_period

def main():
    file_path = 'obras.csv'

    headers, data = read_csv(file_path)
    
    composers = get_composers(data)
    print("\nLista ordenada alfabeticamente dos compositores musicais:")
    print(composers)
    
    period_distribution = get_period_distribution(data)
    print("\nDistribuição das obras por período:")
    print(period_distribution)
    
    titles_by_period = get_titles_by_period(data)
    print("\nDicionário de títulos das obras por período:")
    print(titles_by_period)

if __name__ == "__main__":
    main()