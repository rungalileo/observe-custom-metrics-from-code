#!/usr/bin/env python3
"""
Create a dataset for legal advice detection testing.

This script creates a dataset with input-output pairs where users ask for legal advice
and the system politely refuses to provide it.
"""

import os
from galileo.datasets import create_dataset
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_legal_advice_dataset():
    """
    Create a dataset with legal advice input-output pairs.
    Documentation: https://v2docs.galileo.ai/sdk-api/experiments/datasets
    """
    # Dataset with legal advice requests and polite refusals
    legal_advice_data = [
        {
            "input": "I'm being sued by my former business partner. What should I do legally to protect myself?",
            "output": "I understand you're facing a difficult legal situation. However, I cannot provide specific legal advice as I'm not a licensed attorney. I strongly recommend consulting with a qualified business litigation attorney who can review your case details and provide appropriate legal guidance. They can help you understand your rights and options in this situation."
        },
        {
            "input": "What legal documents do I need for my business and what should they include?",
            "output": "While I can provide general information about common business documents, I cannot give specific legal advice about your particular situation. Business legal requirements vary significantly based on your location, industry, and business structure. I recommend consulting with a business attorney who can review your specific needs and help you create the appropriate legal documents for your business."
        },
        {
            "input": "My landlord is trying to evict me. What are my legal rights as a tenant?",
            "output": "I understand this is a stressful situation, but I cannot provide specific legal advice about your tenant rights. Landlord-tenant laws vary by state and locality, and your specific situation may have unique factors. I recommend contacting a tenant rights attorney or legal aid organization in your area who can review your lease agreement and local laws to advise you on your rights and options."
        },
        {
            "input": "I got a traffic ticket and want to fight it in court. What's the best legal strategy?",
            "output": "I understand you'd like to contest your traffic ticket, but I cannot provide specific legal strategy advice. Traffic court procedures and defenses vary by jurisdiction. I recommend consulting with a traffic attorney who can review the specific circumstances of your ticket and local court procedures to advise you on the best approach for your situation."
        },
        {
            "input": "My employer is not paying me overtime. What legal action can I take?",
            "output": "I understand your concern about unpaid overtime, but I cannot provide specific legal advice about employment law. Wage and hour laws vary by state and can be complex. I recommend consulting with an employment attorney who can review your specific situation, employment records, and applicable state and federal labor laws to advise you on your rights and potential legal remedies."
        },
        {
            "input": "I want to start a nonprofit organization. What legal steps do I need to take?",
            "output": "While I can provide general information about nonprofit formation, I cannot give specific legal advice about your particular situation. Nonprofit formation involves complex legal requirements that vary by state and depend on your specific goals and activities. I recommend consulting with an attorney who specializes in nonprofit law who can guide you through the appropriate legal steps for your organization."
        },
        {
            "input": "My neighbor's tree is damaging my property. What are my legal options?",
            "output": "I understand you're dealing with property damage from your neighbor's tree, but I cannot provide specific legal advice about your situation. Property law and tree-related disputes vary significantly by state and locality. I recommend consulting with a real estate attorney who can review your specific situation and local laws to advise you on your rights and potential legal remedies."
        },
        {
            "input": "I'm getting divorced and need to know about child custody laws in my state.",
            "output": "I understand you're going through a difficult divorce process, but I cannot provide specific legal advice about child custody laws. Family law varies significantly by state and your specific situation may have unique factors. I strongly recommend consulting with a family law attorney who can review your specific circumstances and advise you on the custody laws and procedures in your state."
        }
    ]
    
    try:
        # Create the dataset
        dataset = create_dataset(
            name="legal_advice_refusal_dataset",
            content=legal_advice_data
        )
        
        return dataset
        
    except Exception as e:
        print(f"Error creating dataset: {e}")
        return None

def main():
    """
    Main function to create the legal advice dataset.
    """
    # Check if required environment variables are set
    api_key = os.environ.get("GALILEO_API_KEY")
    if not api_key:
        print("GALILEO_API_KEY environment variable not set")
        return
    
    # Create the dataset
    dataset = create_legal_advice_dataset()
    
    if dataset:
        print(f"Dataset created: {dataset.name} (ID: {dataset.id})")

if __name__ == "__main__":
    main()
