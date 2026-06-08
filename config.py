from dataclasses import dataclass
import os

@dataclass
class Config:
    input_path: str
    output_path: str
    min_amount: float

def load_config() -> Config:
    return Config(
        input_path=get_required_env("INPUT_PATH"),
        output_path=get_required_env("OUTPUT_PATH"),
        min_amount=float(os.getenv("MIN_AMOUNT", "0"))
    )

def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value
