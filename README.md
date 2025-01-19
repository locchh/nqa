# NQA: NVIDIA-Related Question and Answer Project 🧠

A platform dedicated to creating, managing, and evaluating question-and-answer datasets and models focused on NVIDIA technologies. 🚀

---

## 📋 Project Tasks and Status 

| Task No. | Description                                                                 | Status        |
|----------|-----------------------------------------------------------------------------|---------------|
| 01       | Create the `nvidia_qa` dataset                                                | ✅ Completed  |
| 02       | Evaluate and fine-tune the model on the `nvidia_qa` dataset                   | ✅ Completed  |
| 03       | Develop an MCQA application to enhance knowledge of the "NVIDIA AI Infrastructure and Operations Fundamentals" course. | ✅ Completed |
| 04       | Implement multiple-choice question and answer task                          | 🛠️ In Progress |
| 05       | Generate synthetic context and answer options                               | 🛠️ In Progress |
| 06       | Create the `nvidia_mcqa` dataset                                            | ❌ Not Started |

---

## 📂 Datasets 

The following datasets are integral to the project:  

- [Nvidia_AI_Infrastructure_and_Operations_Fundamentals_QA](https://huggingface.co/datasets/locchh/Nvidia_AI_Infrastructure_and_Operations_Fundamentals_QA):  
  A question-and-answer dataset for the "NVIDIA AI Infrastructure and Operations Fundamentals" course. 🎓

- [Nvidia_AI_Infrastructure_and_Operations_Fundamentals_MCQA](https://huggingface.co/datasets/locchh/Nvidia_AI_Infrastructure_and_Operations_Fundamentals_MCQA):  
  A multiple-choice question dataset for the same course.

- [nvidia_qa](https://huggingface.co/datasets/locchh/nvidia_qa):  
  A curated dataset of questions and answers.

- nvidia_qa_ctx:  
  A question-and-answer dataset enriched with synthetic context. *(Link coming soon)*

- nvidia_mcqa:  
  A dataset featuring multiple-choice questions and answers. *(Link coming soon)*

- nvidia_mcqa_ctx:  
  A multiple-choice dataset enriched with synthetic context. *(Link coming soon)*

---

## 📊 Evaluation 

- For evaluation on the `nvidia_qa` dataset, refer to the detailed guide: [Evaluation Documentation](./assets/docs/evaluate_nvidia_qa.md) 📖  
- Evaluation documentation for the `nvidia_mcqa` dataset is under development. *(Link coming soon)* ⏳

---

## 📚 References and Resources 

### Models  
The following pre-trained models are instrumental in this project:  

- [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) 🦙  
- [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) 🦙  
- [SmolLM (135M, 360M, 1.7B) Instruct](https://huggingface.co/collections/HuggingFaceTB/smollm-6695016cad7167254ce15966) 🤖

### Datasets  
The project references key datasets for inspiration and benchmarking:  

- [Alpaca Dataset (tatsu-lab)](https://huggingface.co/datasets/tatsu-lab/alpaca) 🦙  
- [SQuAD Dataset (Rajpurkar)](https://huggingface.co/datasets/rajpurkar/squad) 📖  
- [SWAG Dataset (AllenAI)](https://huggingface.co/datasets/allenai/swag) 🧠  
- [NVIDIA-QA Dataset (ajsbsd)](https://huggingface.co/datasets/ajsbsd/nvidia-qa) 🖥️  
- [Formatted NVIDIA QA Dataset (arunima29)](https://huggingface.co/datasets/arunima29/nvidia_qa_formatted) 📝  

### Implementation Resources  
The following resources were instrumental in implementing project components:  

- [Multiple Choice with Transformers](https://huggingface.co/docs/transformers/tasks/multiple_choice) 🔄  
- [LFQA (Long-Form Question Answering) Overview](https://yjernite.github.io/lfqa.html) 📚

### Key Research Papers  
This project draws insights from several significant publications:  

- [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461) 📑  
- [ELI5: Long Form Question Answering](https://arxiv.org/pdf/1907.09190) 📖  
- [How Much Knowledge Can You Pack Into the Parameters of a Language Model?](https://arxiv.org/pdf/2002.08910) 🧠  
- [Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor](https://arxiv.org/pdf/2212.09689) 🤖

---

## 🔍 Insights 

- *Training involves iterative optimization to improve the model’s performance on the validation set by learning patterns, features, and relationships in the training data.*  

- *A notable challenge in specific-domain closed-book question answering is the reliance on external knowledge collections, where the model lacks explicit references to pinpoint answers.*