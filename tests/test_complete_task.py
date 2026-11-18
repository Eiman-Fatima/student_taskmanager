import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import task_manager as tm  # noqa: E402


class TestCompleteTask(unittest.TestCase):

    def test_already_completed_task_rejected(self):
        tasks = []
        task = tm.add_task(tasks, "Study Git")
        tm.complete_task(tasks, task["id"])

        with self.assertRaises(ValueError):
            tm.complete_task(tasks, task["id"])
    def test_complete_task(self):
        tasks = []
        task = tm.add_task(tasks, "Write report")
        tm.complete_task(tasks, task["id"])
        self.assertTrue(tasks[0]["completed"])

    def test_complete_invalid_id(self):
        with self.assertRaises(ValueError):
            tm.complete_task([], 5)


if __name__ == "__main__":
    unittest.main()
