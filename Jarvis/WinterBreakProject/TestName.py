import random

def main():
    v_after_c = .7
    v_after_v = .3
    c_after_c = .4
    c_after_v = .6
    end = .5
    min_length = 5

    vowels = ["A", "E", "I", "O", "U"]
    consonants = [chr(x) for x in range(65, 91) if chr(x) not in vowels]

    name = ""
    last = random.randint(0, 1) #0 = consonant, 1 = vowel
    done = False
    while not done:
        r = random.random()
        if last == 0: #Last was a consonant
            if r < v_after_c: #Add a vowel
                name += random.choice(vowels)
                last = 1
            else:
                name += random.choice(consonants)
                last = 0

        else:
            if r < v_after_v:
                name += random.choice(vowels)
                last = 1
            else:
                name += random.choice(consonants)
                last = 0

        if len(name) >= min_length:
            if random.random() > end:
                done = True

    print name

main()
