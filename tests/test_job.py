import unittest

from tesk_core.job import Job


class JobTestCase(unittest.TestCase):
    def test_job(self):
        job = Job({'metadata': {'name': 'test'}})
        self.assertEqual(job.name, 'task-job')
        self.assertEqual(job.namespace, 'default')


if __name__ == '__main__':
    unittest.main()
