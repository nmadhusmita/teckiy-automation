import unittest
from unittest.suite import TestSuite
from add_a_comment_test import SearchTest
from create_ticket_test import CreateTicketTest


# Create a test loader
test_loader = unittest.TestLoader()
# Create a test suit
suite = TestSuite()

# load the tests using test loader to test suit
# suite.addTests(test_loader.loadTestsFromTestCase(SignupTest))
suite.addTests(test_loader.loadTestsFromTestCase(CreateTicketTest))
suite.addTests(test_loader.loadTestsFromTestCase(SearchTest))

# run the suite
runner = unittest.TextTestRunner()
runner.run(suite)