from ortools.sat.python import cp_model
import ast

def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        end_states : list[tuple[int, ...]] = []
        buttons : list[list[tuple[int, ...]]] = []
        joltage_reqs : list[tuple[int, ...]] = []
        for line in lines:
            line = line.strip().split()
            end_state = tuple(map(lambda x: 0 if x == '.' else 1, list(line[0][1:-1])))
            end_states.append(end_state)
            joltage = line[-1][1:-1].split(',')
            joltage = tuple(map(int, joltage))
            joltage_reqs.append(joltage)
            current : list[tuple[int, ...]] = []
            for button in line[1:-1]:
                button = ast.literal_eval(button)
                if isinstance(button, int):
                    button = (button, )
                current.append(button)
            buttons.append(current)
            
    return end_states, buttons, joltage_reqs

def solve_min_sum_cp_sat(n_vars, equations, lower_bound=0):
    model = cp_model.CpModel()
    max_rhs = max((rhs for _, rhs in equations), default=0)

    xs = {}
    for i in range(1, n_vars + 1):
        rlist = [rhs for (vars_, rhs) in equations if i in vars_]
        ub = min(rlist) if rlist else max_rhs
        for (vars_, rhs) in equations:
            if i in vars_:
                k = len(vars_)
                ub = min(ub, rhs - lower_bound*(k-1))
        ub = max(ub, lower_bound)
        xs[i] = model.NewIntVar(lower_bound, ub, f"x{i}")

    for vars_, rhs in equations:
        model.Add(sum(xs[i] for i in vars_) == rhs)

    model.Minimize(sum(xs[i] for i in xs))

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 8

    result = solver.Solve(model)
    if result in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return {i: solver.Value(xs[i]) for i in xs}
    else:
        return None

def get_equations(buttons : list[tuple[int, ...]], joltage_req : tuple[int, ...]):
    n = len(buttons)
    eqs : list[list[int]] = [[] for _ in range(len(joltage_req))]
    
    for index, button in enumerate(buttons):
        for x in button:
            eqs[x].append(index + 1)
    
    return n, [(eq, joltage) for eq, joltage in zip(eqs, joltage_req)]

def solve_line(buttons, joltage_req):
    n, equations = get_equations(buttons, joltage_req)
    solution = solve_min_sum_cp_sat(n, equations)
    return sum(solution.values())

def solve(buttons, joltage_reqs):
    total = 0
    i = 0
    
    for button_list, joltage_req in zip(buttons, joltage_reqs):
        total += solve_line(button_list, joltage_req)
        i = i + 1
    
    return total


if __name__ == "__main__":
    _, buttons, joltage_reqs = read_input()
    print(solve(buttons, joltage_reqs))
