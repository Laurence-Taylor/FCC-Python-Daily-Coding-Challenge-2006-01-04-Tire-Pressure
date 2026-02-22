def tire_status(pressures_psi, range_bar):
    # convert the bar to psi
    range_bar = [item * 14.5038 for item in range_bar]
    list_answer = []
    # iterate over each value and create the resulting list
    for item in pressures_psi:
        if item < range_bar[0]:list_answer.append('Low')
        elif range_bar[0] <= item <= range_bar[1]:list_answer.append('Good')
        else:list_answer.append('High')
    return list_answer

if __name__ == '__main__':
    print(tire_status([32, 28, 35, 29], [2, 3]))