import random


def random_marry():
    print('pairs =', end=' ')

    for i in range(min(len(boys), len(girls))):
        boy = random.choice(boys)
        girl = random.choice(girls)
        pair.append([boy, girl])
        boys.remove(boy)
        girls.remove(girl)
        print(f'({boy},{girl})', end=' ')

    print('')

    if len(girls):
        print(girls, 'are single ')

    elif len(boys):
        print(boys, 'are single ')


if __name__ == "__main__":
    pair = []
    boys = ["mohammad", "sobhan", "abdollah",
            "kiya", "mahdi", "sajjad", "homan", "arman"]
    girls = ["mahtab", "hane", "harir", "fateme",
             "kiana", "faezeh", "minoo", "mina", "soghra"]

    random_marry()
