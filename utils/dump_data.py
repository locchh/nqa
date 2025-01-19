import json
from tqdm import tqdm
from datasets  import load_dataset

dataset_name = "locchh/Nvidia_AI_Infrastructure_and_Operations_Fundamentals_MCQA"

dataset = load_dataset(dataset_name)

data = []

for i in tqdm(range(dataset["train"].num_rows)):
    
    sample = dataset["train"][i]

    record = {}

    record["question"] = sample["question"]
    record["A"] = sample["A"]
    record["B"] = sample["B"]
    record["C"] = sample["C"]
    record["D"] = sample["D"]

    if sample["answer"] == record["A"]:
        record["answer"] = "A"
    
    if sample["answer"] == record["B"]:
        record["answer"] = "B"

    if sample["answer"] == record["C"]:
        record["answer"] = "C"

    if sample["answer"] == record["D"]:
        record["answer"] = "D"

    data.append(record)


with open("./assets/data.json","w",encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Done!")