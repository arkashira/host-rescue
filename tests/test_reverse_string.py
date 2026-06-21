import pytest
from axentx_product import reverse_string


def test_reverse_basic():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("AxentX") == "XtnexA"


def test_reverse_empty():
    assert reverse_string("") == ""


def test_reverse_single_char():
    assert reverse_string("a") == "a"


def test_type_error():
    with pytest.raises(TypeError):
        reverse_string(123)  # type: ignore[arg-type]
