# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
import pytest
from datastructures.array2d import Array2D


class TestArray2d:
    def test_method_template(self):
        # Arrange (set up your test data)


        # Act (perform the action you want to test)


        # Assert (check that the test is passing)
        pass
    def test_from_list_01(self):
        lst=[[None for i in range(3)] for i in range(3)]

        array=Array2D.from_list(lst)

        assert Array2D(3,3) == array
    
    def test_getitem_01(self):
        array=Array2D.from_list([[1,2,3],
                                 [4,5,6],
                                 [7,8,9]])

        assert array[1][1] == 5

    def test_getitem_row_01(self):
        array=Array2D.from_list([[1,2,3],
                                 [4,5,6],
                                 [7,8,9]])

        assert array[0] == [1,2,3]
    
    def test_getitem_error_01(self):
        array=Array2D.from_list([[1,2,3],
                                 [4,5,6],
                                 [7,8,9]])

        try:
            array[-1]
        except IndexError:
            pass

    def test_getitem_error_02(self):
        array=Array2D.from_list([[1,2,3],
                                 [4,5,6],
                                 [7,8,9]])

        try:
            array[0][-1]
        except IndexError:
            pass
    
    def test_getitem_error_03(self):
        array=Array2D.from_list([[1,2,3],
                                 [4,5,6],
                                 [7,8,9]])

        try:
            array[3]
        except IndexError:
            pass

    def test_getitem_error_04(self):
        array=Array2D.from_list([[1,2,3],
                                 [4,5,6],
                                 [7,8,9]])

        try:
            array[0][3]
        except IndexError:
            pass
