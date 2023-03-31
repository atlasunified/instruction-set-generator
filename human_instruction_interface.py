import json
import gradio as gr
import datetime

def current_timestamp():
    now = datetime.datetime.utcnow()
    return now.strftime('%Y-%m-%dT%H:%M:%SZ')

def jsonl_template(id, name, instruction, input1, output1, input2, output2, is_classification, label1, label2, source, complexity, tag1, tag2, timestamp, language, domain, author):
    instances = [
        {"input": input1, "output": output1},
        {"input": input2, "output": output2}
    ]
    jsonl_dict = {
        "id": id,
        "name": name,
        "instruction": instruction,
        "instances": instances,
        "is_classification": is_classification,
        "labels": [label1, label2],
        "source": source,
        "complexity": complexity,
        "tags": [tag1, tag2],
        "timestamp": timestamp,
        "language": language,
        "domain": domain,
        "author": author
    }
    return jsonl_dict

def save_to_jsonl(jsonl_obj, filename):
    with open(filename, "a") as f:
        f.write(json.dumps(jsonl_obj))
        f.write("\n")

def generate_jsonl(id, name, instruction, input1, output1, input2, output2, is_classification, label1, label2, source, complexity, tag1, tag2, timestamp, language, domain, author, filename):
    jsonl_obj = jsonl_template(id, name, instruction, input1, output1, input2, output2, is_classification, label1, label2, source, complexity, tag1, tag2, timestamp, language, domain, author)
    save_to_jsonl(jsonl_obj, filename)
    return "{}".format(json.dumps(jsonl_obj, indent=2), filename)

def input_components():
    components = []
    with gr.Row():
        components.append(gr.Textbox(label="ID", value="H-500k-dataset-000001", elem_id="id"))
        components.append(gr.Textbox(label="Name", value="Enter the task name", elem_id="name"))
        components.append(gr.Textbox(label="Instruction", value="Enter the instruction of what this set describes", elem_id="instruction"))
        components.append(gr.Textbox(label="Input 1", value="INPUT1", elem_id="input1"))
        components.append(gr.Textbox(label="Output 1", value="OUTPUT1", elem_id="output1"))
        components.append(gr.Textbox(label="Input 2", value="INPUT2", elem_id="input2"))
        components.append(gr.Textbox(label="Output 2", value="OUTPUT2", elem_id="output2"))
        components.append(gr.Checkbox(label="Is Classification", elem_id="is_classification"))
        components.append(gr.Textbox(label="Label 1", value="Machine Learning", elem_id="label1"))
        components.append(gr.Textbox(label="Label 2", value="LABEL2", elem_id="label2"))
        components.append(gr.Textbox(label="Source", value="An Introduction to Machine Learning", elem_id="source"))
        components.append(gr.Textbox(label="Complexity", value="Basic/Novice/Intermediate/Advanced/Expert", elem_id="complexity"))
        components.append(gr.Textbox(label="Tag 1", value="TAG1", elem_id="tag1"))
        components.append(gr.Textbox(label="Tag 2", value="TAG2", elem_id="tag2"))
        components.append(gr.Textbox(label="Timestamp", value=current_timestamp(), elem_id="timestamp"))
        components.append(gr.Textbox(label="Language", value="English", elem_id="language"))
        components.append(gr.Textbox(label="Domain", value="Machine Learning", elem_id="domain"))
        components.append(gr.Textbox(label="Author", value="Atlas Unified", elem_id="author"))
        components.append(gr.Textbox(label="Filename", value="output-test.jsonl", elem_id="filename"))

    return components

inputs = input_components()
output = gr.Label()
jsonl_output = gr.TextArea()

jsonl_interface = gr.Interface(
    fn=generate_jsonl, 
    inputs=inputs, 
    outputs=jsonl_output,
    title="JSONL Output",
    description="The generated JSONL object in raw form."
)

