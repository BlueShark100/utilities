import argparse

# argparse to add kwargs to command line excecution

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
       description='Generate a text-based table from input text'
    )
    parser.add_argument('-b', '--border', help="Style of the borders. int 1-3")
    parser.add_argument('-d', '--dimensions', help="Dimensions of the table. ROWSxCOLUMNS Ex: 3x5")
    parser.add_argument('-a', '--argument', help="argument example")  # Something else
    args = parser.parse_args()

    print(args.b)
    print(args.a)

    my_dict = {'arg1': args.arg1, 'arg2': args.arg2}
    print(my_dict)

    if not args.dimensions:
        table_dimensions = input("Enter table dimensions (Ex: 3x2): ")
    else:
        table_dimensions = args.dimensions

    try:
        num_rows = int(table_dimensions[0])
        num_cols = int(table_dimensions[-1])
    except ValueError:
        print("|| Couldn't convert rows/columns to integers\n|| double check you inputted them correctly")
        exit("> program exited")

    print(f"rows: {num_rows}, cols: {num_cols}")
