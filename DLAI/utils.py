#!/bin/env python

# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# these expect to find a .env file at the directory above the lesson.                                                                        # the format for that file is (without the comment)                                                                                          #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                         
# Function to load environment variables from a specified .env file
def load_env(env_path):
    load_dotenv(env_path)

# Function to get the OpenAI API key
def get_openai_api_key(env_path):
    load_env(env_path)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key
    
# Specify the path to your test.env file
env_path = './test.env'

# Load environment variables
load_env(env_path)

# Get the API key to ensure it is set
api_key = get_openai_api_key(env_path)
if not api_key:
    raise ValueError("OpenAI API key not found. Ensure it is set in the test.env file.")

# Configuration for the ConversableAgent
llm_config = {
    "api_key": api_key,
    # Add other configurations as needed
}

# def load_env():
#     _ = load_dotenv(find_dotenv())

# def get_openai_api_key():
#     load_env()
#     openai_api_key = os.getenv("OPENAI_API_KEY")
#     return openai_api_key

# load_dotenv()

# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )