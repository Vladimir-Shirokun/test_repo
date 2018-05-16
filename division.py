#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Divide one number by another')
    parser.add_argument('numerator', type=float, help='Numerator')
    parser.add_argument('divisor', type=float, help='Divisor')
    
<<<<<<< HEAD
// one else commit


=======
    
    
    
>>>>>>> 91baf9f1931565391094689b9f12f25beb8555f3
    args = parser.parse_args()
    if ( args.divisor == 0)
    
    
    ////asdasdasdasdasdasdassssssssssssssssssssssssssssssssssssssssss
    
        print("Division on Null is incoreect")
    else
        print(args.numerator / args.divisor)
// make comment
