'''Testing Wallet Class'''
import pytest
from bloomdata.wallet import Wallet

@pytest.fixture
def empty_wallet():
    '''Fixing an instance of an empty wallet'''
    return Wallet()

@pytest.fixture
def wallet_20():
    '''Fixing an instance of a $20 wallet'''
    return Wallet(20)

def test_empty_wallet(empty_wallet):
    '''Intent to test the empty wallet'''
    assert empty_wallet.balance == 0

def test_wallet_20(wallet_20):
    '''Test a wallet with 20'''
    assert Wallet(20).balance == 20

def test_wallet_20_spend_10(wallet_20):
    '''Test a wallet spending 10'''
    assert wallet_20.spend_cash(10) == 'Remaining Balance: $10'
    assert wallet_20.balance == 10

def test_spend_all_cash(wallet_20):
    '''Testing the method spend cash at upper limit'''
    assert wallet_20.spend_cash(20) == 'Remaining Balance: $0'
    assert wallet_20.balance == 0
