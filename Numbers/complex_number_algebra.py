# Class to find out real/imaginary part of given complex number
# Also to find out negation and multiplicative inverse
class Number():
    
    def __init__(self,real,imag):
        
        self.real = real
        self.imag = imag
    
    def __str__(self):
        complex_num = complex(self.real,self.imag)
        return f"{complex_num}"
    
    def negation(self):
        negation = -(complex(self.real,self.imag))
        return negation
    
    def inverse(self):
        inversion = (1/complex(self.real,self.imag))* \
                    (complex.conjugate(complex(self.real,self.imag))/complex.conjugate(complex(self.real,self.imag)))
        return inversion
    
# Addition
def add(complex1,complex2):
    return complex1 + complex2

# Subtraction
def subtract(complex1,complex2):
    return complex1 - complex2

# Multiplication
def multiply(complex1,complex2):
    return complex1*complex2

# Division
def devide(complex1,complex2):
    return complex1/complex2

# Example
complex_number = Number(2,3)

print(f"Given complex number: {complex_number}")
print(f"\nReal part of given Complex number: {complex_number.real}")
print(f"Imaginary part of given Complex number: {complex_number.imag}")
print(f"\nNegation of given Complex number: {complex_number.negation()}")
print(f"\nMultiplicative inverse of given Complex number: {complex_number.inverse()}")

a = complex(-3,-6)
b = complex(8,9)

print(f'\nGiven numbers are: {a} and {b}')

print(f"\nAddition of {a} and {b}: {add(a,b)}")
print(f"Subtraction of {a} and {b}: {subtract(a,b)}")
print(f"Multiplication of {a} and {b}: {multiply(a,b)}")
print(f"Division of {a} and {b}: {devide(a,b)}")
