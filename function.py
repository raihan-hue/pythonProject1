def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(neme1, neme2):
  print(neme1 + " Kamisaki " + neme2)

my_function("holo", "hi")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**buku):
  print("aku mempunyai buku " + buku["buku2"])

my_function(buku1 = "matematika", buku2 = "b.indo")


def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsne")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print(my_function(2))
print(my_function(7))
print(my_function(999999))
print(my_function(9123))
print(my_function(4129))


def my_function():
  pass


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)