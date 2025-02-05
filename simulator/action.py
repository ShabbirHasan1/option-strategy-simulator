from dataclasses import dataclass
from typing import Literal, Optional

import pandas as pd
from simulator.position import OptionPosition


@dataclass
class SimulationAction:
    step: int
    timestamp: pd.Timestamp
    spot: float
    type: Literal["buy", "sell", "expiration", "liquidation"]
    description: Optional[str] = None
    position: Optional[OptionPosition] = None
    liquidity_change: Optional[float] = None
