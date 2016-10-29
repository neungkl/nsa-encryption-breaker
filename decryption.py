def nsa_encrypt(key, text) :
    result = 0
    for i in range(0, len(text)) :
        result = result + ord(text[i:i+1])
        result = result * key
    return result

def find_near_key(hash, sample_text) :
    [l,r] = [0, hash // 2]
    lens = len(sample_text)
    while l <= r :
        c = (l + r) // 2
        if nsa_encrypt(c, sample_text) < hash :
            l = c + 1
        else :
            r = c - 1
    return l

def factorize(hash) :
    list = []
    should_pause = False
    while hash > 1 :
        if should_pause :
            break
        if hash % 2 == 0 :
            list.append(2)
            hash = hash // 2
        else :
            i = 3
            while hash % i != 0 :
                if i % 2000000 == 0 :
                    print ("Calculating...")
                if i > 10000000 :
                    should_pause = 1
                    break
                i = i + 1
            list.append(i)
            hash = hash // i
    return list


def find_best_key(factor, lower_key, upper_key, hash) :

    prop_key = 1
    for n in range(0, len(factor)) :

        prop_key = 1
        for i in range(n, len(factor)) :
            if prop_key * factor[i] >= lower_key :
                break
            prop_key *= factor[i]

        i = 1
        while prop_key * i < lower_key :
            i = i + 1
        prop_key = prop_key * i

        if prop_key < lower_key or upper_key < prop_key :
            continue

        if hash % prop_key != 0 :
            continue

        break

    return prop_key

def find_best_plain_text(key, lower_key_str, upper_key_str, hash) :
    l = int(lower_key_str, 16)
    r = int(upper_key_str, 16)

    def to_hex(num) :
        return str(hex(num).split('x')[1].split('L')[0])

    while l <= r :
        c = (l + r) // 2
        if nsa_encrypt(key, to_hex(c)) < hash :
            l = c + 1
        else :
            r = c - 1

    return to_hex(l)



if __name__ == "__main__" :

    print ("================================================")
    print ("  NSA Encryption break by Kosate Limpongsa")
    print ("================================================")

    hash = 434384569820012709749978085023147407174684824178941182826833799495931410023794845922767533429746537016995520506439457550763575993604402054742042654701475990703513534158579743446096171193503041071008550601683001839024513922875537448251544812606790879783442587227277601837740236112564627038091170167413493638174350319534049389495771259593223970367601200671312435588244337256711215093040169407379877379400242759675821842258110296156050808143302683071999772732555638568114446076107646435540182476596386155629693774180289540430199704239923354089531930534807431109632462125230336414045829798557815327441670222304200
    lens = 32
    sample_lower = "".join(['0']*lens)
    sample_upper = "".join(['f']*lens)

    print ("Hash:\n" + str(hash))
    print ("")

    print ("================================================")
    print ("  Find Key")
    print ("================================================")

    print ("Sample text length: " + str(lens))

    lower_key = find_near_key(hash, sample_upper) - 1
    # lower_key = 9060764011643293511
    upper_key = find_near_key(hash, sample_lower) + 1
    # upper_key = 9276727210565429884

    factor = factorize(hash)
    print
    print ("Some divisible numbers: ")
    print (factor)
    factor = factor[::-1]

    prop_key = find_best_key(factor, lower_key, upper_key, hash)

    print ("")
    print ("Lower bound key: " + str(lower_key))
    print ("Best  Possible:  " + str(prop_key))
    print ("Upper bound key: " + str(upper_key))

    print ("")
    print ("================================================")
    print ("  Find Plain Text")
    print ("================================================")

    text_result = find_best_plain_text(prop_key, sample_lower, sample_upper, hash)

    print (text_result)

    print ("")
    print ("================================================")
    print ("  Checking")
    print ("================================================")

    print ("Key:        " + str(prop_key))
    print ("Plain Text: " + str(text_result))

    if nsa_encrypt(prop_key, text_result) == hash :
        print ("Correct!")
    else :
        print ("Reject!")
    print
