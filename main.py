# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'call':
            self.name = query[1]
        else:
            self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    numbers = {}
    names = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            numbers[cur_query.number] = cur_query.name
            names[cur_query.name] = cur_query.number

        elif cur_query.type == 'del':
            if cur_query.number in numbers:
                name = numbers[cur_query.number]
                names.pop(name)
                numbers.pop(cur_query.number)
        elif cur_query.type == 'find':
            response = 'not found'
            if cur_query.number in numbers:
                response = numbers[cur_query.number]
            result.append(response)
        #Piezvanit pec varda
        elif cur_query.type == 'call':
            response = 'not found'
            if cur_query.name in names:
                response = str(names[cur_query.name])
            result.append(response)
        else:
            print("command not found")
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
