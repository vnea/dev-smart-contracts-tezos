from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface


class CounterContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        contract_path = join(dirname(dirname(__file__)), "contracts/counter.tz")
        cls.contract = ContractInterface.create_from(contract_path)

    def test_increaseCounterBy_should_increase_counter_in_storage_by_increase_value(self):
        # Given
        increase_value = 5

        # When
        result = self.contract.increaseCounterBy(increase_value).result(storage=0)

        # Then
        self.assertEqual(result.storage, 5)

    def test_decreaseCounterBy_should_decrease_counter_in_storage_by_decrease_value(self):
        # Given
        decrease_value = 5

        # When
        result = self.contract.decreaseCounterBy(decrease_value).result(storage=0)

        # Then
        self.assertEqual(result.storage, -5)
