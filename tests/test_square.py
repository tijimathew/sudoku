from square import Square

import pytest

@pytest.fixture
def square():
    yield Square(0,0,0,0)

class TestSquare:

    def test_square_exists(self, square):
        assert isinstance(square, Square) == True
    
    def test_square_has_required_attributes(self, square):
        assert hasattr(square, 'value')
        assert hasattr(square, 'horizontal_row_number')
        assert hasattr(square, 'vertical_column_number')
        assert hasattr(square, 'horizontal_box_number')
        assert hasattr(square, 'vertical_box_number')
           