from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface, MichelsonRuntimeError


class CounterContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        contract_path = join(dirname(dirname(__file__)), "contracts/counter_with_check.tz")
        cls.contract = ContractInterface.create_from(contract_path)

    def test_increaseCounterBy_should_increase_counter_in_storage_by_increase_value(self):
        # Given
        increase_value = 5

        # When
        result = self.contract.increaseCounterBy(increase_value).result(storage=0)

        # Then
        self.assertEqual(result.storage, 5)

    def test_increaseCounterBy_negative_value_should_throw_exception(self):
        try:
            # Given
            increase_value = -1

            # When
            self.contract.increaseCounterBy(increase_value).result(storage=0)
        except MichelsonRuntimeError as e:
            # Then
            return self.assertTrue("value should be > 0" in str(e))

        self.fail("This fail should not happen.")

    def test_decreaseCounterBy_should_decrease_counter_in_storage_by_decrease_value(self):
        # Given
        decrease_value = 5

        # When
        result = self.contract.decreaseCounterBy(decrease_value).result(storage=0)

        # Then
        self.assertEqual(result.storage, -5)
