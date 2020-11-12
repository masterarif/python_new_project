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

# create another objects against MyComplexNumber class
# and create a new attribute 'new_attribute'
cmplx2 = MyComplexNumber(60,70)
cmplx2.new_attribute = 80
print((cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute))

# Deleting object attributes and the object
print(cmplx1)
del cmplx1.real_part
del cmplx1

# print(cmplx1)
#Error object deleted

