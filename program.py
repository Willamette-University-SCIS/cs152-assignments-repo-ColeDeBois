from tests.car import Car, Color, Make, Model
# from datastructures.array import Array

def main():
    print('Hello world!')

    car = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
    print(car)
    # ar=Array.from_list([1,2,3,4,5,6])
    # ar.append('tada')
    # for item in ar:
    #     print(item)
    # print(len(ar))    
    # ar.clear()
    # print(len(ar))


if __name__ == '__main__':
    main()
