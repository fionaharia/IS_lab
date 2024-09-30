class WaterJugProblem3Jugs:
    def __init__(self, capacityA, capacityB, capacityC):
        self.capacityA = capacityA
        self.capacityB = capacityB
        self.capacityC = capacityC

    def fill(self, state, jug):
        if jug == 'A':
            return (self.capacityA, state[1], state[2])
        elif jug == 'B':
            return (state[0], self.capacityB, state[2])
        elif jug == 'C':
            return (state[0], state[1], self.capacityC)
        return state

    def empty(self, state, jug):
        if jug == 'A':
            return (0, state[1], state[2])
        elif jug == 'B':
            return (state[0], 0, state[2])
        elif jug == 'C':
            return (state[0], state[1], 0)
        return state

    def pour(self, state, from_jug, to_jug):
        if from_jug == 'A' and to_jug == 'B':
            transfer = min(state[0], self.capacityB - state[1])
            return (state[0] - transfer, state[1] + transfer, state[2])
        elif from_jug == 'A' and to_jug == 'C':
            transfer = min(state[0], self.capacityC - state[2])
            return (state[0] - transfer, state[1], state[2] + transfer)
        elif from_jug == 'B' and to_jug == 'A':
            transfer = min(state[1], self.capacityA - state[0])
            return (state[0] + transfer, state[1] - transfer, state[2])
        elif from_jug == 'B' and to_jug == 'C':
            transfer = min(state[1], self.capacityC - state[2])
            return (state[0], state[1] - transfer, state[2] + transfer)
        elif from_jug == 'C' and to_jug == 'A':
            transfer = min(state[2], self.capacityA - state[0])
            return (state[0] + transfer, state[1], state[2] - transfer)
        elif from_jug == 'C' and to_jug == 'B':
            transfer = min(state[2], self.capacityB - state[1])
            return (state[0], state[1] + transfer, state[2] - transfer)
        return state

    def get_possible_moves(self, state):
        moves = []
        for jug in 'ABC':
            moves.append(self.fill(state, jug))
            moves.append(self.empty(state, jug))
        for from_jug in 'ABC':
            for to_jug in 'ABC':
                if from_jug != to_jug:
                    moves.append(self.pour(state, from_jug, to_jug))
        return moves

def main():
    print("Enter capacities for the three jugs:")
    capacityA = int(input("Capacity of Jug A: "))
    capacityB = int(input("Capacity of Jug B: "))
    capacityC = int(input("Capacity of Jug C: "))
    
    print("Enter initial state for the three jugs:")
    initialA = int(input("Initial amount in Jug A: "))
    initialB = int(input("Initial amount in Jug B: "))
    initialC = int(input("Initial amount in Jug C: "))

    # Create an instance of WaterJugProblem3Jugs
    problem = WaterJugProblem3Jugs(capacityA, capacityB, capacityC)
    
    initial_state = (initialA, initialB, initialC)
    possible_moves = problem.get_possible_moves(initial_state)
    
    print(f"Possible moves from state {initial_state}:")
    for move in possible_moves:
        print(move)

if __name__ == "__main__":
    main()