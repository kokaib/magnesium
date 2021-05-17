import unittest
from pathlib import Path
import pandas as pd
from pandas._testing import assert_frame_equal
import sys
sys.path.append('src')

from magnesium.prefab import (
    PandasPrefab,
    ListOfDictsPrefab
)


BASE_DIR = Path(__file__).parent


class XMLTestCase(unittest.TestCase):
    def test_pandas_prefab(self):
        with open(BASE_DIR / 'basic_schema.xml', 'r', encoding='utf-8') as fp:
            schema_data = fp.read()

        with open(BASE_DIR / 'basic_sample.xml', 'r', encoding='utf-8') as fp:
            sample_data = fp.read()

        prefab = PandasPrefab(schema_data=schema_data)
        results = prefab.execute(sample_data)

        expected_results = pd.read_csv(BASE_DIR / 'basic_expected_results.csv')
        assert_frame_equal(expected_results, results)

    def test_list_of_dicts_prefab(self):
        with open(BASE_DIR / 'basic_schema.xml', 'r', encoding='utf-8') as fp:
            schema_data = fp.read()

        with open(BASE_DIR / 'basic_sample.xml', 'r', encoding='utf-8') as fp:
            sample_data = fp.read()

        prefab = ListOfDictsPrefab(schema_data=schema_data)
        results = prefab.execute(sample_data)

        expected_results = [
            {'lede': 'cd', 'pubDate': 'ef', 'title': 'ab'},
            {'lede': 'ij', 'pubDate': 'kl', 'title': 'gh'},
            {'lede': 'op', 'pubDate': 'qr', 'title': 'mn'},
            {'lede': 'uv', 'pubDate': 'wx', 'title': 'st'},
            {'lede': 'ab', 'pubDate': 'cd', 'title': 'yz'},
        ]
        self.assertListEqual(expected_results, results)
