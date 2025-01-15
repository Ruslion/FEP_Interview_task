'''Objective 
For the get_score(game_stamps, offset) function developed in the previous task, develop unit tests using the unittest framework.
The tests should cover all possible use cases of the function, focus on testing a single case, not be repetitive, and the 
test names should reflect the essence of the checks being performed.
'''

import unittest
import task_1
import random

class Test_get_score(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Runs once before any test
        self.test_game_stamps = [{'offset': 0, 'score': {'away': 0, 'home': 0}},
                                {'offset': 3, 'score': {'away': 2, 'home': 19}},
                                {'offset': 6, 'score': {'away': 3, 'home': 18}},
                                {'offset': 8, 'score': {'away': 4, 'home': 17}},
                                {'offset': 11, 'score': {'away': 5, 'home': 16}},
                                {'offset': 13, 'score': {'away': 6, 'home': 15}},
                                {'offset': 16, 'score': {'away': 7, 'home': 14}},
                                {'offset': 19, 'score': {'away': 8, 'home': 13}},
                                {'offset': 21, 'score': {'away': 9, 'home': 12}},
                                {'offset': 24, 'score': {'away': 10, 'home': 11}},
                                {'offset': 25, 'score': {'away': 11, 'home': 10}},
                                {'offset': 26, 'score': {'away': 12, 'home': 9}},
                                {'offset': 27, 'score': {'away': 13, 'home': 8}},
                                {'offset': 29, 'score': {'away': 14, 'home': 7}},
                                {'offset': 32, 'score': {'away': 15, 'home': 6}},
                                {'offset': 34, 'score': {'away': 16, 'home': 5}},
                                {'offset': 36, 'score': {'away': 17, 'home': 4}},
                                {'offset': 38, 'score': {'away': 18, 'home': 3}},
                                {'offset': 39, 'score': {'away': 19, 'home': 2}},
                                {'offset': 42, 'score': {'away': 20, 'home': 1}},]
        

    def test_get_score_valid_home_away_scores(self):
        
        home, away = task_1.get_score(self.test_game_stamps, 3)
        self.assertEqual(home, 19)
        self.assertEqual(away, 2)
    
    def test_start_of_game(self):
        """Test score at the start of the game"""
        home, away = task_1.get_score(self.test_game_stamps, 0)
        self.assertEqual(home, 0)
        self.assertEqual(away, 0)

    def test_offset_between_stamps(self):
        """Test when offset is between two stamps"""
        # Returns from 21 offset
        home, away = task_1.get_score(self.test_game_stamps, 20)
        self.assertEqual(home, 12)
        self.assertEqual(away, 9)

        # Returns from 29 offset
        home, away = task_1.get_score(self.test_game_stamps, 28)
        self.assertEqual(home, 7)
        self.assertEqual(away, 14)
    
    def test_end_of_game(self):
        """Test score at the end of the game"""
        home, away = task_1.get_score(self.test_game_stamps, 42)
        self.assertEqual(home, 1)
        self.assertEqual(away, 20)
    
    def test_offset_out_of_range(self):
        """Test when offset is out of range"""
        with self.assertRaises(ValueError):
            task_1.get_score(self.test_game_stamps, 43)
        with self.assertRaises(ValueError):
            task_1.get_score(self.test_game_stamps, -1)

