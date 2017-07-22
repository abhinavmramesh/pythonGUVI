def main():
   
   a = int(input("Enter the length: "))
   b = int(input("Enter the breadth: "))
   c = int(input("Enter the base: "))
   d = int(input("Enter the height: "))
   e = int(input("Enter the side: "))
   print("Area of rect: " + str(a*b))
   print("Area of tri: " + str(0.5*c*d))
   print("Area of sqr: " + str(e**2))
if __name__ == '__main__':
  main()