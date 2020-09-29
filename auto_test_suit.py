from unittest.suite import TestSuite
from test.signup_test import SignupTest
from test.submit_an_answer_test import *
from test.submit_a_suggestion_test import GiveASuggestionTest
from test.add_a_comment_test import AddACommentTest
from test.edit_a_comment_test import EditACommentTest
from test.delete_a_comment_test import DeleteACommentTest
from test.create_ticket_test import CreateTicketTest
from test.edit_a_ticket_test import EditATicketTest
from test.open_and_edit_account_test import OpenAndEditAccountPageTest
from test.pagination_test import PaginationTest

# Create a test loader
test_loader = unittest.TestLoader()
# Create a test suit
suite = TestSuite()

# load the test using test loader to test suit
suite.addTests(test_loader.loadTestsFromTestCase(SignupTest))
suite.addTests(test_loader.loadTestsFromTestCase(CreateTicketTest))
suite.addTests(test_loader.loadTestsFromTestCase(SubmitAnAnswerTestCH))
suite.addTests(test_loader.loadTestsFromTestCase(EditATicketTest))
suite.addTests(test_loader.loadTestsFromTestCase(SubmitAnAnswerTestFF))
suite.addTests(test_loader.loadTestsFromTestCase(AddACommentTest))
suite.addTests(test_loader.loadTestsFromTestCase(EditACommentTest))
suite.addTests(test_loader.loadTestsFromTestCase(DeleteACommentTest))
suite.addTests(test_loader.loadTestsFromTestCase(PaginationTest))
suite.addTests(test_loader.loadTestsFromTestCase(OpenAndEditAccountPageTest))
suite.addTests(test_loader.loadTestsFromTestCase(GiveASuggestionTest))

# run the suite
runner = unittest.TextTestRunner()
runner.run(suite)