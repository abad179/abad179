import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from structural_app.beam import SimpleBeam


class TestSimpleBeam(unittest.TestCase):
    def test_reactions(self):
        beam = SimpleBeam(6.0, 12.0)
        R1, R2 = beam.reactions()
        self.assertAlmostEqual(R1, 36.0)
        self.assertAlmostEqual(R2, 36.0)

    def test_max_values(self):
        beam = SimpleBeam(6.0, 12.0)
        self.assertAlmostEqual(beam.max_shear(), 36.0)
        self.assertAlmostEqual(beam.max_moment(), 54.0)

    def test_diagram_values(self):
        beam = SimpleBeam(6.0, 12.0)
        # At midspan
        self.assertAlmostEqual(beam.shear_at(3.0), 0.0, places=5)
        self.assertAlmostEqual(beam.moment_at(3.0), 54.0)


if __name__ == "__main__":
    unittest.main()
