import unittest
from unittest.mock import patch
from main import LearningTool, QuestionsMode, DisableEnableMode, PracticeMode, TestMode


class TestLearningTool(unittest.TestCase):
    #Checks if program quits when "quit" inputted.
    @patch('builtins.input', side_effect=['quit'])
    def test_start_up_quit(self, mock_input):
        tool = LearningTool()
        with self.assertRaises(SystemExit):
            tool.main()

    #Checks if loop stops iterating once "add" is inputted.
    @patch('builtins.input', side_effect=['add'])
    @patch('time.sleep', return_value=None)
    def test_start_up_add(self, mock_sleep, mock_input):
        tool = LearningTool()
        with self.assertRaises(StopIteration):
            tool.main()


#Checks if function returns 0 when questions.csv has no questions.
class TestQuestionsMode(unittest.TestCase):
    def test_get_last_question_id(self):
        mode = QuestionsMode()
        last_id = mode.get_last_question_id()
        self.assertEqual(last_id, 0)

@patch('builtins.input', side_effect=["done"])
class TestDisableEnableMode(unittest.TestCase):
    def setUp(self):
        self.disable_enable_mode = DisableEnableMode()

    def test_select(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.disable_enable_mode.select()
            mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
