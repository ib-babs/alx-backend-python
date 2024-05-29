#!/usr/bin/env python3
'''TestCases Class Module - utils.access_nested_map'''
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Mapping, Sequence, Union
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''Testing GithubOrgClient class'''

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json', return_value={'login': 'success'})
    def test_org(self, org_name: str, mocked: MagicMock) -> None:
        '''Test org with params provided'''
        client_sig = GithubOrgClient(org_name=org_name)
        result = client_sig.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mocked.method.get_json(expected_url)

        mocked.method.get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {'login': 'success'})

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos_url(self, mock_get_json: MagicMock) -> None:
        '''Test public_repos_url'''
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/mock_org/repos"
            mock_public_repos_url.return_value = url

            client = GithubOrgClient("mock_org")
            result = client.public_repos()
            expected_repos = ["repo1", "repo2"]
            # Assertions
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()
            self.assertEqual(result, expected_repos)

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        '''Test public_repos'''
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/mock_org/repos"
            mock_public_repos_url.return_value = url

            client = GithubOrgClient("mock_org")
            result = client.public_repos()
            expected_repos = ["repo1", "repo2"]
            # Assertions
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()
            self.assertEqual(result, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),

    ])
    def test_has_license(self, repo: Mapping, license: str,
                         expected_output: bool) -> None:
        '''Testing GithubOrgClient method - has_license'''
        self.assertEqual(GithubOrgClient.has_license(
            repo, license), expected_output)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    ''' test the GithubOrgClient.public_repos method in an integration test.
    Meaning:  only mock code that sends external requests.'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @staticmethod
    def get_json_url(cls, url=None) -> Union[Mapping, Sequence, str]:
        if url is None:
            return None
        if url == "https://api.github.com/orgs/google":
            cls.mock_get.return_value.json.side_effect = cls.org_payload
        if url == 'https://api.github.com/orgs/google/repos':
            cls.mock_get.return_value.json.side_effect = cls.repos_payload
        return cls.mock_get.return_value.json.side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mock_get.stop()

    def test_public_repos(self) -> None:
        '''Test public_repos'''
        self.mock_get("https://api.github.com/orgs/google")
        self.mock_get(
            "https://api.github.com/orgs/google/repos")
        self.mock_get.assert_any_call(
            "https://api.github.com/orgs/google")
        self.mock_get.assert_any_call(
            "https://api.github.com/orgs/google/repos")

    def test_public_repos_with_license(self) -> None:
        '''Test public_repos with license'''
        self.mock_get.method.get_json("https://api.github.com/orgs/google")
        self.mock_get.method.get_json(
            "https://api.github.com/orgs/google/repos")
