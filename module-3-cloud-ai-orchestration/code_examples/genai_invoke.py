"""
genai-invoke.py

Purpose: Invoke a GenAI response using LangChain and AWS Lambda.
Author: Ganesan Perumal
Legacy Note: This script is part of Module 3 – Cloud-AI Orchestration.
"""

# 🧭 Imports (Updated for LangChain 0.1+)
import boto3
import json
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# 🧵 Reproducibility Fingerprint
# Python 3.10+
# Dependencies: langchain==0.1.13, langchain-openai==0.3.33, boto3==1.34.0
# Invocation pattern: local → Lambda → GenAI response

# 🔐 AWS Setup
lambda_client = boto3.client('lambda', region_name='us-east-1')

# 🧠 LangChain Setup
prompt = PromptTemplate.from_template(
    "You are a helpful insurance assistant. Answer clearly:\n{question}"
)
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)
chain = prompt | llm

# 🚀 Invocation Function
def invoke_genai(question):
    # Step 1: Generate response using LangChain
    response = chain.invoke({"question": question})

    # Step 2: Package payload for Lambda
    payload = {
        "question": question,
        "response": response
    }

    # Step 3: Invoke Lambda function
    lambda_response = lambda_client.invoke(
        FunctionName='genaiResponder',
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )

    # Step 4: Parse Lambda response
    result = json.load(lambda_response['Payload'])
    return result

# 🧪 Sample Invocation
if __name__ == "__main__":
    question = "What coverage options are available for rental cars?"
    result = invoke_genai(question)
    print("GenAI Response:", result)