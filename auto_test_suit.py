from unittest.suite import TestSuite
from submit_an_answer_test import *
from create_ticket_test import CreateTicketTest
from add_a_comment_test import AddACommentTest
from open_and_edit_account_test import OpenAndEditAccountPageTest
from submit_a_suggestion_test import GiveASuggestionTest

# Create a test loader
test_loader = unittest.TestLoader()
# Create a test suit
suite = TestSuite()

# load the tests using test loader to test suit
# suite.addTests(test_loader.loadTestsFromTestCase(SignupTest))
suite.addTests(test_loader.loadTestsFromTestCase(CreateTicketTest))
suite.addTests(test_loader.loadTestsFromTestCase(SubmitAnAnswerTestCH))
suite.addTests(test_loader.loadTestsFromTestCase(SubmitAnAnswerTestFF))
suite.addTests(test_loader.loadTestsFromTestCase(AddACommentTest))
suite.addTests(test_loader.loadTestsFromTestCase(OpenAndEditAccountPageTest))
suite.addTests(test_loader.loadTestsFromTestCase(GiveASuggestionTest))

# run the suite
runner = unittest.TextTestRunner()
runner.run(suite)