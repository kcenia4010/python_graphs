import unittest
import python_repos

class TestCase(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(200, python_repos.r.status_code)

    def test_number_repositories(self):
        self.assertEqual(30, len(python_repos.repo_dicts))


if __name__ == '__main__':
    unittest.main()