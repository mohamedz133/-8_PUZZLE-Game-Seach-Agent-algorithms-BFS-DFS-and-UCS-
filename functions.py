
def get_actions(puzzle):
    moves=[
            ['a', 'w'],['d', 'a', 'w'],['d', 's'],
            ['a', 'w', 's'],['d', 'a', 'w', 's'],
            ['d', 'w', 's'],['a', 's'],['d', 'a', 's'],
            ['d', 'w']
        ]
    if puzzle.index(0) == 0:
        return moves[2]

    if puzzle.index(0) == 1:
        return moves[7]

    if puzzle.index(0) == 2:
        return moves[6]

    if puzzle.index(0) == 3:
        return moves[5]

    if puzzle.index(0) == 4:
        return moves[4]

    if puzzle.index(0) == 5:
        return moves[3]

    if puzzle.index(0) == 6:
        return moves[8]

    if puzzle.index(0) == 7:
        return moves[1]

    if puzzle.index(0) == 8:
        return moves[0]



def get_state(selected_move, puzzle):
    # apply the action to the given state and return the new state
    copy = puzzle[:]
    # find index of zero in list
    index = puzzle.index(0)

    if selected_move == 'a':
        copy[index] = copy[index - 1]
        copy[index - 1] = 0

    elif selected_move == 'd':
        copy[index] = copy[index + 1]
        copy[index + 1] = 0

    elif selected_move == 'w':
        copy[index] = copy[index - 3]
        copy[index - 3] = 0

    elif selected_move == 's':
        copy[index] = copy[index + 3]
        copy[index + 3] = 0

    return copy


def isgoal(puzzle):
    # if puzzle is solved (in the correct order) return True, otherwise return False
    return puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]
