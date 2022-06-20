def main():
    # TODO: write the code for the program.
    earth_weight = float(input('What do you weigh on Earth? \n'))
    mercuty_weight = print_weight(earth_weight, 0.38)
    jupiter_weight = print_weight(earth_weight, 2.53)

    print(
        'On Mercury you would weigh ' + mercuty_weight + ' pounds.\n'
        + 'On Jupiter you would weigh ' + jupiter_weight + ' pounds.'
    )


def print_weight(earth_weight: int, multiplier: float) -> str:
    return str("{:.2f}".format(earth_weight * multiplier))


# NOTE: This means if the code is run as `python3 planets.py`, run the
# main function.  If the code is merely imported, don't do anything.
if __name__ == '__main__':
    main()
