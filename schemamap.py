import json
import os
from argparse import ArgumentParser

import pandas as pd
from langchain.prompts import PromptTemplate  
from langchain.chains import LLMChain
# from langchain.callbacks import wandb_tracing_enabled
from langchain_community.callbacks import wandb_tracing_enabled
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI

source_df = pd.read_csv("dumbscmap.csv")
print(source_df)


sample_df = pd.read_csv("sample1.csv")
print(sample_df)


# template = """ 
# Transform the data in Source to match the format of the Sample row. Here are the contents of Source 1 and Source 2:

# Source  - {source_row}


# Please create a new row JSON object in the format of the Sample row:

# Sample - {sample_row}

# Pick the value from Source . Apply transformation so that the value changes to Sample format.
#     JSON object:"""

template = """You are an assistant to generate code. 

Lets think step by step

1. You are given two tables. Source and  Sample.
2. Task is to generate a target table which has exactly the same number of columns as sample table and same number of rows as source table
3. Map source column names to sample column names based on the content
4. For each column in the sample table, identify which column matches from source table and find the transformation needed from source to sample table
5. Use pandas in built functions or regex and transform the column into sample table format.
6. Apply mobile transformations(xxx-xxx-xxxx) simillar to the sample table format. 
7. Always transform dates into format of sample table
8. Do not change the source,sample table values. Instead, find the transformations and apply it on the target table. 
9. Do not perform merge or concat, as the tables are huge.
10. The column names in the sample table might not match exactly in the source table. identify the columns based on the column values.
11. when ever not getting any row value in source table make it as null 
12. Generate python code to create target table by reading source.csv, sample.csv.

Few rows of Source and Sample tables:

Source - {source_row}
Sample - {sample_row}
 
Python Code:
"""

OpenAI_API_KEY = "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"
prompt = PromptTemplate(
    template= template ,  input_variables=["source_row", "sample_row"]
)

llm = ChatOpenAI(openai_api_key=OpenAI_API_KEY, model="gpt-3.5-turbo")
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

# openai_result_list = []
# for i in range(len(source1_df)):
#     source1_row = source1_df.iloc[i].to_json()
#     print(source1_row)
#     source2_row = source2_df.iloc[i].to_json()
#     sample_row = sample_df.iloc[-1].to_json()
#     response = llm_chain.run(
#         {"source1_row": source1_row, "source2_row": source2_row, "sample_row": sample_row, "sample_columns": sample_df.columns}
#     )
#     target_row_dict = json.loads(response)
#     openai_result_list.append(target_row_dict)

# target_df = pd.DataFrame(openai_result_list)
# print(target_df)

prompt = PromptTemplate(
    template=template, input_variables=["source_row" , "sample_row"]
)

llm = ChatOpenAI(openai_api_key=OpenAI_API_KEY, model="gpt-4")
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
source_row = source_df.iloc[:10].to_json()
sample_row = sample_df.iloc[:10].to_json()
print(sample_row)
response = llm_chain.run(
    {"source_row": source_row ,  "sample_row": sample_row}
)
print(response)

