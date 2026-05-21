from test_lib import test, report

test('grootste 1', 10, grootste(10, 5))
test('grootste 2', 7, grootste(3, 7))
test('grootste gelijk', 4, grootste(4, 4))
test('grootste negatief', -2, grootste(-2, -5))

report()