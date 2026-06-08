import logging
from .config import load_config
from .extract import extract_sales
from .transform import transform_sales
from .validate import validate_required_columns
from .load import load_sales

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run():
    config = load_config()

    logger.info("Starting job")

    df = extract_sales(config.input_path)
    validate_required_columns(df, ["date", "amount"])
    df = transform_sales(df)
    load_sales(df, config.output_path)

    logger.info("Job completed successfully")

def main():
    run()

if __name__ == "__main__":
    main()
