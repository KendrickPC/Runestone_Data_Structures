from random import choice

alphabets = [chr(i) for i in range(97, 123)]
alphabets.append(" ")
string = "methinks it is like a weasel"


def random_string():
    result = ""
    i = 0
    while i < len(string):
        result += choice(alphabets)
        i += 1
    return result


def score_n_match():
    score = 0
    i = 0
    match = ""
    while i < len(string):
        temp = random_string()
        if string[i] == temp[i]:
            print(f"{i + 1} match found.")
            match += temp[i]
            i += 1
        score += 1
    print(f"generated string: {match} after {score} loops")


score_n_match()
