import unittest
from unittest.mock import patch, call

import solution


class TraderTestCase(unittest.TestCase):
    def test_wallet_does_not_change_if_waiting_using_w_or_wait_or_empty(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'wait']
            solution.main([5, 5,])

    def test_wallet_buying_using_buy(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'w', 'buy', '', '']
            solution.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 60.0 PLN!')

    def test_wallet_buying_using_b(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['', '', 'b', '', '']
            solution.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 60.0 PLN!')

    def test_wallet_selling_using_sell(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'w', 's', 'sell', '']
            solution.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 100.0 PLN!')

    def test_wallet_selling_using_s(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'w', 'b', 's', '']
            solution.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 40.0 PLN!')

    def test_asking_again_for_correct_command(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'w', 'Počkejte', 'w', 'b', 's']
            solution.main([2, 2, 2, 4, 8])
        prt.assert_has_calls(
            [call('Balance: 100.0 PLN, $0.0, rate 2'),
             call('Balance: 100.0 PLN, $0.0, rate 2'),
             call('Balance: 100.0 PLN, $0.0, rate 2'),
             call('Invalid choice: Počkejte'),
             call('Balance: 100.0 PLN, $0.0, rate 4'),
             call('Balance: 0 PLN, $25.0, rate 8'),
             call('Your result: 200.0 PLN!')],
            any_order=True
        )

    def test_selling_with_no_usd_does_not_change_wallet(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'w', 's', 's', '']
            solution.main([2, 3, 4, 5, 6])
        prt.assert_called_with('Your result: 100.0 PLN!')

    def test_buying_with_no_pln_does_not_change_wallet(self):
        with patch('solution.input') as inp, patch('solution.print') as prt:
            inp.side_effect = ['w', 'b', 'b', 'b', 's']
            solution.main([3, 4, 5, 6, 7])
        prt.assert_called_with('Your result: 175.0 PLN!')
