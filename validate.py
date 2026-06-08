class InvalidSchemaError(Exception):
    pass

def validate_required_columns(df, required_columns):
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise InvalidSchemaError(f"Missing required columns: {missing}")
