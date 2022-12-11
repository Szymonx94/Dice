import random
DICES = ( "D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")
def throw_dice(dice_code):
    """ Rolls dice i different choice dice

    :param dice_code: dice
    :rtype: str, int
    :return: dice roll for choice "D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3"
    """
    for dice in DICES:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong"
    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"
    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier

if __name__ == '__main__':
    print(throw_dice("2D10+10"))
    print(throw_dice("D6"))
    print(throw_dice("2D3"))


