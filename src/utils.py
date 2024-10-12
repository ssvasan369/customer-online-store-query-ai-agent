from typing import Any, Dict
import json
import os
import yaml

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Load and parse a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        Dict[str, Any]: Parsed JSON content as a dictionary.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(base_dir, file_path)

    print(f"config_path: {config_path}")

    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {config_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file {config_path}")
        return {}
    



def load_yaml_file(file_path: str) -> Dict[str, Any]:
    """
    Load and parse a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        Dict[str, Any]: Parsed YAML content as a dictionary.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(base_dir, file_path)

    print(f"config_path: {config_path}")

    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {config_path}")
        return {}
    except yaml.YAMLError:
        print(f"Error: Invalid YAML in file {config_path}")
        return {}
    



def format_thoughts(category: str, sentiment: str) -> str:
    """
    Format the support thoughts based on the query analysis.

    Args:
        category (str): The category of the query.
        sentiment (str): The sentiment of the query.

    Returns:
        str: Formatted thoughts string.
    """
    escalated = sentiment == "Negative"
    thoughts = f"""
    - Query categorized as: {category}
    - Detected sentiment: {sentiment}
    - {"Escalated to human support due to negative sentiment" if escalated else "Handled by automated system"}
    - Response tailored to {category.lower()} category
    """
    return thoughts.strip()


def get_response_type(sentiment: str) -> str:
    """
    Determine the response type based on the sentiment.

    Args:
        sentiment (str): The sentiment of the query.

    Returns:
        str: The response type ("Escalated" or "Automated").
    """
    return "Human" if sentiment == "Negative" else "AI Agent"