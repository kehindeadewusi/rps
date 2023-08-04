from billups.numbers.stately.state import state_num


def test_state():
    n = state_num("plateau")

    assert n == 100
