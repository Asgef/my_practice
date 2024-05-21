# Problem: Building a route in a tree.

# Implement the function build_itinerary() that constructs
# an itinerary between cities.
#
# The function takes 3 arguments:
#
# - tree of cities
# - starting city
# - destination city
#
# It returns a list of cities arranged in the same order as they
# appear on the route.


# Задача: Построение маршрута в дереве.

# Реализуйте функцию build_itinerary(), которая выстраивает маршрут
# между городами.
#
# Функция принимает на вход 3 аргумента:
#
# дерево городов
# город старта
# город окончания маршрута
# и возвращает список городов, выстроенных в том же порядке, в котором
# они находятся на пути следования по маршруту.

# example:

# tree = ['Moscow', [
#     ['Smolensk'],
#     ['Yaroslavl'],
#     ['Voronezh', [
#         ['Liski'],
#         ['Boguchar'],
#         ['Kursk', [
#             ['Belgorod', [
#                 ['Borisovka'],
#             ]],
#             ['Kurchatov'],
#         ]],
#     ]],
#     ['Ivanovo', [
#         ['Kostroma'], ['Kineshma'],
#     ]],
#     ['Vladimir'],
#     ['Tver', [
#         ['Klin'], ['Dubna'], ['Rzhev'],
#     ]],
# ]]
#
# build_itinerary(tree, 'Dubna', 'Kostroma')
# # ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']
#
# build_itinerary(tree, 'Borisovka', 'Kurchatov')
# # ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']


def way_to_city(tree, target):
    if tree[0] == target:
        return [tree[0]]

    if len(tree) > 1:
        for subtree in tree[1]:
            path = way_to_city(subtree, target)
            if path:
                return [tree[0]] + path

    return


def build_itinerary(tree, begin, end):
    path_to_begin = way_to_city(tree, begin)
    path_to_end = way_to_city(tree, end)
    general_path = 0

    for bgn, ed in zip(path_to_begin, path_to_end):
        if bgn == ed:
            general_path += 1
        else:
            break

    path = path_to_begin[:general_path-1:-1] + path_to_end[general_path-1:]
    return path
