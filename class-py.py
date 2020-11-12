class MyComplexNumber:
    # Constructor methods
    def __init__(self,real = 0, imag = 0):
        print("MyComplexNumber constructor excecuting...")
        self.real_part = real
        self.imag_part = imag

    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part,self.imag_part))
# Create a new object against MyComplexNumber class
cmplx1 = MyComplexNumber(40,50)

# calling displayComplex() function
# Output: 40 + 50j
cmplx1.displayComplex()
