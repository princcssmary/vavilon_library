import random
import sent_for_text
import string


def generate_text(num_of_sent_in_text):
    dot = ". "
    punc = string.punctuation
    random_text = ''.join((sent_for_text.generate_sent(random.randint(1,7)) + random.choice(punc)) for i in range(num_of_sent_in_text))
    return random_text

