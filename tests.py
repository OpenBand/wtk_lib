from .wtk import *

import os
import pytest
import sys

# ********************
# Run py.test ./tests.py
#

def test_wrand_get_bool():
    test_entropy=set()
    for _ in range(1, 10):
        curr_rnd = WRand.get_bool()
        test_entropy.add(curr_rnd)
    assert len(test_entropy) == 2

def test_wrand_get_int():
    with pytest.raises(ValueError):
        WRand.get_int(-1000, -10)
        WRand.get_int(-999, 10)
        WRand.get_int(1000, 10)

    test_entropy=set()
    for _ in range(1, 10):
        curr_rnd = WRand.get_int(10, 1000)
        test_entropy.add(curr_rnd)
    assert len(test_entropy) > 1

def test_wrand_choice():
    with pytest.raises(ValueError):
        WRand.choice(999)
        WRand.choice("blabla")

    test_entropy=set()
    decs = list("0123456789")
    for _ in range(1, 10):
        curr_rnd = WRand.choice(decs)
        test_entropy.add(curr_rnd)
    assert len(test_entropy) > 1

def test_wgui_echo_simple():
    WGui.debug("test")
    WGui.message("test")
    WGui.echo("test")
    WGui.ok("test")
    WGui.warning("test")
    WGui.error("test")
    WGui.print("test")

def test_wgui_echo_with_extra_args():
    WGui.echo("Message ", message = "test")
    WGui.echo("Message ", nl = False)
    WGui.echo("Message ", file = sys.stderr)

def test_wgui_hi():
    WGui.Hi("""
        I must not fear.
        Fear is the mind-killer.
        Fear is the little-death that brings total obliteration.
        I will face my fear.
        I will permit it to pass over me and through me.
        And when it has gone past, I will turn the inner eye to see its path.
        Where the fear 
        has gone there will be nothing. Only I will remain.        
    """)

def test_get_bool_environ():
    TEST_ENV="BLABLAVAL"

    assert None == os.environ.get(TEST_ENV)
    assert get_bool_environ(TEST_ENV) == False

    os.environ[TEST_ENV] = 'False'
    assert get_bool_environ(TEST_ENV) == False

    os.environ[TEST_ENV] = 'faLSe'
    assert get_bool_environ(TEST_ENV) == False

    os.environ[TEST_ENV] = '0'
    assert get_bool_environ(TEST_ENV) == False

    os.environ[TEST_ENV] = '000'
    assert get_bool_environ(TEST_ENV) == False

    os.environ[TEST_ENV] = 'True'
    assert get_bool_environ(TEST_ENV) == True

    os.environ[TEST_ENV] = 'TrAAA'
    assert get_bool_environ(TEST_ENV) == True

    os.environ[TEST_ENV] = '1'
    assert get_bool_environ(TEST_ENV) == True

    os.environ[TEST_ENV] = '0001'
    assert get_bool_environ(TEST_ENV) == True
