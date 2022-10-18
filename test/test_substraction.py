from src.calculator import subtract
import pytest
def test_subtract():
    result = subtract(3, 4)
    assert result == 7
def test_subtract_string():
    with pytest.raises(TypeError):
        subtract("string", 4)