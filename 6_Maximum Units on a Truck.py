def maximum_units(boxTypes, truckSize):
    # Sort boxTypes by number of units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    for numberOfBoxes, unitsPerBox in boxTypes:
        if truckSize == 0:
            break

        # Take as many boxes as possible up to the truck's remaining capacity
        boxes_to_take = min(truckSize, numberOfBoxes)
        total_units += boxes_to_take * unitsPerBox
        truckSize -= boxes_to_take

    return total_units


# Example usage:
boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
print(maximum_units(boxTypes, truckSize))  # Output: 8
