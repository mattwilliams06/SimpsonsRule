import simpson
from simpson import Simpson
import numpy as np
from numpy.testing import assert_allclose

x = np.linspace(0, 1, 11)
y = x
LBP = 1
test_simps = Simpson()
y_uneven = np.array([0., 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.])
spacing_array = np.array([0.5, 1., 1., 1., 1., 0.5])

def test_first_rule():
    solution = 0.5
    assert_allclose(solution, test_simps.first_rule(y, LBP))


def test_first_rule_uneven_spacing():
    solution_uneven = 0.4416666666666666
    assert_allclose(solution_uneven, test_simps.first_rule_uneven_spacing(y_uneven, LBP, spacing_array))


