import main
import pytest
@pytest.fixture
def test_read_txt():
    data = main.read_txt("testtext.txt")
    return data

