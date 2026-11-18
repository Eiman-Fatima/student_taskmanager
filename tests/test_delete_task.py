import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import task_manager as tm  # noqa: E402


class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
        tasks = []
        task = tm.add_task(tasks, "Submit lab")
        tm.delete_task(tasks, task["id"])
        self.assertEqual(tasks, [])

    def test_delete_invalid_id(self):
        with self.assertRaises(ValueError):
            tm.delete_task([], 99)


if __name__ == "__main__":
    unittest.main()
