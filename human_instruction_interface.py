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
        components.append(gr.Textbox(label="Filename", value="output2.jsonl", elem_id="filename"))

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

test=gr.Markdown("test")

main_interface = gr.Interface(fn=generate_jsonl, inputs=inputs, outputs=output, title="Human Dataset Developer Template", description="Fill in the fields and click 'submit' to generate and save a JSONL object. All sets created will be in the main directory and log properly. Please number your sets accordingly. If you would like to modify your file name, understand that a new list will be created if you re-name the 'output.jsonl' file.")

dash = gr.TabbedInterface([main_interface, test], ["Human Interface Dashboard", "test"])

dash.launch(inbrowser=True)