#!/usr/bin/env python3
'''TestCases Class Module - utils.access_nested_map'''
import unittest
import unittest.mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    '''Testing case for `access_nested_map`'''
    @parameterized.expand([
        ({'a': 1}, ("a",), 1),
        ({'a': {"b": 1}}, ("a",), {'b': 1}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        '''Test access_nested_map'''
        self.assertEqual(access_nested_map(
            nested_map=nested_map, path=path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({'a': 1}, ("a", "b",), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_error: KeyError) -> None:
        '''Test acess_nested_map exception'''
        with self.assertRaises(expected_error):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Testing case for get_json'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(self, url: str, payload: bool,
                      mock_get: unittest.mock.Mock,) -> None:
        '''Test and mocking get_json function'''
        mock = mock_get.return_value
        mock.json.return_value = payload
        mock(url)
        result = get_json(url)
        mock.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    '''Testing case for memoize'''

    def test_memoize(self) -> None:
        class TestClass:

            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()
        with unittest.mock.patch.object(TestClass, 'a_method') as p:
            t = TestClass()
            t1 = t.a_property
            t2 = t.a_property
            p.assert_called_once()
