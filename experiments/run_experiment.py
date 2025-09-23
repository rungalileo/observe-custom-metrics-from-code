#!/usr/bin/env python3
"""
Run an experiment using the legal advice dataset.

This script fetches the legal advice dataset and runs an experiment
to test the "Legal Advice Offered" metric.
"""

import os
from galileo.datasets import get_dataset
from galileo.experiments import run_experiment
from galileo.schema.metrics import GalileoScorers
from galileo.openai import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def simple_llm_function(input_text: str) -> str:
    """
    Simple function that takes input and returns output using OpenAI.
    Documentation: https://v2docs.galileo.ai/sdk-api/third-party-integrations/openai/openai
    
    Args:
        input_text (str): The input text to process
        
    Returns:
        str: The LLM response
    """
    # Initialize the Galileo wrapped OpenAI client
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Make the API call
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": input_text}],
        model="gpt-4o"
    )
    
    return response.choices[0].message.content

def main():
    """
    Main function to run the experiment.
    """
    # Check if required environment variables are set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY environment variable not set")
        return
    
    try:
        # Get the dataset
        dataset = get_dataset(name="legal_advice_refusal_dataset")
        print(f"Dataset loaded: {dataset.name}")
        
        # Run the experiment
        results = run_experiment(
            "legal_advice_experiment",
            dataset=dataset,
            function=simple_llm_function,
            metrics=[
                "Legal Advice Offered", # custom metric
                GalileoScorers.ground_truth_adherence
                ],
            project=os.environ.get("GALILEO_PROJECT")
        )
        print(results)
        experiment_id = results['experiment'].id
        print(f"Experiment ID: {experiment_id}")
        print(f"\nTo view results, run: python fetch_experiment.py {experiment_id}")
        
    except Exception as e:
        print(f"Error running experiment: {e}")

if __name__ == "__main__":
    main()
