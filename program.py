from tests.car import Car, Color, Make, Model
from datastructures.array2d import Array2D
from datastructures.intervaltree import IntervalTree


def main():
    print('Hello world!')

    tree=IntervalTree()
        
    tree.insert(100,150, 'apple')
    tree.insert(150,175, 'microsoft')
    tree.insert(120,160, 'tesla')
    
    tree.insert(200,250, 'google')
    tree.tree._balance_factor(tree.tree._root.right)

    print(tree.search(125))

    # car = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
    # print(car)
    # ar=Array.from_list([1,2,3,4,5,6])
    # ar.append('tada')
    # for item in ar:
    #     print(item)
    # print(len(ar))    
    # ar.clear()
    # print(len(ar))
    # print([[None for i in range(3)] for i in range(3)])
    # print(Array2D(2,2))



if __name__ == '__main__':
    main()
