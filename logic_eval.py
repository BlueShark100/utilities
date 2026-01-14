"""
If the help command is just... unhelpful, I added this as a reference

----------------------------------- INPUTTING_A_FUNCTION -----------------------------------------
there are serval key-words that are used as equivalents to the symbols in propositional logic
╭─────────┬─────────────╮
│ Keyword │ Equivalence │       <-- this table was made with another program of mine
├─────────┼─────────────┤               find it here: https://github.com/BlueShark100/utilities
│   and   │      ∧      │               it's table_generator.py
├─────────┼─────────────┤
│   or    │      ∨      │
├─────────┼─────────────┤           EXAMPLE: '(not p) and (p iff q)'
│   not   │      ¬      │           EQUIVALENCE: (¬p) ∧ (p ↔ q)
├─────────┼─────────────┤
│  then   │      →      │
├─────────┼─────────────┤
│   iff   │      ↔      │
╰─────────┴─────────────╯

NOTE! pythons operator precedence puts the 'not' operator before 'and' and 'or'
(check the bottom of the program) so make sure to use parentheses with the 'not'
operator to make sure to get intended behavior.

----------------------------- USING THE COMMAND LINE ARGUMENTS -----------------------------------
single letter argument flag, full word argument flag
    description
    > example usage

-f, --function
    you can input the function before the program has to ask for it.
    > python3 logic_eval.py -f '(not p) and (p iff q)'

-s, --show
    this is show a little extra info from the program like the letter
    propositions detected.
    > python3 logic_eval.py -s True

-c, --compatible
    this doesn't do anything right now. It will change the table output
    to use '+', '-', and '|' so that it pastes easier into other places
    if needed.
    > python3 logic_eval.py -c True

-p, --propositions
    You can manually input propositions you're going to use with this
    argument. This will overwrite the auto-detected form the program.
    Assigning these variables will also set the order for the variables
    when the table is generated.
    > python3 logic_eval.py -p 'pqr'

A full usage example would look like:
> python3 logic_eval.py -f '(not p) and (p iff q)' -p 'pqr' -s True

Using the flags, you can put the arguments in any order.

----------------------------------- TO-DO AND EXTRA NOTES -----------------------------------------

• Add windows check to disable colored output
    - I haven't tested it yet and I know windows
      likes to do a few things differently

    - Also add a command line argument: '-idc'
      for 'I don't care' to get rid of the warning
      and bring back colored output. (Ignore the check)

• Add command line argument to disable colored output
    - I might have to change the flag name for the
      compatible table output.

• Add compatible table mode
    - instead of using special Unicode characters
      (that should still work almost everywhere)
      use '+' signs, '|', and '-' to make the table.

    - I also should use tab characters to make sure
      there is a consistent lineup of characters since
      compatible mode probably means you're not pasting
      into a monospace font.

The ignore and keywords lists both contribute how the program auto-detects
propositions in the function. It just removes white-space, operators, and keywords.
They are seperated for clarity in the error output.

Just to clarify, keywords and ignoring have no effect on the function itself!
Only how the program will tell operators and parenthesis apart from the propositions.
"""

from colorama import Fore, Style
import argparse
import traceback

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
keywords = ['and', 'not', 'or', 'then', 'iff']
ignore = ['(', ')', ' ', 'i', 'j', 'True', 'False']  # used when extracting letter variables

parser = argparse.ArgumentParser(
                    prog='Logic Evaluator',
                    description='Takes in an argument with as many variables as desired and creates a full truth table for the function',
                    epilog=f'ignore list is only when looking for variables. It will NOT remove parentheses in the actual function. It WILL keep its original order of operations\n\n{Style.DIM}Keywords: {keywords}\n\nIgnoring: {ignore}{Style.RESET_ALL}')
parser.add_argument('-f', '--function', type=str, default=None, help='the input function')
parser.add_argument('-s', '--show', type=bool, default=False, help='Shows some extra info within the program')
parser.add_argument('-c', '--compatible', type=bool, default=False, help='Creates a more copy/paste compatible version of the table. DOES NOTHING RIGHT NOW')
parser.add_argument('-p', '--propositions', type=str, default=None, help='input variables manually, especially if you want a specific order on the table')

function = parser.parse_args().function
show_info = bool(parser.parse_args().show)
variables = parser.parse_args().propositions

ansi_blink = '\033[5m'  # I don't think I've used these yet, but they are interesting
ansi_underline = '\033[4m'

if function is not None:
    function_to_eval = function
    print(f'{Style.DIM}\nFunction entered: {function_to_eval}{Style.RESET_ALL}')
else:
    function_to_eval = input(f'\n{Style.DIM}Enter function here: {Style.RESET_ALL}{Style.BRIGHT}')
    print(Style.RESET_ALL, end='')
prop_vars = function_to_eval

print(f'{Style.DIM}Symbolic: {Style.RESET_ALL}{Style.BRIGHT}{function_to_eval.replace('and', '∧').replace('not ', '¬').replace('or', '∨').replace('then', '→').replace('iff', '↔')}{Style.RESET_ALL}')

if variables is not None:  # if they input variables
    prop_vars = list(variables)  # set those variables
