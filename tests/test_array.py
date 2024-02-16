from datastructures.array import Array

class test_Array_Methods:
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
        lst=[1,2,3,4]
        array=Array.from_list(lst)
        assert array[0] == lst[0]

    def test__setitem_01():
        array=Array(size=5)
        array[0]='good'
        assert array[0] == 'good'

    def test___len__01():
        lst=[1,2,3,4]
        array=Array.from_list(lst)
        assert len(array) == len(lst)

    def test_append_01():
        lst=[1,2,3,4]
        array=Array.from_list(lst)

        array.append(5)
        assert array[4] == 5

    def test_len_append():
        lst=[1,2,3,4]
        array=Array.from_list(lst)

        array.append(5)
        assert len(array) == 5
        

    
    

    

        


        


