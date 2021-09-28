import unittest

import datapipeline_tests


class VersionTestCase(unittest.TestCase):
    """Version tests"""

    def test_version(self):
        """check datapipeline_tests exposes a version attribute"""
        self.assertTrue(hasattr(datapipeline_tests, "__version__"))
        self.assertIsInstance(datapipeline_tests.__version__, str)
