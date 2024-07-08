import sys


def show_tape(tape, position):
    if len(tape) > 15:
        for n in range(len(tape)):
            if (position == n):
                print("↓", end="")
            else:
                print(" ", end="")
        print("")

        for n in tape:
            print(f"{n}", end="")
        print("")

    else:
        for n in range(len(tape)):
            if (position == n):
                print(" _↓_ ", end="")
            else:
                print(" ___ ", end="")
        print("")

        for n in tape:
            print(f"| {n} |", end="")
        print("")

        for n in range(len(tape)):
            print(" ‾‾‾ ", end="")

        print("")


def q0(tape, position):
    if tape[position] == "0":
        tape[position] = "A"
        position += 1
        show_tape(tape, position)
        q1(tape, position)

    if tape[position] == "B":
        tape[position] = tape[position]  #do nothing
        position += 1
        show_tape(tape, position)
        q3(tape, position)

    if tape[position] == "_":
        print(f"✅ string \"{inputs}\" is Accepted")
        raise Exception

    if tape[position] == "1":
        print(f"❌ string {inputs} is Rejected")
        print("Because the string cannot start with 1")

        raise Exception


def q1(tape, position):
    if tape[position] == "0" or (tape[position]) == "B":
        tape[position] = tape[position]  #do nothing
        position += 1
        show_tape(tape, position)
        q1(tape, position)

    if tape[position] == "1":
        tape[position] = "B"
        position -= 1
        show_tape(tape, position)
        q2(tape, position)

    if tape[position] == "_":
        print(f"❌ string {inputs} is Rejected")
        print("Total number of 1 is lower than total number of 0")
        raise Exception


def q2(tape, position):
    if tape[position] == "0" or (tape[position]) == "B":
        tape[position] = tape[position]  #do nothing
        position -= 1
        show_tape(tape, position)
        q2(tape, position)

    if tape[position] == "A":
        tape[position] = tape[position]
        position += 1
        show_tape(tape, position)
        q0(tape, position)


def q3(tape, position):
    if tape[position] == "B":
        tape[position] = tape[position]  #do nothing
        position += 1
        show_tape(tape, position)
        q3(tape, position)

    if tape[position] == "1":
        tape[position] = tape[position]  #do nothing
        position -= 1
        show_tape(tape, position)
        q4(tape, position)

    if tape[position] == "_":
        print(f"✅ string \"{inputs}\" is Accepted")

        raise Exception


def q4(tape, position):
    if tape[position] == "X" or (tape[position]) == "A" or (
            tape[position]) == "B":
        tape[position] = tape[position]  #do nothing
        position -= 1
        show_tape(tape, position)
        q4(tape, position)

    if tape[position] == "_":
        tape[position] = tape[position]  #do nothing
        position += 1
        show_tape(tape, position)
        q5(tape, position)


def q5(tape, position):
    if tape[position] == "X":
        tape[position] = tape[position]  #do nothing
        position += 1
        show_tape(tape, position)
        q5(tape, position)

    if tape[position] == "A":
        tape[position] = "X"
        position += 1
        show_tape(tape, position)
        q6(tape, position)

    if tape[position] == "B":
        print(f"❌ string {inputs} is Rejected")
        print(f"Total number of 1 is more than double the number of 0")
        raise Exception


def q6(tape, position):
    if tape[position] == "X" or (tape[position]) == "A" or (
            tape[position]) == "B":
        tape[position] = tape[position]  #do nothing
        position += 1
        show_tape(tape, position)
        q6(tape, position)

    if tape[position] == "1":
        tape[position] = "X"
        position += 1
        show_tape(tape, position)
        q3(tape, position)


def main():

    print()

    sys.setrecursionlimit(sys.getrecursionlimit() * 5)
    tape = []
    position = 1
    global inputs

    print("Please enter the input string:", end="")
    inputs = input()

    tape.append("_")
    for i in inputs:
        tape.append(str(i))
    tape.append("_")

    show_tape(tape, position)
    q0(tape, position)

    sys.setrecursionlimit(sys.getrecursionlimit() / 5)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
