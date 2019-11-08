from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface


class CounterContractTest(TestCase):
    UNDEFINED = -999

    @classmethod
    def setUpClass(cls):
        contract_path = join(dirname(dirname(__file__)), "contracts/counter_with_previous_counter.tz")
        cls.contract = ContractInterface.create_from(contract_path)

    def test_increaseCounterBy_should_update_previous_counter_with_initial_counter(self):
        # Given
        increase_value = 5
        initial_counter = 10

        # When
        result = self.contract.increaseCounterBy(increase_value).result(
            storage={"counter": initial_counter, "previousCounter": self.UNDEFINED})

        # Then
        self.assertEqual(result.storage["previousCounter"], initial_counter)

    def test_increaseCounterBy_should_increase_counter_in_storage_by_increase_value(self):
        # Given
        increase_value = 5
        initial_counter = 10

        # When
        result = self.contract.increaseCounterBy(increase_value).result(
            storage={"counter": initial_counter, "previousCounter": self.UNDEFINED})

        # Then
        self.assertEqual(result.storage["counter"], 15)

    def test_decreaseCounterBy_should_update_previous_counter_with_initial_counter(self):
        # Given
        decrease_value = 5
        initial_counter = 10

        # When
        result = self.contract.decreaseCounterBy(decrease_value).result(
            storage={"counter": initial_counter, "previousCounter": self.UNDEFINED})

        # Then
        self.assertEqual(result.storage["previousCounter"], initial_counter)

    def test_decreaseCounterBy_should_decrease_counter_in_storage_by_decrease_value(self):
        # Given
        decrease_value = 5
        initial_counter = 10

        # When
        result = self.contract.decreaseCounterBy(decrease_value).result(
            storage={"counter": initial_counter, "previousCounter": self.UNDEFINED})

        # Then
        self.assertEqual(result.storage["counter"], 5)
