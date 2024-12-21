from random import randint, choice

__alph = ['A', 'M', 'P', "Е", "Х", "У", "Н", "К", "Л", "И"]


def generate_grz():
    if randint(1, 5) > 2:
        return choice(["P038ИН",
                       "P038ИН",
                       "Е848НM",
                       "Е955УН",
                       "И327ХУ",
                       "К108КP",
                       "К803УК",
                       "К826PК",
                       "Л616ЛM",
                       "Х397AК",
                       "Х491ЛЕ"])
    else:
        num = randint(1, 999)
        return f"{choice(__alph)}{num:03}{choice(__alph)}{choice(__alph)}"
