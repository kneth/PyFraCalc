# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


class Fraction:
    def _gcd(self, a, b):
        if a == b:
            return a
        else:
            if a > b:
                return self._gcd(a - b, b)
            else:
                return self._gcd(a, b - a)

    def __init__(self, numerator, denominator):
        gcd = self._gcd(numerator, denominator)
        self.numerator = numerator / gcd
        self.denominator = denominator / gcd

    def __attr__(self, name):
        if name == "numerator":
            return self.numerator
        else:
            if name == "denominator":
                return self.denominator
            else:
                print("Wrong argument")
                return 0

    def __mul__(self, f):
        return Fraction(self.numerator * f.numerator, self.denominator * f.denominator)

    def __add__(self, f):
        return Fraction(
            self.denominator * f.numerator + f.denominator * self.numerator,
            self.denominator * f.denominator,
        )

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
