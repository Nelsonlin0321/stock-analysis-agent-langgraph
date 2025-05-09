from pydantic import BaseModel


class SymbolWithIncreasePercentage(BaseModel):
    """Top performance stock with increased percentage."""
    symbol: str
    percentage: float
