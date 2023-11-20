
import json

from statement import Statement


def main() -> None:
    statement_calculator = Statement()
    result = statement_calculator.statement(
        json.load(open('invoices.json'))[0],
        json.load(open('plays.json')),
    )
    print(result)


if __name__ == '__main__':
    main()
