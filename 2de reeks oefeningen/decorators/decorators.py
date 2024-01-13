import random


def remember(func):
    gevraagde_vragen = set()

    def wrapper(vraag):
        if vraag in gevraagde_vragen:
            return "You have asked this question before"
        else:
            gevraagde_vragen.add(vraag)
            return func(vraag)
    return wrapper

@remember
def magic_eight_ball(question):
    antwoorden = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Better not tell you now",
        "Cannot predict now",
        "Maybe rephrase the question",
        "Don't count on it",
        "My reply is no",
        "Outlook not so good"
    ]
    return random.choice(antwoorden)

print(magic_eight_ball("Will it rain tomorrow?"))

# Tst magic_eight_ball met decorator
magic_eight_ball = remember(magic_eight_ball)
print(magic_eight_ball("Should I take a new job?"))
print(magic_eight_ball("Should I take a new job?")) 