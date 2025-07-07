#!/bin/python3
# Find the total paths for travelling from the start of a grid to the end
# but only travelling through the grid cell if the value is 1
# the only way to travel through the grid is down or right

def num_paths(ware_house):
    print(ware_house)
    dest_x_coordinate = len(ware_house) - 1
    dest_y_coordinate = len(ware_house[0]) - 1
    des_key = str(dest_x_coordinate) + "." + str(dest_y_coordinate)
    memo = {des_key: 1}
    return count_path([0, 0], ware_house, 0, memo)


def count_path(source, ware_house, count, memo):
    x_coordinate = source[0]
    y_coordinate = source[1]
    memo_coordinate = str(x_coordinate) + "." + str(y_coordinate)
    if memo.get(memo_coordinate) is not None:
        return count + memo.get(memo_coordinate)
    if x_coordinate != len(ware_house) - 1 and ware_house[x_coordinate + 1][y_coordinate] == 1:
        count = count_path([x_coordinate + 1, y_coordinate], ware_house, count, memo)
    if y_coordinate != len(ware_house[0]) - 1 and ware_house[x_coordinate][y_coordinate + 1] == 1:
        count = count_path([x_coordinate, y_coordinate + 1], ware_house, count, memo)
    return count


if __name__ == '__main__':
    warehouse = [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1],
                 [1, 1, 1]]

    print(num_paths(warehouse))
