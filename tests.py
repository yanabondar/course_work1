from utils import get_data, get_filtered_data, get_last_values, get_formatted_data

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{

    }]

def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == [...]

def test_formatted_data(test_data):
    data = get_formatted|_data(test_data)
    assert data == []