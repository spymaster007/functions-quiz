import unittest
import quiz


class HasTeen(unittest.TestCase):

	def test_for_no_teens(self):
		self.assertFalse(quiz.has_teen(11, 20, 12))

	def test_for_one_teen(self):
		self.assertTrue(quiz.has_teen(19, 1, 4))
		self.assertTrue(quiz.has_teen(9, 14, 4))
		self.assertTrue(quiz.has_teen(9, 1, 13))

	def test_for_two_teens(self):
		self.assertTrue(quiz.has_teen(19, 13, 4))
		self.assertTrue(quiz.has_teen(9, 16, 13))
		self.assertTrue(quiz.has_teen(19, 1, 18))

	def test_for_all_teens(self):
		self.assertTrue(quiz.has_teen(19, 13, 14))


class NotString(unittest.TestCase):

	def test_adds_a_not(self):
		self.assertEqual(quiz.not_string('word'), 'notword')

	def test_adds_to_end_when_there(self):
		self.assertEqual(quiz.not_string('notword'), 'notwordnot')

	def test_empty(self):
		self.assertEqual(quiz.not_string(''), 'not')


class IcyHot(unittest.TestCase):

	def test_both_icy(self):
		self.assertFalse(quiz.icy_hot(-1, -2))

	def test_both_hot(self):
		self.assertFalse(quiz.icy_hot(101, 110))

	def test_icy_and_hot(self):
		self.assertTrue(quiz.icy_hot(-1, 104))

	def test_hot_and_icy(self):
		self.assertTrue(quiz.icy_hot(101, -4))

	def test_icy_and_middle(self):
		self.assertFalse(quiz.icy_hot(-1, 0))

	def test_hot_and_middle(self):
		self.assertFalse(quiz.icy_hot(101, 100))

	def test_both_middle(self):
		self.assertFalse(quiz.icy_hot(0, 100))


class CloserTo(unittest.TestCase):

	def test_a_closer(self):
		self.assertEqual(quiz.closer_to(10, 11, 12), 11)

	def test_b_closer(self):
		self.assertEqual(quiz.closer_to(10, 12, 11), 11)

	def test_equidistant(self):
		self.assertEqual(quiz.closer_to(10, 11, 11), 0)

	def test_lower(self):
		self.assertEqual(quiz.closer_to(10, 8, 7), 8)


class TwoAsOne(unittest.TestCase):

	def test_ab_is_c(self):
		self.assertTrue(quiz.two_as_one(1, 2, 3))

	def test_bc_is_a(self):
		self.assertTrue(quiz.two_as_one(5, 2, 3))

	def test_ac_is_b(self):
		self.assertTrue(quiz.two_as_one(1, 4, 3))

	def test_no_equals(self):
		self.assertFalse(quiz.two_as_one(1, 2, 4))

	def test_same(self):
		self.assertFalse(quiz.two_as_one(1, 1, 1))


if __name__ == '__main__':
	tests = [HasTeen, NotString, IcyHot, CloserTo, TwoAsOne]
	loader = unittest.TestLoader()
	suites = map(lambda x: loader.loadTestsFromTestCase(x), tests)
	unittest.TextTestRunner().run(unittest.TestSuite(suites))