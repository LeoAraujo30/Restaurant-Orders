from src.models.ingredient import Ingredient, restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("presunto")
    restriction = restriction_map().get("presunto", set())
    ingredient2 = Ingredient("frango")

    assert ingredient1.name == "presunto"
    assert ingredient1.restrictions == restriction
    assert ingredient1.__hash__() == ingredient1.__hash__()
    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert ingredient1.__eq__(ingredient1) is True
    assert ingredient1.__eq__(ingredient2) is False
    assert ingredient1.__repr__() == "Ingredient('presunto')"