qap=gr.Markdown("""
# Example of a Question-Answer Pair

{
"id": "G-500k-dataset-000001",
"name": "Question-Answer Pairs",
"instruction": "Create a language model using AI algorithms and question-answer pairs to identify correct answers to related input.",
"instances": [
{"input": "What is AI?", "output": "Artificial Intelligence is a branch of computer science that uses algorithms and AI technologies to simulate intelligent behavior."},
{"input": "What is Machine Learning?", "output": "Machine learning is a type of artificial intelligence that uses algorithms to learn from data, identify patterns and make decisions without being explicitly programmed to do so."},

],
"is_classification": "False",
"labels": ["Machine Learning"],
"source": "Machine Learning Research Papers",
"complexity": "Intermediate",
"tags": ["Artificial Intelligence", "Machine Learning", "Question-Answer Pairs"],
"timestamp": "2023-03-29T12:54:00Z",
"language": "English",
"domain": "AI",
"author": "Atlas Unified"
}

""")

clt=gr.Markdown("""
# Example of Cloze Test

{
"id": "G-500k-dataset-000001",
"name": "Cloze Test",
"instruction": "Initialize a model that outputs 'cloze' as an answer, such asfill-in-the-blank questions. The model should take an incomplete text sentence as an input and a full,finalised sentence as an output. Use a 500K dataset for training and testing.",
"instances": [
{"input": "John went to the ____ to buy some milk.", "output": "John went to the supermarket to buy some milk."},
{"input": "Jane's mom gave her a ____ of chocolates.", "output": "Jane's mom gave her a box of chocolates."},

],
"is_classification": "False",
"labels": [],
"source": "https://en.wikipedia.org/wiki/Cloze_test",
"complexity": "High",
"tags": ["cloze test", "fill-in-the-blank", "natural language processing"], 
"timestamp": "2023-03-29T12:54:00Z",
"language": "English",
"domain": "Machine Learning",
"author": "Atlas Unified"
}
    
    """)

cod=gr.Markdown("""
# Example of Conversational Dialogue

{
"id": "G-500k-dataset-000001",
"name": "Conversational Dialogue",
"instruction": "Create a language model using AI algorithms and conversational dialogue to generate natural-sounding responses to user queries.",
"instances": [
{"input": "What is the weather like today?", "output": "It's sunny and 75 outside today! Sun protection is adviseable today."},
{"input": "How do I cancel my order?", "output": "We will head over to their website and begin the process of cancellation."},

],
"is_classification": "False",
"labels": ["Artificial Intelligence", "Machine Learning"],
"source": "Conversational Datasets",
"complexity": "low",
"tags": ["Artificial Intelligence", "Dialogue", "Natural Language Generation"],
"timestamp": "2023-03-29T12:54:00Z",
"language": "English",
"domain": "AI",
"author": "Atlas Unified"
}
    
    """)

muc=gr.Markdown("""
# Example of Multiple Choice

{
"id": "G-500k-dataset-000001",
"name": "Multiple Choice",
"instruction": "This task consists of labeled data consisting of a set of multiple choices and correct input answers. Specify the set of input, output and labels and any additional information such as tags, language and domain as required.",
"instances": [
"instruction": "This task consists of labeled data with descriptions of machine learning algorithms and their corresponding names. Specify the set of input, output, and labels, as well as any additional information such as tags, language, and domain as required.",
{"input": "Which algorithm is primarily used for reducing the number of features in a dataset?", "output": "Principal Component Analysis (PCA)"},
{"input": "Which algorithm is a popular supervised learning method for classification and regression tasks?", "output": "Support Vector Machine (SVM)"}

],
"is_classification": "True",
"labels": ["Geography", "History"],
"source": "Wikipedia",
"complexity": "High",
"tags": ["Multiple Choice", "Questions"],
"timestamp": "2023-03-29T12:54:00Z",
"language": "English",
"domain": "Geography and History",
"author": "Atlas Unified"
}
    
    """)

xxx=gr.Markdown("""
# Example of xx


    
    """)

xxx=gr.Markdown("""
# Example of xx


    
    """)

xxx=gr.Markdown("""
# Example of xx


    
    """)


main_interface = gr.Interface(fn=generate_jsonl, inputs=inputs, outputs=output, title="Human Dataset Developer Template", description="Fill in the fields and click 'submit' to generate and save a JSONL object. All sets created will be in the main directory and log properly. Please number your sets accordingly. If you would like to modify your file name, understand that a new list will be created if you re-name the 'output.jsonl' file.")

dash = gr.TabbedInterface([main_interface, qap, clt, cod, muc], ["Human Interface Dashboard", "QAP", "CLT", "COD", "MUC"])

dash.launch(inbrowser=True)