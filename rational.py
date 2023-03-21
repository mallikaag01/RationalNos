#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Mar 16 00:02:18 2023

Defining a Rational number class

Refer to the instructions on Canvas for more information.

"I have neither given nor received unauthorized help on this assignment."
@author: Mallika Gupta
date: March 18, 2023
"""
__version__ = 1

class Rational:
    
    '''
    Initialize a new Rational object with value iNum/iDen stored in hidden __numerator and
    __denominator variables.  Calls the reduce() method to put the fraction in lowest terms.
    '''
    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()

##The method getNumerator() will call the reduce() method to put the udpated 
##rational in lowest terms.
    def getNumerator(self):
        return self.__numerator

##The method getDenominator() will call the reduce() method to put the udpated 
##rational in lowest terms.   
    def getDenominator(self):
        return self.__denominator
        
##The method setNumerator() is created for both the __numerator and __denominator
##instance variables.This will call the reduce() method which will put the 
##updated rational in lowest terms.
    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()

##The method setDenominator() is created for both the __numerator and __denominator
##instance variables.This will call the reduce() method which will put the 
##updated rational in lowest terms.
    def setDenominator(self, d):
        self.__denominator = d
        self.reduce()      
 
##The method isValid(self) is created due to the fact that rational numbers
##cannot have a zero in the denominator. The method will return True() if the 
##rational is valid and return False() if the rational has a denominator whi
##is zero.
    def isValid(self):
        return self.__denominator != 0
    
##The method add(self,num2) is used to add num2 to the current rational. This
##will update the the self.__numerator and self.__denominator instance variables
##to the sum of self and num2.I called the self.reduce() method which would 
##help put the rational in lowest terms.
    def add(self, num2):
        self.__numerator = self.__numerator * num2.getDenominator() + num2.getNumerator() * self.__denominator
        self.__denominator *= num2.getDenominator()
        self.reduce()       
        
##The method sub(self,num2) is used to subtract num2 to the current rational. This
##will update the the self.__numerator and self.__denominator instance variables
##to the sum of self and num2.I called the self.reduce() method which would 
##help put the rational in lowest terms.
    def sub(self, num2):
        self.__numerator = self.__numerator * num2.getDenominator() - num2.getNumerator() * self.__denominator
        self.__denominator *= num2.getDenominator()
        self.reduce()
          
##The method mult(self,num2) is used to multiply num2 to the current rational. 
##This will update the the self.__numerator and self.__denominator instance 
##variables to the product of self and num2.I called the self.reduce() method 
##which would help put the rational in lowest terms. 
    def mult(self, num2):
        self.__numerator *= num2.getNumerator()
        self.__denominator *= num2.getDenominator()
        self.reduce()
        
##The method div(self,num2) is used to divide num2 to the current rational. 
##This will update the the self.__numerator and self.__denominator instance 
##variables to the result of dividing self and num2.I called the self.reduce() 
##method which would help put the rational in lowest terms.    
    def div(self, num2):
        self.__numerator *= num2.getDenominator()
        self.__denominator *= num2.getNumerator()
        self.reduce() 
    
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################
    '''
    Reduces the Rational to lowest terms
      - Checks if both the numerator and denominator are negative; if so, makes both positive
      - Calls gcf() to find the greatest common factor between the numerator and denominator, and
        continues to divide by that gcf until the greatest common factor is 1
    '''
    def reduce(self):
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    '''
    Determines the greatest common factor between the numerator and denominator
      - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
      - When it finds a number divisble by both, it breaks the loop and returns that number
      - The smallest number that can be returned is 1
    '''
    def gcf(self):
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    '''
    Returns a string representation of the Rational, e.g. "1/8"
    '''
    def __str__(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    '''
    Determines if two Rationals are exactly equal to each other (same numerator and same
    denominator, no consideration of reducing the numbers)
    '''
    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    

## The main function is used to call the test case functions.
def main():
    testGetNumerator()
    testGetDenominator()
    testSetNumerator()
    testSetDenominator()
    testIsValid()
    testAdd()
    testSub()
    testMult()
    testDiv()

##I created a rational object with numerator 3 and denominator 4 for testing 
##the first four functions.
r = Rational(3, 4)
r5 = Rational(4,5)
r6 = Rational(6,7)


###############################################################

# Here is where you will write your test case functions

##The testGetNumerator() method is created to help see if the above method 
##getNumerator() gives the correct result.For example, if the value of r1 is 3/4,
##the result should be 3.
def testGetNumerator():
   assert r.getNumerator() == 3
   assert r5.getNumerator() == 4
   assert r6.getNumerator() == 6

##The testGetDenominator() method is created to help see if the above method 
##getDenominator() gives the correct result.For example, if the value is of r1
##is 3/4, the result should be 4.
def testGetDenominator():
   assert r.getDenominator() == 4
   assert r5.getDenominator() == 5
   assert r6.getDenominator() == 7

##The testSetNumerator() method is created to help see if the above method 
##setNumerator() gives the correct result.For example, if the value is of r1
##is 3/14,r1 is updated to 7/14 and will reduce to 1/2.
def testSetNumerator(n):
    assert r.setNumerator(n)==1/2
    assert r.setNumerator(n)==1/2
    assert r.setNumerator(n)==1/2

##The testSetDenominator() method is created to help see if the above method 
##setDenominator() gives the correct result.For example, if the value is of r1
##is 3/14, it will give the result 3/-4
def testSetDenominator(n):
    assert r.setDenominator(n)==3/-4
    assert r.setDenominator(n)==3/-4
    assert r.setDenominator(n)==3/-4

##The testIsValid() method is created to help see if the above method 
##isValid() gives the correct result.For example, if the value is of r1
##is 7/4, the result will be True and False if r1 is 7/0.
def testIsValid():
    assert r.isValid(7/4) == True
    assert r.isValid(7/0) == False
    assert r.isValid(9/5) == True


##The testAdd() method is created to help see if the correct result is given.
##For example, if r1 is 1/4 and r2 is 1/2, the result will be 3/8 after adding 
#both of those numbers.
def testAdd():
    assert r.Add("1/4","1/2") == "3/8"
    assert r.Add("1/2","1/3") == "5/6"
    assert r.Add("3/4","1/2") == "5/4"

##The testSub() method is created to help see if the correct result is given.
##For example, if r1 is 1/4 and r2 is 1/2, the result will be 1/8 after taking
## the difference of those numbers.
def testSub():
    assert r.Sub("1/4","1/2") == "1/8"
    assert r.Sub("1/2","1/3") == "1/6"
    assert r.Sub("3/4","1/2") == "1/4"

##The testMult() method is created to help see if the correct result is given.
##For example, if r1 is 1/4 and r2 is 1/2, the result will be 1/8 after taking
## the product of those numbers.
def testMult():
    assert r.Mult("1/4","1/2") == "1/8"
    assert r.Mult("1/2","1/3") == "1/6"
    assert r.Mult("3/4","1/2") == "3/8"

##The testDivt() method is created to help see if the correct result is given.
##For example, if r1 is 1/4 and r2 is 1/2, the result will be 1/2 after 
##diving both those numbers.
def testDiv():
    assert r.Div("1/4","1/2") == "1/2"
    assert r.Div("1/2","1/3") == "3/2"
    assert r.Div("3/4","1/2") == "3/2"

    


    
###############################################################    
    
if __name__ == "__main__":
    main()    