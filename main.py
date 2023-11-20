
import json

from statement import Statement


def main() -> None:
    statement_calculator = Statement()
    result = statement_calculator.statement(
        json.load(open('./_chapter_1/invoices.json'))[0],
        json.load(open('./_chapter_1/plays.json')),
    )
    print(result)


if __name__ == '__main__':
    main()