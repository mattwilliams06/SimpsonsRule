import numpy as np

class Simpson:
    """ Class containing methods for using Simpson's rule under various conditions. Although designed using Naval
     Architecture applications with the associated terminology, it works for all numerical quadrature applications
     that can be solved with Simpson's Rule.
    """

    def first_rule(self, offsets, lbp, uneven_spacing=False, spacing_array=None):
        """ Calculate definite integrals using Simpson's first rule. Requires an odd number of stations.
        If the spacing between arrays is not constant, the user must set the uneven_spacing flag to True, and pass
        a spacing array.

        Inputs
        ------
        offsets: a 1D array. Contains the y-values or offset value at each station.

        LBP: float. Length of the interval, or length between perpendiculars.

        uneven_spacing: boolean. Default is False. Must be true if the stations/intervals are not set at equal widths.

        spacing_array: a 1D array. This array contains the relative spacing of stations. For example, if the station
        numbers, corresponding to their spacing, were [0, 0.5, 1, 2, 3, 5, 7, 9], then the first two intervals are half-
        spaced, the next two are unit spaced, and the last two are double spaced. The spacing_array would then be
        [0.5, 1.0, 2.0].

        Returns
        -------

        The area under the curve/offsets. For ship applications, the result must be doubled if the offsets are from
        centerline.

        """

        if uneven_spacing:
            area = self.first_rule_uneven_spacing(offsets, lbp, spacing_array)
            return area

        n_stations = len(offsets)
        if n_stations % 2 == 0:
            print('The first rule is for an odd number of stations. Please use the second rule.')
            return None

        n_intervals = n_stations - 1
        dx = lbp / n_intervals
        multipliers = np.array([1, 4, 1])
        n_rows = n_intervals // 2
        mult_array = np.zeros((n_rows, n_stations))
        for i in range(n_rows):
            for j in range(3):
                mult_array[i, 2*i + j] = multipliers[j]
        mults = np.sum(mult_array, axis=0)
        area = dx / 3 * np.sum(mults * offsets)

        return area

    def first_rule_uneven_spacing(self, offsets, lbp, spacing_array):
        """ This method is invoked if there is non-constant spacing between stations. It does not need to be called
        directly. It will be invoked if the flag uneven_spacing is set to True.
        """

        n_stations = len(offsets)
        if n_stations % 2 == 0:
            print('The first rule is for an odd number of stations. Please use the second rule.')
            return None

        n_intervals = n_stations - 1
        dx = lbp / n_intervals
        multipliers = np.array([1, 4, 1])
        n_rows = n_intervals // 2
        mult_array = np.zeros((n_rows, n_stations))
        for i in range(n_rows):
            for j in range(3):
                mult_array[i, 2 * i + j] = multipliers[j] * spacing_array[i]
        mults = np.sum(mult_array, axis=0)
        area = dx / 3 * np.sum(mults * offsets)
        self.waterplane_area = area * 2

        return area

    def second_rule(self, offsets, lbp):
        """ This method if for using Simpson's Second rule. The constraint is that the number of stations - 1 must
        be divisible by 3
        """

        n_stations = len(offsets)
        n_intervals = n_stations - 1
        if n_intervals % 3 != 0:
            print('The number of intervals must be divisible by 3. Please select a different rule.')
            return None

        multipliers = np.array([1., 3., 3., 1.])
        dx = lbp / n_intervals
        n_rows = n_intervals // 3
        mult_array = np.zeros((n_rows, n_stations))
        for row in range(n_rows):
            for col in range(4):
                mult_array[row, 3 * col + col] = multipliers[col]
        mults = np.sum(mult_array, axis=0)
        area = (dx * 3 / 8) * mults * offsets

        return area




