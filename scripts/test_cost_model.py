"""Pure domain smoke checks; no broker, configuration or credentials imported."""
import importlib.util
from pathlib import Path
import sys
import unittest
from decimal import Decimal as D

SOURCE = Path(__file__).resolve().parents[1] / 'samples/paper-risk/cost_model.py'
spec = importlib.util.spec_from_file_location('portfolio_cost_sample', SOURCE)
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)


class CostDomainChecks(unittest.TestCase):
    def estimate(self, engine, **kwargs):
        return engine.estimate_trade_cost(notional=D('10000'), quantity=D('100'), **kwargs)

    def test_basis_points_and_exact_decimal_costs(self):
        result = self.estimate(model.CostModel(model.CostModelConfig(commission_pct=D('0.001'), spread_bps=D('4'), slippage_bps=D('6'))))
        self.assertEqual(result.commission, D('10'))
        self.assertEqual(result.spread_cost, D('4'))
        self.assertEqual(result.slippage_cost, D('6'))
        self.assertEqual(result.total, D('20'))
        self.assertEqual(result.total_bps, D('20'))

    def test_sell_regulatory_fees_are_separate(self):
        engine = model.CostModel()
        buy, sell = self.estimate(engine), self.estimate(engine, is_sell=True)
        self.assertEqual(buy.regulatory_fees, D('0'))
        self.assertEqual(sell.regulatory_fees, D('0.2946000'))
        self.assertGreater(sell.total, buy.total)

    def test_slippage_stress_does_not_mutate_base(self):
        base = model.CostModel()
        stressed = base.stressed(model.StressScenario.SLIPPAGE_3X)
        self.assertEqual(self.estimate(stressed).slippage_cost, self.estimate(base).slippage_cost * 3)
        self.assertEqual(base.config.slippage_bps, D('5.0'))

    def test_zero_notional_bps_is_defined(self):
        result = model.CostModel().estimate_trade_cost(notional=D('0'), quantity=D('0'))
        self.assertEqual(result.total_bps, D('0'))


if __name__ == '__main__':
    unittest.main()
