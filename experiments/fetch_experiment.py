#!/usr/bin/env python3
"""
Fetch experiment traces with detailed metric information by experiment ID.

This script fetches and displays comprehensive trace-level metrics for an experiment from Galileo API.
It uses the traces search endpoint to find traces, then fetches detailed trace information
showing custom metrics, explanations, rationales, and other metric details at the trace level.
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_experiment_traces(experiment_id: str, project_id: str = None, limit: int = 100) -> dict:
    """
    Fetch traces for an experiment from Galileo API using the search endpoint.
    Documentation: https://v2docs.galileo.ai/api-reference/trace/query-traces
    
    Args:
        experiment_id (str): The experiment ID
        project_id (str, optional): The project ID. If not provided, uses GALILEO_PROJECT_ID env var
        limit (int): Maximum number of traces to return (default: 100)
        
    Returns:
        dict: Traces search results
    """
    if project_id is None:
        project_id = os.environ.get("GALILEO_PROJECT_ID")
        if not project_id:
            raise ValueError("GALILEO_PROJECT_ID environment variable is required")
    
    api_key = os.environ.get("GALILEO_API_KEY")
    api_url = os.environ.get("GALILEO_API_URL")
    
    if not api_key or not api_url:
        raise ValueError("GALILEO_API_KEY and GALILEO_API_URL environment variables are required")
    
    # Construct API URL for traces search
    url = f"{api_url}/v2/projects/{project_id}/traces/search"
    headers = {"Galileo-API-Key": api_key, "Content-Type": "application/json"}
    
    # Request payload for searching traces by experiment_id
    payload = {
        "experiment_id": experiment_id,
        "limit": limit,
        "starting_token": 0,
        "sort": {
            "column_id": "created_at",
            "ascending": False,
            "sort_type": "column"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching experiment traces: {e}")
        return {}


def print_traces_summary(traces_data: dict) -> None:
    """
    Print a formatted summary of trace results using search API data.
    
    Shows trace-level metrics from the search results including custom metrics,
    explanations, rationales, costs, and model information. Focuses on the first 5 traces.
    
    Args:
        traces_data (dict): Traces data from search API
    """
    print("\n" + "="*60)
    print("EXPERIMENT TRACES WITH METRIC INFO")
    print("="*60)
    
    # Basic info
    num_records = traces_data.get('num_records', 0)
    records = traces_data.get('records', [])
    
    print(f"\nTotal Traces Found: {num_records}")
    print(f"Records Returned: {len(records)}")
    
    if not records:
        print("\nNo traces found for this experiment.")
        return
    
    # Process each trace from search results
    for i, trace_record in enumerate(records):  # Limit to first 5 traces
        trace_id = trace_record.get('id')
        if not trace_id:
            continue
            
        print(f"\n{'='*50}")
        print(f"TRACE {i+1}: {trace_id}")
        print(f"{'='*50}")
        
        # Show basic trace info from search results
        print(f"  Created: {trace_record.get('created_at', 'N/A')}")
        print(f"  Name: {trace_record.get('name', 'N/A')}")
        print(f"  Complete: {trace_record.get('is_complete', 'N/A')}")
        
        # Show input and output
        input_data = trace_record.get('input', '')
        if input_data:
            print(f"  Input: {input_data}")
        
        output_data = trace_record.get('output', '')
        if output_data:
            print(f"  Output: {output_data}")
        
        # Show metric scores only
        metric_data = trace_record.get('metrics', {})
        if metric_data:
            print("\n")
            print(f"Metric Data:")
            for metric_name, metric_value in metric_data.items():
                # Only show the main metric values, not the detailed breakdowns
                if not any(suffix in metric_name for suffix in ['_num_judges', '_metric_cost', '_explanation', '_status', '_rationale', '_model_alias']):
                    print(f"{metric_name}: {metric_value}")
    

def main():
    """
    Main function to fetch experiment traces with detailed metric information.
    
    Fetches traces for an experiment and displays comprehensive metric details
    including custom metrics, explanations, rationales, and other metadata.
    """
    import sys
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python fetch_experiment.py <experiment_id> [limit]")
        print("  experiment_id: The experiment ID to fetch traces for")
        print("  limit: Maximum number of traces to return (default: 100)")
        sys.exit(1)
    
    experiment_id = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) == 3 else 100
    
    # Check if required environment variables are set
    api_key = os.environ.get("GALILEO_API_KEY")
    if not api_key:
        print("GALILEO_API_KEY environment variable not set")
        return
    
    try:
        # Fetch experiment traces
        traces_data = fetch_experiment_traces(experiment_id, limit=limit)
        if traces_data:
            print_traces_summary(traces_data)
        else:
            print("No traces data found")
            
    except Exception as e:
        print(f"Error fetching experiment traces: {e}")

if __name__ == "__main__":
    main()
