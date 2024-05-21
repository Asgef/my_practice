from my_practice.python_trees_itinerary_exercise import build_itinerary


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


def test_build_itinerary():

    assert build_itinerary(
        tree, 'Dubna', 'Kostroma'
    ) == ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']

    assert build_itinerary(
        tree, 'Borisovka', 'Kurchatov'
    ) == ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
