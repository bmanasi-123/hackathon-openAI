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

source1 = """PatientID,FirstName,LastName,Gender,Age,DateOfBirth,Phone,Email
101,John,Smith,Male,35,15-07-1987,(555) 123-4567,john.smith@email.com
102,Mary,Johnson,Female,28,22-03-1995,(555) 987-6543,mary.j@email.com
103,David,Williams,Male,45,10-12-1978,(555) 555-5555,david.w@email.com
104,Sarah,Brown,Female,52,05-09-1971,(555) 111-2222,sarah.b@email.com
105,Michael,Davis,Male,30,20-11-1992,(555) 333-4444,michael.d@email.com
"""

source2="""PatientID,Name,Sex,Age,DOB,Telephone,Email
101,John Smith,M,35,15/07/1987,(555) 123-4567,john.smith@email.com
102,Mary Johnson,F,28,22/03/1995,(555) 987-6543,mary.j@email.com
103,David Williams,M,45,10/12/1978,(555) 555-5555,david.w@email.com
104,Sarah Brown,F,52,05/09/1971,(555) 111-2222,sarah.b@email.com
105,Michael Davis,M,30,20/11/1992,(555) 333-4444,michael.d@email.com
"""

sample="""ID,Full Name,Gender,Age,DOB,Mobile,Email
104,Sarah Brown,Female,52,1971-09-05,555-111-2222,sarah.b@email.com
105,Michael Davis,Male,30,1992-11-20,555-333-4444,michael.d@email.com
"""


with open("source1.csv", "w") as fp:
    fp.write(source1)
source1_df = pd.read_csv("source1.csv")
print(source1_df)

# Write source2 data to source2.csv and create corresponding DataFrame
with open("source2.csv", "w") as fp:
    fp.write(source2)
source2_df = pd.read_csv("source2.csv")
print(source2_df)

# Write sample data to sample.csv and create corresponding DataFrame
with open("sample.csv", "w") as fp:
    fp.write(sample)
sample_df = pd.read_csv("sample.csv")
print(sample_df)


# template = """ 
# Transform the data in Source 1 and Source 2 to match the format of the Sample row. Here are the contents of Source 1 and Source 2:

# Source 1 - {source1_row}
# Source 2 - {source2_row}

# Please create a new row JSON object in the format of the Sample row:

# Sample - {sample_row}

# Pick the value from Source 1 or Source 2. Apply transformation so that the value changes to Sample format.
#     JSON object:"""

template = """You are an assistant to generate code. 

Lets think step by step

1. You are given three tables. Source1, Source2 and Sample.
2. Task is to generate a target table which has exactly the same number of columns as sample table and same number of rows as source1 table
3. Map source column names to sample column names based on the content
4. For each column in the sample table, identify which column matches from source1 or source2 table and find the transformation needed from source to sample table
5. Use pandas in built functions or regex and transform the column into sample table format.
6. Apply mobile transformations(xxx-xxx-xxxx) simillar to the sample table format. 
7. Always transform dates into yyyy-mm-dd format
8. Do not change the source1, source2 and sample table values. Instead, find the transformations and apply it on the target table. 
9. Do not perform merge or concat, as the tables are huge.
10. The column names in the sample table might not match exactly in the source1 and source2 table. identify the columns based on the column values.
11. Generate python code to create target table by reading source1.csv, source2.csv, sample.csv.

Few rows of Source1, Source2 and Sample tables:

Source 1 - {source1_row}
Source 2 - {source2_row}
Sample - {sample_row}
 
Python Code:
"""

OpenAI_API_KEY = "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"

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
    template=template, input_variables=["source1_row", "source2_row", "sample_row"]
)

llm = ChatOpenAI(openai_api_key=OpenAI_API_KEY, model="gpt-4")
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
source1_row = source1_df.iloc[:1].to_json()
print(source1_row)
source2_row = source2_df.iloc[:1].to_json()
print(source2_row)
sample_row = sample_df.iloc[:1].to_json()
print(sample_row)
response = llm_chain.run(
    {"source1_row": source1_row, "source2_row": source2_row, "sample_row": sample_row}
)
print(response)