else:
    for old_str in (keywords + ignore):  # get the variables from the function
        prop_vars = prop_vars.replace(old_str, '')

prop_vars = list(dict.fromkeys(prop_vars))

# change some special keywords that are directly interpreted by python
function_to_eval = function_to_eval.replace('then', '<=')
function_to_eval = function_to_eval.replace('iff', '==')

if ('i' in function_to_eval) or ('j' in function_to_eval):
    print(f'\n{Fore.RED}{Style.BRIGHT}Cannot use i or j as variables!{Style.DIM}\nI use it in my for loops. It will break the code{Fore.RESET}\n\nkeywords: {keywords}\nignoring: {ignore}\n')
    exit()
elif len(prop_vars) == 0:
    print(f"\n{Fore.RED}{Style.BRIGHT}No propositions detected!\n{Style.DIM}Make sure to use letters in the alphabet.{Fore.RESET}\n\nkeywords: {keywords}\nignoring: {ignore}\n")
    exit()
else:
    try:
        for i in range(len(prop_vars)):
            exec(f'{prop_vars[i]} = False')
        eval(function_to_eval)
    except Exception as e:
        print(
            f"\n{Fore.RED}{Style.BRIGHT}Error running function!\n{Style.DIM}make sure you're using letters and\nkeywords There should be a space\nbetween each keyword and letter.\nBelow is the specific error given:\n{Style.NORMAL}{traceback.format_exception(e)[-1]}\n{Fore.RESET}\nkeywords: {keywords}\nignoring: {ignore}\n")
        exit()
    if show_info:
        print(f"\n{Fore.GREEN}Detected {len(prop_vars)} propositions:{Style.RESET_ALL}\n{prop_vars}")

num_vars = len(prop_vars)
truth_table = [[None for _ in range(num_vars + 1)] for _ in range((2 ** num_vars) + 1)]
row_counter = 1

def populate_table(prop_vars, all_vars=None):
    """
    This function is the only useful part of the program.
    Most of everything else is just to help with error
    handling or to make the output look nice and tidy.
    """
    global row_counter
    global truth_table
    global num_vars

    if all_vars is None:
        all_vars = prop_vars

    # print(f'got {prop_vars} with length {len(prop_vars)}')

    if len(prop_vars) > 1:  # more than one left
        for i in range(2):
            truth_table[0][num_vars - len(prop_vars)] = (i == 0)  # write the variable truth value to its corresponding position
            populate_table(prop_vars[1:], all_vars)
    else:  # only one variable left
        for i in range(2):
            truth_table[0][num_vars - len(prop_vars)] = (i == 0)  # write the last variables truth value to its corresponding position
            for j in range(len(all_vars)):
                exec(f'{all_vars[j]} = truth_table[0][j]')  # execute variable assignment so the eval can use it
                # print(f'SETTING: {all_vars[j]} = test_table[0][j]\ncurrently {truth_table[0][j]}\n')

            curr_row = [str(truth_table[0][j])[0] for j in range(len(all_vars))]  # copy the list with a little modification
            curr_row.append(str(eval(function_to_eval))[0])  # write in the result in the last column

            # print(f'writing {str(test_table[0][j])[0]} at index {j} on row {test_counter}')
            truth_table[row_counter] = curr_row  # write the new row in

            # print(f'Top row: {test_table[0]}')
            # print(f'This row [{row_counter}]: {truth_table[row_counter]}')
            # print(f'Evaluating {function_to_eval} to {str(eval(function_to_eval))[0]}')
            # input('\n')
            row_counter += 1


populate_table(prop_vars)
# reset the first row to have the variable names
truth_table[0] = [var for var in prop_vars] + ['#']
# print(truth_table)

# print the table
# give each string a color depending on if its "T" or else
truth_table = [truth_table[0]] + [[f'{Fore.GREEN}{Style.BRIGHT}{val}{Style.RESET_ALL}' if val == "T" else f'{Fore.RED}{Style.BRIGHT}{val}{Style.RESET_ALL}' for val in row] for row in truth_table[1:]]
# Look I know this line is wildly cursed but it works and I don't want to remake it even though it's pretty simple

print(f"\n╭{"───┬" * len(prop_vars)}───╮")
for row in truth_table[:-1]:
    print("│ ", end="")
    print(*row, sep=" │ ", end=" │\n")
    print(f"├{"───┼" * len(prop_vars)}───┤")
print("│ ", end="")
print(*truth_table[-1], sep=" │ ", end=" │\n")
print(f"╰{"───┴" * len(prop_vars)}───╯\n")

'''
Operator Precedence in Python

0. :=
1. lambda
2. if – else
3. or
4. and
5. not x
6. in, not in, is, is not, <, <=, >, >=, !=, ==
7. |
8. ^
9. &
10. <<, >>
11. +, -
12. *, @, /, //, %
13. +x, -x, ~x
14. **
14. await x
15. x[index], x[index:index], x(arguments...), x.attribute
16. (expressions...), [expressions...], {key: value...}, {expressions...}

I just copied this list from the internet. I don't remember the site. Probably stack overflow
'''