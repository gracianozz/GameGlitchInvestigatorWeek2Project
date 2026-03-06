import pytest
from logic_utils import check_guess, get_range_for_difficulty


class TestCheckGuessHintMessages:
    """Test suite for the hint message bug fix.
    
    Bug: Hint messages were reversed for Too High and Too Low cases.
    When a guess was lower than the secret, it would incorrectly say "go lower"
    instead of "go higher", and vice versa.
    """

    def test_guess_too_high_returns_correct_hint(self):
        """Test that guessing higher than secret returns 'Too High' with 'Go LOWER' message."""
        secret = 50
        guess = 75
        outcome, message = check_guess(guess, secret)
        
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_guess_too_low_returns_correct_hint(self):
        """Test that guessing lower than secret returns 'Too Low' with 'Go HIGHER' message."""
        secret = 50
        guess = 25
        outcome, message = check_guess(guess, secret)
        
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_guess_correct_returns_win(self):
        """Test that guessing the secret number returns 'Win' outcome."""
        secret = 50
        guess = 50
        outcome, message = check_guess(guess, secret)
        
        assert outcome == "Win"
        assert "Correct" in message

    def test_hint_messages_with_edge_values(self):
        """Test hint messages work correctly with edge case values."""
        # Test with boundary values
        secret = 1
        
        # Too high guess
        outcome, message = check_guess(100, secret)
        assert outcome == "Too High"
        assert "LOWER" in message
        
        # Too low guess
        outcome, message = check_guess(0, secret)
        assert outcome == "Too Low"
        assert "HIGHER" in message
        
        # Correct guess
        outcome, message = check_guess(1, secret)
        assert outcome == "Win"

    def test_multiple_incorrect_guesses_give_consistent_hints(self):
        """Test that multiple guesses against the same secret give consistent hints."""
        secret = 86
        
        # Bug scenario: guessing 74 (lower than 86) should say "Go HIGHER", not "Go LOWER"
        outcome1, message1 = check_guess(74, secret)
        assert outcome1 == "Too Low"
        assert "HIGHER" in message1
        
        # Guessing higher than secret
        outcome2, message2 = check_guess(95, secret)
        assert outcome2 == "Too High"
        assert "LOWER" in message2


class TestDifficultyRanges:
    """Test suite for difficulty-based number ranges.
    
    Bug: Difficulty ranges may not be correctly assigned or validated.
    This test ensures each difficulty level returns the expected range bounds.
    """

    def test_easy_difficulty_range(self):
        """Test that Easy difficulty returns range 1-20."""
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20
        # Verify range span
        assert high - low + 1 == 20, "Easy range should span exactly 20 numbers"

    def test_normal_difficulty_range(self):
        """Test that Normal difficulty returns range 1-50."""
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 50
        # Verify range span
        assert high - low + 1 == 50, "Normal range should span exactly 50 numbers"

    def test_hard_difficulty_range(self):
        """Test that Hard difficulty returns range 1-100."""
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 100
        # Verify range span
        assert high - low + 1 == 100, "Hard range should span exactly 100 numbers"

    def test_easy_boundary_values(self):
        """Test that Easy range boundaries are correct: 1-20."""
        low, high = get_range_for_difficulty("Easy")
        # Lower boundary
        assert low == 1, "Easy minimum should be 1"
        # Upper boundary
        assert high == 20, "Easy maximum should be 20"
        # Verify no values outside range
        assert low > 0, "Easy should not include 0 or negative numbers"
        assert high < 21, "Easy should not include 21 or higher"

    def test_normal_boundary_values(self):
        """Test that Normal range boundaries are correct: 1-50."""
        low, high = get_range_for_difficulty("Normal")
        # Lower boundary
        assert low == 1, "Normal minimum should be 1"
        # Upper boundary
        assert high == 50, "Normal maximum should be 50"
        # Verify range is larger than Easy
        easy_low, easy_high = get_range_for_difficulty("Easy")
        assert high > easy_high, "Normal max should exceed Easy max"

    def test_hard_boundary_values(self):
        """Test that Hard range boundaries are correct: 1-100."""
        low, high = get_range_for_difficulty("Hard")
        # Lower boundary
        assert low == 1, "Hard minimum should be 1"
        # Upper boundary
        assert high == 100, "Hard maximum should be 100"
        # Verify range is larger than Normal
        normal_low, normal_high = get_range_for_difficulty("Normal")
        assert high > normal_high, "Hard max should exceed Normal max"

    def test_invalid_difficulty_defaults_to_hard(self):
        """Test that invalid difficulty defaults to Hard range (1-100)."""
        low, high = get_range_for_difficulty("Impossible")
        assert low == 1
        assert high == 100

    def test_all_difficulties_have_same_lower_bound(self):
        """Test that all difficulty levels start at 1."""
        difficulties = ["Easy", "Normal", "Hard"]
        for difficulty in difficulties:
            low, high = get_range_for_difficulty(difficulty)
            assert low == 1, f"{difficulty} should have lower bound of 1"

    def test_difficulty_ranges_increase_progressively(self):
        """Test that ranges progressively increase: Easy < Normal < Hard."""
        easy_low, easy_high = get_range_for_difficulty("Easy")
        normal_low, normal_high = get_range_for_difficulty("Normal")
        hard_low, hard_high = get_range_for_difficulty("Hard")
        
        # All start at 1
        assert easy_low == normal_low == hard_low == 1
        
        # Upper bounds increase with difficulty
        assert easy_high == 20, "Easy should have max of 20"
        assert normal_high == 50, "Normal should have max of 50"
        assert hard_high == 100, "Hard should have max of 100"
        
        # Progressive increase
        assert easy_high < normal_high < hard_high
