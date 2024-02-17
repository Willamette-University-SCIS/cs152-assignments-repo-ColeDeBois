from datastructures.array import Array

class TestArray:
    def test_method_template(self):
        # Arrange (set up your test data)


        # Act (perform the action you want to test)


        # Assert (check that the test is passing)
        pass

    def test_from_list_type_error(self):
        lst='lll'
        try:
            array=Array.from_list(lst)
            print(array)
        except TypeError:
            pass
    
    def test_from_list_01(self):
        lst=[1,2,3,4]

        assert Array.from_list(lst) == [1,2,3,4]

    def test__getitem_01(self):
        lst=[1,2,3,4]
        array=Array.from_list(lst)
        assert array[0] == lst[0]

    def test__getitem_02(self):
        lst=[1,2,3,4]
        array=Array.from_list(lst)
        try:
            array[4]
        except:
            IndexError

    def test__setitem_01(self):
        array=Array(size=5)
        array[0]='good'
        assert array[0] == 'good'

    def test___len__01(self):
        lst=[1,2,3,4]
        array=Array.from_list(lst)
        assert len(array) == len(lst)

    def test_append_01(self):
        lst=[1,2,3,4]
        array=Array.from_list(lst)

        array.append(5)
        assert array[4] == 5

    def test_len_append(self):
        lst=[1,2,3,4]
        array=Array.from_list(lst)

        array.append(5)
        assert len(array) == 5

    def test_ne_equal_sized(self):
        lst1=[2,3,2]
        lst2=[1,2,3]
        array1=Array.from_list(lst1)
        array2=Array.from_list(lst2)

        assert array2 != array1
    
    def test_ne_type(self):
        lst1=[2,3,2]
        array1=Array.from_list(lst1)
        assert array1 != lst1

    def test_eq_different_sizes(self):
        lst1=[1,2,3,4]
        lst2=[1,2,3]
        array1=Array.from_list(lst1)
        array2=Array.from_list(lst2)

        assert not array2 == array1

    def test_eq_different_entries(self):
        lst1=[1,4,3]
        lst2=[1,2,3]
        array1=Array.from_list(lst1)
        array2=Array.from_list(lst2)

        assert not array2 == array1

    def test_del_01(self):
        lst=[1,2,3,4]
        array=Array.from_list(lst)

        del array[1]

        assert array == Array.from_list([1,3,4])


    
    

    

        


        


