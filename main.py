import ColorMapping

def get_lines(fileName):
    lines = []
    with open(fileName,'r') as readFile:
        for line in readFile:
            lines.append(line)
    return lines


""" Takes a list of lines and creates a CSP representation.
    Format:
    variable values ...
    ...
    0
    binary_constraint_type inputs ...
    ...
    0
    unary_constraint_type inputs ... 
    ... """


def csp_parse(csp_lines):
    i = 0
    variables = []
    domains = []
    while csp_lines[i].strip() != '0':
        line = csp_lines[i].split()
        variables.append(line[0])
        domains.append(set(line[1:]))
        i += 1
    i += 1

    binary_constraints = []
    while csp_lines[i].strip() != '0':
        line = csp_lines[i].split()
        binary_constraints.append(getattr(ColorMapping, line[0])(*line[1:]))
        i += 1
    i += 1

    return ColorMapping.csp(variables, domains, binary_constraints)



lines = get_lines("D:/CU Boulder Semesters/spring'23/Intro to AI/csp2.csp")
csp = csp_parse(lines)
yy= ColorMapping.solveCSP(csp, orderValuesMethod=ColorMapping.valOrder, selectVariableMethod=ColorMapping.varOrder)