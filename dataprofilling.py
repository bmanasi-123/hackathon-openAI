import openai

# Set your OpenAI API key
openai.api_key = "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"

# Provide the template prompt
template = """
You are an assistant to generate code. 
Lets think step by step

Important: for all the analysis you need to use pandasAI only

0. You have a table to profiling the data
1. What is the number of rows of the table? 
2. What are the column names and their data types?
3. Give me a few lines of my table.
4. Get the count of null values and the count of empty row values.
5. When you get the data types, based on that:
    -- If the data is numeric, find the max and min.
    -- If the data can be plotted, please plot a graph.
    -- If the row data of a particular column  has repeated unique values, count the values for each unique value.
6. Do not change the table values. Instead, try to make a summary of the data analysis you did so far in this particular table.
7. The summary should be of 5 lines, not more than that.
8. Generate Python code for this:
    -- You need to write different prompts for different data analysis.
    Here is one example:
    pandas_ai.run(df, prompt="Which products are in Product line?")
You can read the CSV file from sample1.csv.

python:
"""



# Call the OpenAI API to generate completion
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=template,
    max_tokens=100,
    n=1,
    stop=None
)

# Retrieve the generated code
generated_code = response.choices[0].text.strip()

# Print the generated code
print("Generated Python code:")
print(generated_code)

