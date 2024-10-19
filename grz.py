from random import randint, choice

__alph = ['A', 'M', 'P', "Е", "Х", "У", "Н", "К", "Л", "И"]

def generate_grz():
    num = randint(1, 999)
    return f"{choice(__alph)}{num:03}{choice(__alph)}{choice(__alph)}"