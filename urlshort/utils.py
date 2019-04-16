import random
import string


def code_gen(code_len=10, chars= string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for a in range(code_len))


def unique_code(instance):
    new_code = code_gen()
    short_class = instance.__class__
    qs = short_class.objects.filter(code=new_code).exists()
    if qs:
        return unique_code()
    return new_code
