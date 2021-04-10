from square import Square
import pytest

@pytest.fixture
def square(self):
    yield Square()

class TestSquare:

    def test_square_exists(self, square):
        assert isinstance(square_init, Square) == True
    
    def test_square_has_required_attributes(self, square_init):
        assert hasattr(square_init, 'value')
        assert hasattr(square_init, 'horizontal_row_number')
        assert hasattr(square_init, 'vertical_column_number')
        assert hasattr(square_init, 'horizontal_box_number')
        assert hasattr(square_init, 'vertical_box_number')