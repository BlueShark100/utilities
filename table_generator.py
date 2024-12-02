import argparse
from colorama import Fore, Back, Style

border_styles_text = '''
     Style 1             Style 2             Style 3
+---------+------+  ╭─────────┬──────╮  ┏━━━━━━━━━┳━━━━━━┓
| example | data |  │ example │ data │  ┃ example ┃ data ┃
+---------+------+  ├─────────┼──────┤  ┣━━━━━━━━━╋━━━━━━┫
|   24    | 4.1  |  │   24    │ 4.1  │  ┃   24    ┃ 4.1  ┃
+---------+------+  ├─────────┼──────┤  ┣━━━━━━━━━╋━━━━━━┫
|   50    | 1.64 |  │   50    │ 1.64 │  ┃   50    ┃ 1.64 ┃
+---------+------+  ├─────────┼──────┤  ┣━━━━━━━━━╋━━━━━━┫
|   60    | 1.97 |  │   60    │ 1.97 │  ┃   60    ┃ 1.97 ┃
+---------+------+  ├─────────┼──────┤  ┣━━━━━━━━━╋━━━━━━┫
|   120   | 0.82 |  │   120   │ 0.82 │  ┃   120   ┃ 0.82 ┃
+---------+------+  ╰─────────┴──────╯  ┗━━━━━━━━━┻━━━━━━┛

     Style 4             Style 5             Style 6
╓─────────╥──────╖  ╒═════════╤══════╕  ╔═════════╦══════╗
║ example ║ data ║  │ example │ data │  ║ example ║ data ║
╟─────────╫──────╢  ╞═════════╪══════╡  ╠═════════╬══════╣
║   24    ║ 4.1  ║  │   24    │ 4.1  │  ║   24    ║ 4.1  ║
╟─────────╫──────╢  ╞═════════╪══════╡  ╠═════════╬══════╣
║   50    ║ 1.64 ║  │   50    │ 1.64 │  ║   50    ║ 1.64 ║
╟─────────╫──────╢  ╞═════════╪══════╡  ╠═════════╬══════╣
║   60    ║ 1.97 ║  │   60    │ 1.97 │  ║   60    ║ 1.97 ║
╟─────────╫──────╢  ╞═════════╪══════╡  ╠═════════╬══════╣
║   120   ║ 0.82 ║  │   120   │ 0.82 │  ║   120   ║ 0.82 ║
╙─────────╨──────╜  ╘═════════╧══════╛  ╚═════════╩══════╝
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a text-based table from input text',
        formatter_class=argparse.MetavarTypeHelpFormatter,
        epilog='When inputting values, spaces before and after are ok to help with readability while inputting. The program will remove spaces before and after but not in between text. '
    )
    parser.add_argument('-v', '--version', action='version', version=f'{Style.DIM}%(prog)s {Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} 1.0', help="Show program's version number and exit.")
    parser.add_argument('--show_borders', '--border_styles', action='store_true', help="Show all the border styles available")
    parser.add_argument('-b', '--border', default=2, type=int, help="Style of the borders. 1-6")
    parser.add_argument('-d', '--dimensions', type=str, help="Dimensions of the table. COLUMNSxROWS Ex: 3x5")
    parser.add_argument('-a', '--align', type=str, default="c", help="Where to align the text in each box. c: center l: left r: right")  # TODO: add text alignment
    args = parser.parse_args()

    if args.show_borders:
        print(border_styles_text)
        exit(0)

    border_styles = [["-", "|", "+", "+", "+", "+", "+", "+", "+", "+", "+"], ["─", "│", "├", "┬", "┤", "┴", "┼", "╭", "╮", "╰", "╯"], ["━", "┃", "┣", "┳", "┫", "┻", "╋", "┏", "┓", "┗", "┛"], ["─", "║", "╟", "╥", "╢", "╨", "╫", "╓", "╖", "╙", "╜"], ["═", "│", "╞", "╤", "╡", "╧", "╪", "╒", "╕", "╘", "╛"], ["═", "║", "╠", "╦", "╣", "╩", "╬", "╔", "╗", "╚", "╝"]]
    text_align_args = {"c": "^", "l": "<", "r": ">"}

    if args.align not in text_align_args.keys():
        print(f'\n{Fore.RED}Alignment argument invalid!\n{Style.DIM}Use "c" for centered, "l" for\nleft aligned, or "r" for right\naligned.{Style.RESET_ALL}\n')
        exit(1)

    if not args.dimensions:
        table_dimensions = input(f"Enter table dimensions {Style.DIM}(Ex: 3x2){Style.RESET_ALL}: ")
    else:
        table_dimensions = args.dimensions

    try:
        num_cols = int(table_dimensions[0])
        num_rows = int(table_dimensions[-1])
    except ValueError:
        print(f"\n{Fore.RED}Couldn't convert rows/columns to integers\n{Style.DIM}double check you inputted them correctly\n")
        exit(1)

    table_data: [str] = [""] * num_rows

    # print(f"rows: {num_rows}, cols: {num_cols}")
    print(f'{Style.DIM}Enter each rows values separated by a comma.\nStart the next row by hitting enter\nCOLUMNS: {num_cols} | ROWS: {num_rows}{Style.RESET_ALL}')
    for i in range(num_rows):
        table_data[i] = [x.strip() for x in input().split(",")]

    column_widths: [int] = [0] * num_cols

    try:
        for i in range(num_cols):
            for j in range(num_rows):
                if column_widths[i] < len(table_data[j][i]):
                    column_widths[i] = len(table_data[j][i])
    except IndexError:
        print(f"\n{Fore.RED}Error when generating table:\n{Style.DIM}Input Missmatch with table dimensions{Style.RESET_ALL}\n")
        exit(1)

    horizontal = border_styles[args.border - 1][0]
    vertical = border_styles[args.border - 1][1]
    cross = border_styles[args.border - 1][6]
    tr_corner = border_styles[args.border - 1][7]  # top right
    tl_corner = border_styles[args.border - 1][8]  # top left
    br_corner = border_styles[args.border - 1][9]  # bottom right
    bl_corner = border_styles[args.border - 1][10]  # bottom left
    l_edge = border_styles[args.border - 1][2]  # left edge
    t_edge = border_styles[args.border - 1][3]  # top edge
    r_edge = border_styles[args.border - 1][4]  # right edge
    b_edge = border_styles[args.border - 1][5]  # bottom ede

    def print_table_line(row_index: int):
        if row_index == 0:
            for j in range(num_cols):
                if j == 0:
                    print(f"{tr_corner}{horizontal * (column_widths[j] + 2)}", end="")
                else:
                    print(f"{t_edge}{horizontal * (column_widths[j] + 2)}", end="")
            print(f"{tl_corner}")
        elif row_index == num_rows:
            for j in range(num_cols):
                if j == 0:
                    print(f"{br_corner}{horizontal * (column_widths[j] + 2)}", end="")
                else:
                    print(f"{b_edge}{horizontal * (column_widths[j] + 2)}", end="")
            print(f"{bl_corner}")
        else:
            for j in range(num_cols):
                if j == 0:
                    print(f"{l_edge}{horizontal * (column_widths[j] + 2)}", end="")
                else:
                    print(f"{cross}{horizontal * (column_widths[j] + 2)}", end="")
            print(f"{r_edge}")

    def print_content_line():
        for j in range(num_cols):
            print(f"{vertical} {table_data[i][j]:{text_align_args[args.align]}{column_widths[j]}} ", end="")
        print(f"{vertical}")

    print("")  # newline for space
    for i in range(num_rows):
        print_table_line(i)
        print_content_line()

    print_table_line(num_rows)

    print(f"\n{Fore.GREEN}Table successfully generated.{Style.RESET_ALL}\n")
