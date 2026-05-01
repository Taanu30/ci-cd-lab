import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_data

def test_load_data():
    df = load_data()
    assert not df.empty
