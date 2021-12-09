from aocd import lines


def uncipher_one(numbers):
    one = next(nb for nb in numbers if len(nb) == 2) # Get the digit with a length of 2
    return {
        'c' : [one[0], one[1]],
        'f' : [one[0], one[1]]
        }


def uncipher_seven(digits, segments):
    seven = next(nb for nb in digits if len(nb) == 3) # Get the digit with a length of 3

    a_segment = list(set(seven) - set(segments['c']))
    segments['a'] = a_segment[0]
    return segments


def uncipher_four(digits, segments):
    four = next(nb for nb in digits if len(nb) == 4) # Get the digit with a length of 4
    
    bd_segments = list(set(four) - set(segments['c']))
    segments['b'] = [bd_segments[0], bd_segments[1]]
    segments['d'] = [bd_segments[0], bd_segments[1]]
    return segments


def uncipher_eight(digits, segments):
    eight = next(nb for nb in digits if len(nb) == 7) # Get the digit with a length of 7
    
    eg_segments = list(set(eight) - set(''.join(segments['b']) + segments['a'] + ''.join(segments['c'])))
    segments['e'] = [eg_segments[0], eg_segments[1]]
    segments['g'] = [eg_segments[0], eg_segments[1]]
    return segments


def contains_segment(digit, segment):
    return segment in digit


def uncipher_nine(digits, segments):
    possible_nines = [nb for nb in digits if len(nb) == 6]
    for nine in possible_nines:
        if not contains_segment(nine, segments['a']):
            continue
        if not contains_segment(nine, segments['b'][0]):
            continue
        if not contains_segment(nine, segments['b'][1]):
            continue
        if not contains_segment(nine, segments['c'][0]):
            continue
        if not contains_segment(nine, segments['c'][1]):
            continue
        real_nine = nine

    segments['g'] = list(set(real_nine) - set(''.join(segments['b']) + segments['a'] + ''.join(segments['c'])))[0]
    segments['e'] = list(set(segments['e']) - set(segments['g']))[0]
    return segments


def uncipher_six(digits, segments):
    possible_sixes = [nb for nb in digits if len(nb) == 6]
    for six in possible_sixes:
        if not contains_segment(six, segments['d'][0]):
            continue
        if not contains_segment(six, segments['d'][1]):
            continue
        if not contains_segment(six, segments['e']):
            continue
        real_six = six

    segments['f'] = list(set(real_six) - set(''.join(segments['b']) + segments['a'] + segments['e'] + segments['g']))[0]
    segments['c'] = list(set(segments['c']) - set(segments['f']))[0]
    return segments


def uncipher_zero(digits, segments):
    possible_zeroes = [nb for nb in digits if len(nb) == 6]
    for zero in possible_zeroes:
        if not contains_segment(zero, segments['e']):
            continue
        if not contains_segment(zero, segments['c']):
            continue
        real_zero = zero

    segments['b'] = list(set(real_zero) - set(segments['a'] + segments['c'] + segments['e'] + segments['f'] + segments['g']))[0]
    segments['d'] = list(set(segments['d']) - set(segments['b']))[0]
    return segments


def determine_digit(str, segments):
    nine_segments = segments['a'] + segments['b'] + segments['c'] + segments['d'] + segments['f'] + segments['g']
    six_segments = segments['a'] + segments['b'] + segments['d'] + segments['e'] + segments['f'] + segments['g']
    zero_segments = segments['a'] + segments['b'] + segments['c'] + segments['e'] + segments['f'] + segments['g']
    two_segments = segments['a'] + segments['c'] + segments['d'] + segments['e'] + segments['g']
    three_segments = segments['a'] + segments['c'] + segments['d'] + segments['f'] + segments['g']
    five_segments = segments['a'] + segments['b'] + segments['d'] + segments['f'] + segments['g']

    if len(str) == 2:
        return 1
    elif len(str) == 3:
        return 7
    elif len(str) == 4:
        return 4
    elif len(str) == 7:
        return 8
    elif len(set(nine_segments) - set(str)) == 0:
        return 9
    elif len(set(six_segments) - set(str)) == 0:
        return 6
    elif len(set(zero_segments) - set(str)) == 0:
        return 0
    elif len(set(two_segments) - set(str)) == 0:
        return 2
    elif len(set(three_segments) - set(str)) == 0:
        return 3
    elif len(set(five_segments) - set(str)) == 0:
        return 5
    else:
        return -1


sum = 0

for line in lines:
    splitted_line = line.split('|')
    digits = splitted_line[0].strip().split(' ')
    inputs = splitted_line[1].strip().split(' ')
    segments = {}
    unciphered_input = ''
    
    segments = uncipher_one(digits)
    segments = uncipher_seven(digits, segments)
    segments = uncipher_four(digits, segments)
    segments = uncipher_eight(digits, segments)
    segments = uncipher_nine(digits, segments)
    segments = uncipher_six(digits, segments)
    segments = uncipher_zero(digits, segments)
    
    for input in inputs:
        digit = determine_digit(input, segments)
        unciphered_input += str(digit)

    sum += int(unciphered_input)

print(sum)