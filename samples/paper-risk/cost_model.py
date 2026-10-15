from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class StressScenario(str, Enum):
    BASE = "base"
    FEE_1_5X = "fee_1_5x"
    FEE_2X = "fee_2x"
    SLIPPAGE_2X = "slippage_2x"
    SLIPPAGE_3X = "slippage_3x"
    SPREAD_2X = "spread_2x"
    LOW_LIQUIDITY = "low_liquidity"
    DELAYED_FILL = "delayed_fill"
    PARTIAL_FILL = "partial_fill"
    GAP_AGAINST_POSITION = "gap_against_position"
    NEWS_SHOCK = "news_shock"


@dataclass(frozen=True)
class CostModelConfig:
    commission_pct: Decimal = Decimal("0.0000")
    sec_fee_pct: Decimal = Decimal("0.0000278")
    taf_fee_per_share: Decimal = Decimal("0.000166")
    spread_bps: Decimal = Decimal("2.0")
    slippage_bps: Decimal = Decimal("5.0")
    fx_cost_pct: Decimal = Decimal("0.0000")
    partial_fill_penalty_pct: Decimal = Decimal("0.0000")
    market_impact_bps: Decimal = Decimal("0.0")


@dataclass(frozen=True)
class TradeCostEstimate:
    commission: Decimal
    regulatory_fees: Decimal
    spread_cost: Decimal
    slippage_cost: Decimal
    fx_cost: Decimal
    partial_fill_penalty: Decimal
    market_impact_cost: Decimal

    @property
    def total(self) -> Decimal:
        return (
            self.commission
            + self.regulatory_fees
            + self.spread_cost
            + self.slippage_cost
            + self.fx_cost
            + self.partial_fill_penalty
            + self.market_impact_cost
        )

    @property
    def total_bps(self) -> Decimal:
        if self._notional <= 0:
            return Decimal("0")
        return self.total / self._notional * Decimal("10000")

    @property
    def _notional(self) -> Decimal:
        return getattr(self, "__notional")


class CostModel:
    def __init__(self, config: CostModelConfig | None = None) -> None:
        self.config = config or CostModelConfig()

    def estimate_trade_cost(
        self,
        *,
        notional: Decimal,
        quantity: Decimal,
        is_sell: bool = False,
    ) -> TradeCostEstimate:
        cfg = self.config
        commission = notional * cfg.commission_pct
        regulatory = notional * cfg.sec_fee_pct if is_sell else Decimal("0")
        regulatory += abs(quantity) * cfg.taf_fee_per_share if is_sell else Decimal("0")
        spread = notional * cfg.spread_bps / Decimal("10000")
        slippage = notional * cfg.slippage_bps / Decimal("10000")
        fx_cost = notional * cfg.fx_cost_pct
        partial = notional * cfg.partial_fill_penalty_pct
        impact = notional * cfg.market_impact_bps / Decimal("10000")
        estimate = TradeCostEstimate(
            commission=commission,
            regulatory_fees=regulatory,
            spread_cost=spread,
            slippage_cost=slippage,
            fx_cost=fx_cost,
            partial_fill_penalty=partial,
            market_impact_cost=impact,
        )
        object.__setattr__(estimate, "__notional", notional)
        return estimate

    def stressed(self, scenario: StressScenario | str) -> "CostModel":
        scenario = StressScenario(scenario)
        cfg = self.config
        if scenario == StressScenario.BASE:
            return CostModel(cfg)
        multiplier = {
            StressScenario.FEE_1_5X: {"commission": Decimal("1.5"), "sec": Decimal("1.5")},
            StressScenario.FEE_2X: {"commission": Decimal("2"), "sec": Decimal("2")},
            StressScenario.SLIPPAGE_2X: {"slippage": Decimal("2")},
            StressScenario.SLIPPAGE_3X: {"slippage": Decimal("3")},
            StressScenario.SPREAD_2X: {"spread": Decimal("2")},
            StressScenario.LOW_LIQUIDITY: {"spread": Decimal("2"), "slippage": Decimal("2"), "partial": Decimal("0.001")},
            StressScenario.DELAYED_FILL: {"slippage": Decimal("2")},
            StressScenario.PARTIAL_FILL: {"partial": Decimal("0.0015")},
            StressScenario.GAP_AGAINST_POSITION: {"slippage": Decimal("4")},
            StressScenario.NEWS_SHOCK: {"spread": Decimal("3"), "slippage": Decimal("5")},
        }[scenario]
        return CostModel(
            CostModelConfig(
                commission_pct=cfg.commission_pct * multiplier.get("commission", Decimal("1")),
                sec_fee_pct=cfg.sec_fee_pct * multiplier.get("sec", Decimal("1")),
                taf_fee_per_share=cfg.taf_fee_per_share * multiplier.get("sec", Decimal("1")),
                spread_bps=cfg.spread_bps * multiplier.get("spread", Decimal("1")),
                slippage_bps=cfg.slippage_bps * multiplier.get("slippage", Decimal("1")),
                fx_cost_pct=cfg.fx_cost_pct,
                partial_fill_penalty_pct=cfg.partial_fill_penalty_pct
                + multiplier.get("partial", Decimal("0")),
                market_impact_bps=cfg.market_impact_bps,
            )
        )
