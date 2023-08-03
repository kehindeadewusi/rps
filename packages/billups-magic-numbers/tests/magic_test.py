from billups.numbers.magic import secret_number_generator


def test_magic():
    n = secret_number_generator()

    assert n >= 0
