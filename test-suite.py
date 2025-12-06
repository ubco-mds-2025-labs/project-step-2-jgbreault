import unittest
from tests.structure.TestFoundation import TestFoundation
from tests.analysis.TestTournament import TestTournament 
from tests.analysis.TestTeam import TestTeam

def test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    comment = """
    suite.addTest(TestFoundation('test_completedTournament_random'))
    suite.addTest(TestFoundation('test_completedTournament_similar'))
    suite.addTest(TestFoundation('test_completedTournament_opposite'))
    suite.addTest(TestFoundation('test_teamListFunctions'))

    suite.addTest(TestTournament('test_helper_functions'))
    suite.addTest(TestTournament('test_get_winner_probabilities'))
    
    suite.addTest(TestTeam('test_helper_functions'))
    suite.addTest(TestTeam('test_get_round_probabilities'))
    """

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

test_suite()
