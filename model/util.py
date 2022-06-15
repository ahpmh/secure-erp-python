import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    random_small_letters = [random.choice(
        string.ascii_lowercase) for letter in range(number_of_small_letters)]
    random_capital_letters = [random.choice(
        string.ascii_uppercase) for letter in range(number_of_capital_letters)]
    random_digits = [random.choice(str(string.digits))
                     for number in range(number_of_digits)]
    random_spec_chars = [random.choice(
        allowed_special_chars) for chars in range(number_of_special_chars)]
    # összeadja a random kiválaszott betűket, számokat és spec karaktereket egy listába rendezetten
    half_random_id = random_small_letters + \
        random_capital_letters + random_digits + random_spec_chars
    # összekeveri a random kiválasztott betűket, számokat és spec karaktereket
    random.shuffle(half_random_id)
    random_id = ''.join(half_random_id)

    return random_id

    # return 'T!uq6-b4Yq'
