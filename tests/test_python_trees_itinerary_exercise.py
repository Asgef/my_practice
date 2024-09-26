from my_practice.python_trees_itinerary_exercise import (
    build_itinerary, build_city_routes
)


tree = ['Moscow', [
    ['Smolensk'],
    ['Yaroslavl'],
    ['Voronezh', [
        ['Liski'],
        ['Boguchar'],
        ['Kursk', [
            ['Belgorod', [
                ['Borisovka'],
            ]],
            ['Kurchatov'],
        ]],
    ]],
    ['Ivanovo', [
        ['Kostroma'], ['Kineshma'],
    ]],
    ['Vladimir'],
    ['Tver', [
        ['Klin'], ['Dubna'], ['Rzhev'],
    ]],
]]


def test_build_sity_roytes():
    routes = {}
    build_city_routes(tree, routes)
    assert routes == {
        'Belgorod': ['Borisovka', 'Kursk'],
        'Boguchar': ['Voronezh'],
        'Borisovka': ['Belgorod'],
        'Dubna': ['Tver'],
        'Ivanovo': ['Kostroma', 'Kineshma', 'Moscow'],
        'Kineshma': ['Ivanovo'],
        'Klin': ['Tver'],
        'Kostroma': ['Ivanovo'],
        'Kurchatov': ['Kursk'],
        'Kursk': ['Belgorod', 'Kurchatov', 'Voronezh'],
        'Liski': ['Voronezh'],
        'Moscow': [
            'Smolensk', 'Yaroslavl', 'Voronezh', 'Ivanovo', 'Vladimir', 'Tver'
        ],
        'Rzhev': ['Tver'],
        'Smolensk': ['Moscow'],
        'Tver': ['Klin', 'Dubna', 'Rzhev', 'Moscow'],
        'Vladimir': ['Moscow'],
        'Voronezh': ['Liski', 'Boguchar', 'Kursk', 'Moscow'],
        'Yaroslavl': ['Moscow']
    }


def test_build_itinerary():

    assert build_itinerary(
        tree, 'Dubna', 'Kostroma'
    ) == ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']

    assert build_itinerary(
        tree, 'Borisovka', 'Kurchatov'
    ) == ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
