def validate_query(query):
    if not isinstance(query, str):
        raise ValueError("Query must be a string.")
    if len(query) == 0:
        raise ValueError("Query cannot be empty.")
    return query.strip()


def handle_error(error):
    print(f"An error occurred: {error}")


def run_query(query):
    try:
        validated_query = validate_query(query)
        # Assume execute_query is a function that executes the SQL query.
        result = execute_query(validated_query)
        return result
    except ValueError as ve:
        handle_error(ve)
    except Exception as e:
        handle_error(e)


# Example Usage:
# query_result = run_query("SELECT * FROM users;")
# print(query_result)