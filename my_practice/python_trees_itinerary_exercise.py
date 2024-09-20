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


def build_city_routes(node, routes):
    if len(node) == 1:
        city = node[0]
        routes[city] = []
        return city

    city, neighdbords = node
    routes[city] = []

    for tree in neighdbords:
        neighdbord = build_city_routes(tree, routes)
        routes[city].append(neighdbord)
        routes[neighdbord].append(city)
    return city


def search_way(start, finish, path, routes):
    if start == finish:
        return path + [finish]

    for city in routes[start]:
        if city in path:
            continue
        rest = search_way(city, finish, path + [start], routes)
        if rest:
            return rest


def build_itinerary(tree, start_sity, finish_city):
    routes = {}  # Список смежностей
    build_city_routes(tree, routes)
    return search_way(start_sity, finish_city, [], routes)

# Графы, DFS, обход в глубиу, список смежностей
