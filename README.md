# 🧠 **NQA: NVIDIA-Related Question and Answer Project**  

A comprehensive platform for creating and managing question-and-answer datasets and models related to NVIDIA technologies.  

---

## ✅ **TODOs**

| No | Task                                         | Status |
|----|----------------------------------------------|--------|
| 01 | Create `nvidia_qa` dataset                   | ✅     |
| 02 | Evaluate and Fine-tune model                 | 🛠️     |
| 03 | Deploy model                                 | ❌     |
| 04 | Generate synthetic context, options          | ❌     |
| 05 | Create `nvidia_mcqa` dataset                 | ❌     |

---

## 📂 **Datasets**

- **[nvidia_qa](https://huggingface.co/datasets/locchh/nvidia_qa):**  
  A dataset of questions and answers.

- **[nvidia_qa_ctx]():**  
  A question-and-answer dataset enriched with synthetic context.

- **[nvidia_mcqa]():**  
  A dataset of multiple-choice questions and answers.

- **[nvidia_mcqa_ctx]():**  
  A dataset of multiple-choice questions and answers, enriched with synthetic context.

---

## 📖 **References**

Here are some key datasets and resources that inspired and supported this project:

**Models**:
- [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
- [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- [SmolLM 135M, 360M, 1.7B](https://huggingface.co/collections/HuggingFaceTB/smollm-6695016cad7167254ce15966)

**Datasets**:  
- [tatsu-lab Alpaca Dataset](https://huggingface.co/datasets/tatsu-lab/alpaca)  
- [Rajpurkar's SQuAD Dataset](https://huggingface.co/datasets/rajpurkar/squad)  
- [AllenAI's SWAG Dataset](https://huggingface.co/datasets/allenai/swag)  
- [NVIDIA-QA by ajsbsd](https://huggingface.co/datasets/ajsbsd/nvidia-qa)  
- [NVIDIA QA Formatted by arunima29](https://huggingface.co/datasets/arunima29/nvidia_qa_formatted)  

**Resources for Implementation**:  
- [Multiple Choice with Transformers](https://huggingface.co/docs/transformers/tasks/multiple_choice)  
- [LFQA (Long-Form Question Answering) Overview](https://yjernite.github.io/lfqa.html)  

**Key Papers**:  
- [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461)  
- [ELI5: Long Form Question Answering](https://arxiv.org/pdf/1907.09190)  
- [How Much Knowledge Can You Pack Into the Parameters of a Language Model?](https://arxiv.org/pdf/2002.08910)  
- [Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor](https://arxiv.org/pdf/2212.09689)