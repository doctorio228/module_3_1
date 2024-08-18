calls = 0
def count_calls():
    global calls
    calls += 1
a = ''
def string_info(a):
    count_calls()
    b = int(len(a))
    c = a.upper()
    d = a.lower()
    tuple_ = b, c, d
    return (tuple_)
string_ = ''
list_ = []
def is_contains(string_, list_):
    count_calls()
    string_lower = string_.lower()
    return string_lower in (i.lower() for i in list_)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(f'Функции были вызваны {calls} раза.')


