'''Tests Helper Functions'''

import bloomdata.helper_functions as hf

def test_random_phrase():
    assert type(hf.random_phrase()) == str
