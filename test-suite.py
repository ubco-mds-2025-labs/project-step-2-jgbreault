import unittest
from tests.structure.test_foundation import test_foundation
from tests.analysis.test_tournament import test_tournament as TestTournamentAnalysis
from tests.analysis.test_team import test_team as TestTeamAnalysis
from tests.visualization.test_tournament import test_tournament as TestTournamentViz
from tests.visualization.test_analysis import test_analysis as TestAnalysisViz

def test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    suite.addTest(test_foundation('test_completedTournament_random'))
    suite.addTest(test_foundation('test_completedTournament_similar'))
    suite.addTest(test_foundation('test_completedTournament_opposite'))
    suite.addTest(test_foundation('test_teamListFunctions'))

    suite.addTest(TestTournamentAnalysis('test_helper_functions'))
    suite.addTest(TestTournamentAnalysis('test_get_winner_probabilities'))
    
    suite.addTest(TestTeamAnalysis('test_helper_functions'))
    suite.addTest(TestTeamAnalysis('test_get_round_probabilities'))
    
    suite.addTest(TestTournamentViz('test_add_round_edges'))
    suite.addTest(TestTournamentViz('test_append_edge'))
    suite.addTest(TestTournamentViz('test_get_new_file_name'))
    
    suite.addTest(TestAnalysisViz('test_plot_pie_tournament'))
    suite.addTest(TestAnalysisViz('test_plot_pie_team'))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

test_suite()
