"""This should simulate frequevent typos when using keyboard"""
keyboard_neighborhood = {
    '1': ['`', '2', 'q'],
    '2': ['1', '3', 'q', 'w'],
    '3': ['2', '4', 'w', 'e'],
    '4': ['3', '5', 'e', 'r'],
    '5': ['4', '6', 'r', 't'],
    '6': ['5', '7', 't', 'y'],
    '7': ['6', '8', 'y', 'u'],
    '8': ['7', '9', 'u', 'i'],
    '9': ['8', '0', 'i', 'o'],
    '0': ['9', '-', 'o', 'p'],
    '-': ['0', '=', 'p', '[', '\''],
    '=': ['-', '[', ']', '+'],
    'q': ['w', 'a', '1', '2'],
    'w': ['q', 'e', 'a', 's', '2', '3'],
    'e': ['w', 'r', 's', 'd', '3', '4'],
    'r': ['e', 't', 'd', 'f', '4', '5'],
    't': ['r', 'y', 'f', 'g', '5', '6'],
    'y': ['t', 'u', 'g', 'h', '6', '7', 'z'],
    'u': ['y', 'i', 'h', 'j', '7', '8'],
    'i': ['u', 'o', 'j', 'k', '8', '9'],
    'o': ['i', 'p', 'k', 'l', '9', '0'],
    'p': ['o', 'l', '[', ';', '0', '-'],
    '[': ['p', ']', ';', '\'','-', '=' 'š'],
    ']': ['[', 'đ', '\'', '\\', 'đ'],
    'a': ['q', 'w', 's', 'z'],
    's': ['a', 'w', 'e', 'd', 'z', 'x'],
    'd': ['s', 'e', 'r', 'f', 'x', 'c'],
    'f': ['d', 'r', 't', 'g', 'c', 'v'],
    'g': ['f', 't', 'y', 'h', 'v', 'b'],
    'h': ['g', 'y', 'u', 'j', 'b', 'n'],
    'j': ['h', 'u', 'i', 'k', 'n', 'm'],
    'k': ['j', 'i', 'o', 'l', 'm', ','],
    'l': ['k', 'o', 'p', ';', ',', '.'],
    ';': ['p', '[', 'l', '\'', '.', '/', 'č'],
    '\'': ['[', ']', ';', 'ć'],
    '\\': ['ž', ']'],
    'z': ['a', 's', 'x', 'y'],
    'x': ['z', 's', 'd', 'c'],
    'c': ['x', 'd', 'f', 'v', ' '],
    'v': ['c', 'f', 'g', 'b', ' '],
    'b': ['v', 'g', 'h', 'n', ' '],
    'n': ['b', 'h', 'j', 'm', ' '],
    'm': ['n', 'j', 'k', ' ', ','],
    ',': ['m', 'k', 'l', '.'],
    '.': [',', 'l', ';', '/'],
    '/': ['.', ';', '\''],
    ' ': ['c', 'v', 'b', 'n', 'm'],
    '!': ['1'],
    '?': ['/'],
    'ž': ['z', '\\'],
    'š': ['s', '\''],
    'đ': [']', 'd'],
    'ć': ['c', '\''],
    'č': [';', 'c']
}