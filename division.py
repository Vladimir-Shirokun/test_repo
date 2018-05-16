#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Divide one number by another')
    parser.add_argument('numerator', type=float, help='Numerator')
    parser.add_argument('divisor', type=float, help='Divisor')
    
// one else commit


    args = parser.parse_args()
    if ( args.divisor == 0)
        print("Division on Null is incoreect")
    else
        print(args.numerator / args.divisor)
// make comment
