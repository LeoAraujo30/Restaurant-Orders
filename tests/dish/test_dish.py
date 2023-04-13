from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, restriction_map
import pytest


# Req 2
def test_dish():
    dish1 = Dish("lasanha presunto", 25.90)
    dish2 = Dish("lasanha berinjela", 27.00)

    assert dish1.name == "lasanha presunto"
    assert dish1.price == 25.90
    assert dish1.recipe == {}
    assert dish1.__repr__() == "Dish('lasanha presunto', R$25.90)"
    assert dish1.__hash__() == dish1.__hash__()
    assert dish1.__hash__() != dish2.__hash__()
    assert dish1.__eq__(dish1) is True
    assert dish1.__eq__(dish2) is False

    dish1.add_ingredient_dependency(Ingredient("presunto"), 15)
    dish1.add_ingredient_dependency(Ingredient("queijo mussarela"), 15)

    restriction1_presunto = restriction_map().get("presunto", set())
    restriction1_queijo = restriction_map().get("queijo mussarela", set())

    assert dish1.get_restrictions() == restriction1_presunto.union(
        restriction1_queijo
    )
    assert dish1.get_ingredients() == {
        Ingredient('presunto'), Ingredient('queijo mussarela')
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha presunto", "dasdas")

    with pytest.raises(
        ValueError,
        match="Dish price must be greater then zero."
    ):
        Dish("lasanha berinjela", -27.00)
