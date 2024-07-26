def can_complete_circuit(gas, cost):
    total_gas = 0
    total_cost = 0
    current_gas = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        current_gas += gas[i] - cost[i]

        # If current gas is negative, cannot start from current start_index
        if current_gas < 0:
            # Reset the starting index to the next station
            start_index = i + 1
            # Reset current gas for the new start index
            current_gas = 0

    # If total gas is less than total cost, it's impossible to complete the circuit
    if total_gas < total_cost:
        return -1
    return start_index

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas, cost))  # Output: 3
