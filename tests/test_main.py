import main
import pytest
@pytest.fixture
def test_read_txt():
    data = main.read_txt("testtext.txt")
    return data

def test_sort_area(test_read_txt):
    data = test_read_txt
    sorted_data = main.sort_area(data)
    expected_data = [('Франція', 100000.0, 80000),
                     ('Англія', 200000.0, 15000),
                     ('Україна', 600000.0, 42000),
                     ('Німечинна', 800000.0, 50000),
                     ('США', 900000.0, 17000),
                     ('Китай', 1000000.0, 900000)]
    assert sorted_data == expected_data

def test_sort_population(test_read_txt):
    data = test_read_txt
    sorted_data = main.sort_population(data)
    expected_data = [('Англія', 200000.0, 15000),
                     ('США', 900000.0, 17000),
                     ('Україна', 600000.0, 42000),
                     ('Німечинна', 800000.0, 50000),
                     ('Франція', 100000.0, 80000),
                     ('Китай', 1000000.0, 900000)]
    assert sorted_data == expected_data