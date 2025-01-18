### **Prerequisites**
1. Install the necessary libraries:
   ```bash
   pip install transformers datasets evaluate torch
   ```

2. Ensure you have a GPU-enabled environment for efficient training:
   ```bash
   pip install accelerate
   ```

---

### **Steps for Fine-Tuning**

1. **Prepare the Dataset**  
   Use the `datasets` library to process and tokenize your dataset.

   ```python
   from transformers import AutoTokenizer
   from datasets import DatasetDict

   # Assume your dataset is structured as shown
   dataset = DatasetDict({
       "train": train_dataset,
       "validation": validation_dataset,
       "test": test_dataset
   })

   # Load the tokenizer
   model_name = "HuggingFaceTB/SmolLM-360M"
   tokenizer = AutoTokenizer.from_pretrained(model_name)

   # Tokenize the dataset
   def tokenize_function(example):
       return tokenizer(
           example["question"], 
           example["answer"], 
           truncation=True, 
           padding="max_length", 
           max_length=128
       )

   tokenized_datasets = dataset.map(tokenize_function, batched=True)
   ```

---

2. **Set Up Data Collator**  
   Use a data collator to handle batching and padding.

   ```python
   from transformers import DataCollatorForSeq2Seq

   data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model_name)
   ```

---

3. **Load the Model**  
   Load the pre-trained sequence-to-sequence model.

   ```python
   from transformers import AutoModelForCausalLM

   model = AutoModelForCausalLM.from_pretrained(model_name)
   ```

---

4. **Define Metrics**  
   Set up BLEU and ROUGE metrics for evaluation.

   ```python
   import evaluate

   bleu_metric = evaluate.load("bleu")
   rouge_metric = evaluate.load("rouge")

   def compute_metrics(eval_pred):
       predictions, labels = eval_pred
       decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
       decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

       # BLEU score
       bleu_score = bleu_metric.compute(
           predictions=decoded_preds, 
           references=[[label] for label in decoded_labels]
       )

       # ROUGE score
       rouge_score = rouge_metric.compute(
           predictions=decoded_preds, 
           references=decoded_labels
       )

       # Combine metrics
       return {
           "bleu": bleu_score["bleu"],
           "rouge1": rouge_score["rouge1"],
           "rouge2": rouge_score["rouge2"],
           "rougeL": rouge_score["rougeL"],
           "rougeLsum": rouge_score["rougeLsum"]
       }
   ```

---

5. **Configure TrainingArguments**  
   Specify training configurations, including batch size, learning rate, and evaluation strategy.

   ```python
   from transformers import TrainingArguments

   training_args = TrainingArguments(
       output_dir="./results",
       evaluation_strategy="epoch",
       learning_rate=5e-5,
       per_device_train_batch_size=8,
       per_device_eval_batch_size=8,
       num_train_epochs=3,
       weight_decay=0.01,
       save_strategy="epoch",
       save_total_limit=2,
       predict_with_generate=True,
       logging_dir="./logs",
       logging_steps=10
   )
   ```

---

6. **Initialize Trainer**  
   Combine the model, dataset, and configurations into a `Trainer` instance.

   ```python
   from transformers import Trainer

   trainer = Trainer(
       model=model,
       args=training_args,
       train_dataset=tokenized_datasets["train"],
       eval_dataset=tokenized_datasets["validation"],
       tokenizer=tokenizer,
       data_collator=data_collator,
       compute_metrics=compute_metrics,
   )
   ```

---

7. **Train the Model**  
   Begin fine-tuning the model.

   ```python
   trainer.train()
   ```

---

8. **Evaluate and Test the Model**  
   Evaluate the model on the test dataset.

   ```python
   results = trainer.evaluate(tokenized_datasets["test"])
   print(results)
   ```

---

9. **Save the Fine-Tuned Model**  
   Save the fine-tuned model and tokenizer.

   ```python
   trainer.save_model("./fine_tuned_model")
   tokenizer.save_pretrained("./fine_tuned_model")
   ```

---

### **Key Points**
- **BLEU** is great for measuring n-gram overlaps.
- **ROUGE** evaluates recall-focused text overlaps, which is particularly useful for summarization tasks.
- **Hyperparameter Tuning**: Experiment with learning rates, batch sizes, and epochs for optimal performance.
- **Experiment Tracking**: Use tools like [Weights & Biases](https://wandb.ai/) or TensorBoard.