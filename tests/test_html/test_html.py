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


class HTMLTestCase(unittest.TestCase):
    def test_basic_prefab(self):
        with open(BASE_DIR / 'basic_schema.xml', 'r', encoding='utf-8') as fp:
            schema_data = fp.read()

        with open(BASE_DIR / 'basic_sample.html', 'r', encoding='utf-8') as fp:
            sample_data = fp.read()

        prefab = PandasPrefab(schema_data)
        results = prefab.execute(sample_data)

        expected_results = pd.read_csv(BASE_DIR / 'basic_expected_results.csv')
        assert_frame_equal(expected_results, results)

    def test_list_of_dicts_prefab(self):
        with open(BASE_DIR / 'basic_schema.xml', 'r', encoding='utf-8') as fp:
            schema_data = fp.read()

        with open(BASE_DIR / 'basic_sample.html', 'r', encoding='utf-8') as fp:
            sample_data = fp.read()

        prefab = ListOfDictsPrefab(schema_data=schema_data)
        results = prefab.execute(sample_data)

        expected_results = [
            {'div_a_text': 'ab', 'span_id': 'cd', 'span_text': 'ef'},
            {'div_a_text': 'gh', 'span_id': 'ij', 'span_text': 'kl'},
            {'div_a_text': 'mn', 'span_id': 'op', 'span_text': 'qr'},
            {'div_a_text': 'st', 'span_id': 'uv', 'span_text': 'wx'},
            {'div_a_text': 'yz', 'span_id': 'ab', 'span_text': 'cd'},
        ]
        self.assertListEqual(expected_results, results)
