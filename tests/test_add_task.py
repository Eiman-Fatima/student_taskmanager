import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import task_manager as tm  # noqa: E402


class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = tm.add_task(tasks, "Study DevOps")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(task["title"], "Study DevOps")
        self.assertFalse(task["completed"])

    def test_add_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            tm.add_task([], "   ")
    def test_add_none_title_rejected(self):
        with self.assertRaises(ValueError):
            tm.add_task([], None)

if __name__ == "__main__":
    unittest.main()
