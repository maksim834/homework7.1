# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
my_dikt = {'Ivan': 1982, 'Anna': 1987, 'Sergey': 1980}
print(my_dikt)
print(my_dikt['Anna'])
print(my_dikt.get('Egor'))
my_dikt.update({'Mariya': 1984, 'Dariya': 1990})
print(my_dikt)
a = my_dikt.pop('Dariya')
print(my_dikt)
print(a)

my_set = {3, 5, 'd', 'd', 'fool', 6}
print(my_set)
print(my_set.add(8))
print(my_set)
print(my_set.add('S'))
print(my_set)
print(my_set.remove('fool'))
print(my_set)