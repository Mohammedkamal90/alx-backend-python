#!/usr/bin/env python3
"""unittests & Integrated tests"""

# test_client.py

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        expected_result = {"org": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    @patch.object(GithubOrgClient, 'org')
    def test_public_repos_url(self, mock_org):
        org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = org_payload

        client = GithubOrgClient('google')
        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient('google')
        result = client.public_repos()

        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo_payload, license_key, expected_result):
        client = GithubOrgClient('google')
        result = client.has_license(repo_payload, license_key)

        self.assertEqual(result, expected_result)

class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    @parameterized.expand([
        ('org_payload',),
        ('repos_payload',),
        ('expected_repos',),
        ('apache2_repos',)
    ])
    def test_integration(self, fixture_name):
        with open(f'fixtures/{fixture_name}.json', 'r') as f:
            fixture_data = f.read()
            self.mock_get.return_value.json.return_value = fixture_data

        # Perform integration testing here

if __name__ == '__main__':
    unittest.main()
