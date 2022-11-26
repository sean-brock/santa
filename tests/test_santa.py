import pytest
from santa.assign import santa, validate

@pytest.mark.parametrize("keys,vals,valid", [([1,2,3,4], [2,3,4,1], True), ([1,2],[3,3],False), ([1,2], [1,2], False), ([1,2], [2,2], False)])
def test_validate(keys, vals, valid):
    pairs = {}
    for i in range(len(keys)):
        pairs[keys[i]] = vals[i]

    assert validate(pairs) == valid

@pytest.mark.parametrize("data", [[1,2,3,4], ["sd","asd","asdad"], ["d","e"]])
def test_santa(data):
    pairs = santa(data)
    assert validate(pairs)
