import argparse
from colorama import Fore, Back, Style

# argparse to add kwargs to command line excecution

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a text-based table from input text',
        formatter_class=argparse.MetavarTypeHelpFormatter,
        epilog='When inputting values spaces before and after are ok to help with readability while inputting. The program will remove spaces before and after but not in between text'
    )
    parser.add_argument('-b', '--border', default=1, type=int, help="Style of the borders. 1-2")
    parser.add_argument('-d', '--dimensions', type=str, help="Dimensions of the table. ROWSxCOLUMNS Ex: 3x5")
    parser.add_argument('-a', '--align', type=str, help="Where to align the text in each box. c: center l: left r: right")  # TODO: add text alignment
    args = parser.parse_args()

    # print(f"\arguments: {args}\n")

    border_styles = [["-", "|", "+", "+", "+", "+", "+", "+", "+", "+", "+"], ["─", "│", "├", "┬", "┤", "┴", "┼", "┌", "┐", "└", "┘"]]

    if not args.dimensions:
        table_dimensions = input(f"Enter table dimensions {Style.DIM}(Ex: 3x2){Style.RESET_ALL}: ")
    else:
        table_dimensions = args.dimensions

    try:
        num_rows = int(table_dimensions[0])
        num_cols = int(table_dimensions[-1])
    except ValueError:
        print(f"\n{Fore.RED}Couldn't convert rows/columns to integers\ndouble check you inputted them correctly\n")
        exit(1)

    table_data: [str] = [""] * num_rows

    # print(f"rows: {num_rows}, cols: {num_cols}")
    print(f'{Style.DIM}Enter row values separated by a period.\nROWS:{num_rows} | COLUMNS: {num_cols}{Style.RESET_ALL}')
    for i in range(num_rows):
        table_data[i] = [x.strip() for x in input().split(".")]

    column_widths: [int] = [0] * num_cols

    try:
        for i in range(num_cols):
            for j in range(num_rows):
                if column_widths[i] < len(table_data[j][i]):
                    column_widths[i] = len(table_data[j][i])
    except IndexError:
        print(f"\n{Fore.RED}Table not generated:\nInput Missmatch with table dimensions{Style.RESET_ALL}\n")
        exit(1)

    horizontal = border_styles[args.border - 1][0]
    vertical = border_styles[args.border - 1][1]
    cross = border_styles[args.border - 1][6]
    tr_corner = border_styles[args.border - 1][7]  # top right
    tl_corner = border_styles[args.border - 1][8]  # top left
    br_corner = border_styles[args.border - 1][9]  # bottom right
    bl_corner = border_styles[args.border - 1][10]  # bottom left

    print("")  # newline for space
    for i in range(num_rows):
        for j in range(num_cols):
            print(f"{cross}{horizontal * (column_widths[j] + 2)}", end="")
        print(f"{cross}")

        for j in range(num_cols):
            print(f"{vertical} {table_data[i][j]:^{column_widths[j]}} ", end="")
        print(f"{vertical}")

    for j in range(num_cols):
        print(f"{cross}{horizontal * (column_widths[j] + 2)}", end="")
    print(f"{cross}")

    print(f"\n{Fore.GREEN}Table successfully generated.{Style.RESET_ALL}\n")

'''
+-----+--------+
| fps | scaler |
+-----+--------+
| 24  | 4.1    |
+-----+--------+
| 50  | 1.64   |
+-----+--------+
| 60  | 1.97   |
+-----+--------+
| 120 | 0.82   |
+-----+--------+
'''
