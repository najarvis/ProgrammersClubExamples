import sys, random

def get_single_letter_data(data, letter):
    letter_dict = {}
    last = False
    for x_letter in data:
        actual_letter = x_letter.lower()

        if actual_letter == letter:
            last = True
            continue

        if last:
            try:
                letter_dict[actual_letter] += 1
            except KeyError:
                letter_dict[actual_letter] = 1
            last = False
    
    good_keys = [chr(x) for x in range(97, 123)]
    for key in letter_dict.keys():
        if key not in good_keys:
            del letter_dict[key]

    total = 0.0
    for key in letter_dict.keys():
        total += letter_dict[key]

    for key in letter_dict.keys():
        letter_dict[key] /= total
    
    return letter_dict

def main(filename, num, chosen_letter=None):
    main_data = {}
    with open(filename, 'r') as f:
        data = f.read()
        letters = [chr(x) for x in xrange(97, 123)] + [' ']
        for letter in letters:
            main_data[letter] = get_single_letter_data(data, letter)

    min_length = 5
    max_length = 10
    end = 0.5
    num_names = 0
    try:
        num_names = int(num)
    except ValueError:
        num_names = 3
    
    if chosen_letter is None:
        for l in [chr(x) for x in xrange(97, 123)]:
            for n in xrange(num_names):
                print generate_name(main_data, l, min_length, max_length, end)
    else:
        for n in xrange(num_names):
            print generate_name(main_data, chosen_letter, min_length, max_length, end)

def generate_name(main_data, start_letter, min_length, max_length, end):
    name = ""
    first_letter = start_letter
    name += first_letter

    done = False
    while not done:
        r = random.random()
        name += get_letter(main_data, name[-1])

        if len(name) >= min_length:
            if len(name) >= max_length:
                done = True
            elif random.random() > end:
                done = True
    
    return name

def get_letter(data, letter):
    lst = []
    total = 0
    for k in data[letter].keys():
        total += data[letter][k]
        lst.append(total)

    r = random.random()
    for i in lst:
        if r <= i:
            letter = data[letter].keys()[lst.index(i)]
            break

    return letter

if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print ">>> Usage: WordMaker.py [filename] [num] ([letter])"
    else:
        letter = None
        if len(sys.argv) == 4:
            letter = sys.argv[3]
        main(sys.argv[1], sys.argv[2], letter)

