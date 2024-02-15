from datastructures.array import Array

class TestClassTemplate:
    def test_method_template(self):
        # Arrange (set up your test data)


        # Act (perform the action you want to test)


        # Assert (check that the test is passing)
        pass

    def test_from_list_type_error():
        lst='lll'

        
        try:
            array=Array.from_list(lst)
            print(array)
        except TypeError:
            pass
    
    def test_from_list_01():
        lst=[1,2,3,4]

        assert Array.from_list(lst) == [1,2,3,4]

    def test__getitem_01():
        pass

    def test__setitem_01():
        pass

    def test_append_01():
        pass

    def test___len__01():
        pass
    

    

        


        


