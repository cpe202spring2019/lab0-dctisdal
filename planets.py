def weight_on_planets():
    mass = int(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh %s pounds." % (mass * 0.38) +
          "\nOn Jupiter you would weigh %s pounds." % (mass * 2.34))


if __name__ == '__main__':
   weight_on_planets()
