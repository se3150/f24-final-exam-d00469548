import pytest
from brute import Brute
import string, time

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")
    
    def describe_init():
        def initializes_with_correct_target(cracker):
            assert cracker.target == '00ab3eef51b8551de98a6cab9352898aed783a35995285659bbdd40162fda9505aebff62d7bf29fd7474d45f303f3cddd8d3aa0383f45a9f9facd6a8860f7938'
    
    def describe_hash():
        def hashes_to_correct_value(cracker):
            assert cracker.hash('abc123') == 'c70b5dd9ebfb6f51d09d4132b7170c9d20750a7852f00680f65658f0310e810056e6763c34c9a00b0e940076f54495c169fc2302cceb312039271c43469507dc'

    def describe_random_guess():
        def returns_strings_of_correct_length(cracker):
            for _ in range(30):
                assert 1 <= len(cracker.randomGuess()) <= 8

        def returns_strings_containing_only_letters_and_numbers(cracker):
            allowed_characters = string.ascii_letters + string.digits
            for _ in range(30):
                assert all([char in allowed_characters for char in cracker.randomGuess()])

    def describe_bruteOnce():
        def returns_true_if_attempt_matches_secret_string(cracker):
            assert cracker.bruteOnce("TDD") == True

        def returns_false_if_attempt_does_not_match_secret_string(cracker):
            assert cracker.bruteOnce("System testing") == False

    def describe_bruteMany():
        def returns_negative_1_if_all_guesses_incorrect(cracker, mocker):
            mock_randomGuess = mocker.patch.object(cracker, 'randomGuess', return_value='abc123')
            assert cracker.bruteMany(limit=30) == -1

        def returns_time_taken_if_a_guess_is_correct(cracker, mocker):
            mock_randomGuess = mocker.patch.object(cracker, 'randomGuess', return_value='TDD')
            
            time_taken = time.time()
            return_value = cracker.bruteMany(limit=30)
            time_taken = time.time() - time_taken

            assert (time_taken - .5) < return_value < (time_taken + .5)

        def attempts_until_correct_guess(cracker, mocker):
            mock_randomGuess = mocker.patch.object(cracker, 'randomGuess', return_value='TDD')
            cracker.bruteMany(limit=30)
            mock_randomGuess.assert_called_once()

            mock_bruteOnce = mocker.patch.object(cracker, 'bruteOnce', return_value=True)
            cracker.bruteMany(limit=30)
            mock_bruteOnce.assert_called_once()

        def attempts_until_guess_limit_if_all_guesses_incorrect(cracker, mocker):
            mock_randomGuess = mocker.patch.object(cracker, 'randomGuess', return_value='abc123')
            cracker.bruteMany(limit=30)
            assert mock_randomGuess.call_count == 30

            mock_bruteOnce = mocker.patch.object(cracker, 'bruteOnce', return_value=False)
            cracker.bruteMany(limit=30)
            assert mock_bruteOnce.call_count == 30
        
        
            
