from grid import Grid, Row, Column, Box, Square

import pytest

@pytest.fixture
def grid():
    yield Grid()

class TestGrid:

    def test_grid_exists(self, grid):
        assert isinstance(grid, Grid)
        #assert hasattr(grid, 'boxes')
        #assert hasattr(grid, 'rows')
        #assert hasattr(grid, 'columns')
        assert hasattr(grid, 'squares')
    
    #def test_grid_has_nine_rows(self, grid):
    #    assert len(grid.rows) == 9
    
    #def test_grid_has_nine_columns(self, grid):
    #    assert len(grid.columns) == 9

    #def test_grid_has_nine_boxes(self, grid):
    #    assert len(grid.boxes) == 9
    
    #@pytest.mark.parametrize("test_input,expected", [(i, 9) for i in range(9)])
    #def test_row_has_nine_squares(self, grid, test_input, expected):
    #    assert len(grid.rows[test_input].squares) == expected

    #@pytest.mark.parametrize("test_input,expected", [(i, 9) for i in range(9)])
    #def test_column_has_nine_squares(self, grid, test_input, expected):
    #    assert len(grid.columns[test_input].squares) == expected
    
    #@pytest.mark.parametrize("test_input,expected", [(i, 9) for i in range(9)])
    #def test_box_has_nine_squares(self, grid, test_input, expected):
    #    assert len(grid.boxes[test_input].squares) == expected


@pytest.fixture
def square():
    yield Square(0, 0)

class TestSquare:

    def test_square_exists(self, square):
        assert isinstance(square, Square) == True
    
    def test_square_has_required_attributes(self, square):
        assert hasattr(square, 'value')
        assert hasattr(square, 'grid_row_index')
        assert hasattr(square, 'grid_column_index')
        assert hasattr(square, 'box_row_index')
        assert hasattr(square, 'box_column_index')

@pytest.fixture
def box():
    yield Box(0, 0)
    
class TestBox:

    def test_box_exists(self, box):
        assert isinstance(box, Box) == True
    
    def test_square_has_required_attributes(self, box):
        assert hasattr(box, 'grid_box_index')
        assert hasattr(box, 'grid_box_row_index')
        assert hasattr(box, 'grid_box_column_index')
        assert hasattr(box, 'square_indices')