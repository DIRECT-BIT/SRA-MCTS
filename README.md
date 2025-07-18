
# SRA-MCTS: Self-driven Reasoning Augmentation with Monte Carlo Tree Search for Code Generation
This repository contains the implementation of **SRA-MCTS**, a self-driven reasoning augmentation method that leverages Monte Carlo Tree Search (MCTS) to generate high-quality reasoning steps for code generation tasks.

<div align="center">
  <img src="images/head.png" width="700" height="400" />
</div>
<p align="center">
  📄 <a href="https://arxiv.org/pdf/2411.11053" target="_blank">Paper</a> &nbsp; | &nbsp;
  🤗 <a href="#code" target="_blank">Quick start</a> &nbsp;
  🎰 <a href="https://huggingface.co/datasets/BinXD/SRA-MCTS-Llama-3.1-8B" target="_blank">Datasets</a> &nbsp;| &nbsp;
  ⚖️ <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache-2.0 License</a>
</p>


# Table of Contents
- [Overview](#overview)
- [Experimental Results](#experimental-results)
  - [Comparison between External Model Generated Data and Self-Generated Data](#comparison-between-external-model-generated-data-and-self-generated-data)
  - [Ablation Experiment](#ablation-experiment)
  - [Performance Comparison of Different Methods](#performance-comparison-of-different-methods)
- [Language Models and Datasets](#language-models-and-datasets)
- [Comparisons](#comparisons)
- [Code](#code)

# Overview
In this work, we propose and validate the following findings:

1. **Performance Improvement through Self-Generated Data**: Small models can achieve performance improvements comparable to, or even exceeding, those obtained from large-model-distilled data. Compared to methods using synthetic data generated by 70B models, SRA-MCTS demonstrates an average **2-point** improvement on Human-Eval and Human-Eval+ benchmarks for 2B and 8B scale models.

2. **Diversity and Effectiveness of Generated Data**: Data generated by SRA-MCTS is more diverse than that produced using the Chain-of-Thought (CoT) method. Experimental results show that SRA-MCTS surpasses CoT in enhancing model performance, achieving improvements of **5 points** and **3 points** at 8B and 14B scales, respectively.

3. We have open-sourced the complete process data generated by Meta-Llama-3.1-8B, covering reasoning paths and final code.

The overall workflow is as follows:
<div align="center">
  <img src="images/pipeline.jpg" width="600px" />
</div>

<div align="center">
  <img src="images/mcts_new.png" width="600px" />
</div>

<div align="center">
  <img src="images/evaluation.png" width="600px" />
</div>

# Experimental Results
Through extensive experiments, we found that:

1. **SRA-MCTS Enhances Small Models' Autonomous Reasoning Capabilities**
   - Compared to data generated by the 70B model synthesis method, SRA-MCTS improved the Human-Eval and Human-Eval+ scores by an average of 2 points at the 2B and 8B scales. The 70B model's data surpasses SRA-MCTS only at the 14B scale.
   - In comparison to distilled data from the 70B model, data generated by SRA-MCTS yields larger performance improvements for smaller models.

2. **SRA-MCTS Surpasses CoT in Overall Performance**
   - SRA-MCTS outperformed the CoT method on nearly all benchmarks, except for MBPP+, and achieved nearly a 2-point advantage over Instruct on Human-Eval+.
   - When calculating the incremental average values across various models and benchmarks, SRA-MCTS exhibited performance improvements at all model scales, with 5-point and 3-point gains at the 8B and 14B scales, respectively.

3. **SRA-MCTS Demonstrates Exceptional Performance in Diversity on pass@10**
   - SRA-MCTS outperformed CoT, especially in multi-pass generation tasks, demonstrating stronger diversity, particularly in smaller models.

4. **SRA-MCTS Exhibits Both Diversity and Reliability as Model Size Increases**
   - On smaller models, due to insufficient intermediate evaluation capabilities, SRA-MCTS primarily enhanced diversity, with improvements primarily observed in pass@10 (multiple generation).
   - As model size increases and the model's ability to follow instructions and evaluate improves, SRA-MCTS not only performs well in pass@10 but also surpasses CoT on pass@1, showcasing both diversity and reliability.

### Comparison between External Model Generated Data and Self-Generated Data

<p align="center">
  <img width="500" alt="62b86fc1ed018e717e1ef1ae806d88e" src="images/experiment1.png">
</p>

The above figure shows a performance comparison between the same model using self-generated data and data distilled from an external model. The external model used is **Meta-Llama-3-70B-Instruct**.

### Ablation Experiment

<div align="center">
  <img src="images/ablation.png" />
</div>

This experiment investigates the role of natural language reasoning steps in model responses. In this case, the **SRA-MCTS** training data includes both natural language reasoning and code, while another set of data only includes code.

We found that models trained without natural language data demonstrated a significant performance decline across all three model scales. While the performance gap was small (1-2 points) on the **Human-Eval** related benchmarks, the difference was much more pronounced on the **MBPP** related benchmarks.

- On the **2B** model, the performance gap on **MBPP+** was nearly **7** points, and the difference was around **1-2** points on other benchmarks.
- On the **8B** model, the performance gap on **MBPP** was as large as **7** points.
- The largest performance gap was observed on the **14B** model's **MBPP (pass@10)**, where the performance difference reached **13** points.

This clearly demonstrates the guiding and stimulating effect of natural language reasoning on model thinking.

### Performance Comparison of Different Methods

<p align="center">
  <img width="694" alt="e6b067489885e4de46dac0b2f8b15a9" src="images/experiment2.png">
</p>

The above table compares the performance of the **official instruction version**, **CoT training version**, and our proposed **SRA-MCTS** across **2B**, **8B**, and **14B** model scales. Values marked with **`*`** and **bold** indicate the best performance in specific benchmarks within that model scale category.

# Language Models and Datasets
We conducted experiments using **gemma-2-2b**, **Meta-Llama-3.1-8B**, and **Qwen2.5-14B** models, utilizing code-related evaluation datasets: **human-eval**, **human-eval+**, **MBPP**, and **MBPP+**.

# Comparisons
Comparison of SRA-MCTS with other models:

| Model | Size | Human-Eval | Human-Eval+ | MBPP  | MBPP+ |
|---|---|---|---|---|---|
| [gemma-2-2b-Instruct](https://huggingface.co/google/gemma-2-2b-it) | 2B | 39.76 | 33.05 | 34.42 | 43.39 |
| gemma-2-2b-CoT | 2B | 41.89 | 35.37 | 34.90 | 43.70 |
| **gemma-2-2b-SRA-MCTS** | 2B | 40.73 | 34.88 | 33.92 | 45.37 |
| [CodeGen-2B](https://arxiv.org/abs/2203.13474) | 2B | 24.4 | 22.6 | 46.3 | 36 |
| [CodeT5+-2B](https://www.salesforce.com/blog/codet5/) | 2B | 25 | 22 | 48.4 | 38.1 |
| [codegemma-2b](https://huggingface.co/google/codegemma-2b) | 2B | 26.8 | 20.7 | 55.6 | 46.6 |
|---|---|---|---|---|---|
| [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | 8B | 62.74 | 58.90 | 51.94 | 45.37 |
| Meta-Llama-3.1-8B-CoT | 8B | 62.32 | 58.35 | 52.94 | 60.50 |
| **Meta-Llama-3.1-8B-SRA-MCTS** | 8B | 62.19 | 57.87 | 54.52 | 59.97 |
| [Zephyr β-7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) | 7B | 30 | 23.2 | 42.1 | 34.7 |
| [Mistral-7B](https://mistral.ai/news/announcing-mistral-7b/) | 7B | 28.7 | 23.8 | 51.9 | 42.1 |
| [gemma-7b](https://huggingface.co/google/gemma-7b) | 7B | 35.4 | 28.7 | 52.6 | 43.4 |
| [CodeT5+-6B](https://www.salesforce.com/blog/codet5/) | 6B | 29.3 | 24.4 | 52.9 | 41.5 |
| [WizardCoder-Python-7B-V1.0](https://huggingface.co/WizardLM/WizardCoder-Python-7B-V1.0) | 7B | 50.6 | 45.1 | 58.5 | 49.5 |
| [CodeLlama-7B](https://about.fb.com/news/2023/08/code-llama-ai-for-coding/amp/) | 7B | 37.8 | 35.4 | 59.5 | 46.8 |
| [codegemma-7b](https://huggingface.co/google/codegemma-7b) | 7B | 44.5 | 41.5 | 65.1 | 52.4 |
| [DeepSeek-Coder-6.7B-Instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | 6.7B | 74.4 | 71.3 | 74.9 | 65.6 |
| [CodeQwen1.5-7B](https://huggingface.co/Qwen/CodeQwen1.5-7B) | 7B | 51.8 | 45.7 | 73.5 | 60.8 |
| [Magicoder-S-DS-6.7B](https://huggingface.co/ise-uiuc/Magicoder-S-DS-6.7B) | 6.7B | 76.8 | 71.3 | 79.4 | 69 |
|---|---|---|---|---|---|
| [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | 14B | 80.37 | 76.52 | 56.42 | 61.48 |
| Qwen2.5-14B-CoT | 14B | 78.66 | 73.84 | 58.12 | 63.97 |
| **Qwen2.5-14B-SRA-MCTS** | 14B | 85.37 | 75.00 | 61.02 | 61.16 |
| [CodeGen-16B](https://arxiv.org/abs/2203.13474) | 16B | 32.9 | 28 | 54.2 | 45.5 |
| [StarCoder-15B](https://huggingface.co/bigcode/starcoder) | 15B | 34.1 | 29.3 | 55.1 | 46.1 |
| [CodeT5+-16B](https://www.salesforce.com/blog/codet5/) | 16B | 31.7 | 26.8 | 56.6 | 47.1 |
| [CodeLlama-13B](https://about.fb.com/news/2023/08/code-llama-ai-for-coding/amp/) | 13B | 42.7 | 38.4 | 63.5 | 52.6 |
| [WizardCoder-15B-V1.0](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0) | 15B | 56.7 | 50.6 | 64.3 | 54.2 |

# Code
Below are the steps for a quick start:
### Create a Virtual Environment
  ```bash
  conda create --name SRA-MCTS python=3.10
  conda activate SRA-MCTS
  pip install requirements.txt
  ```
### Execution Steps  
1. In `models/model.py` at line 6, specify the path to the model you wish to use (absolute paths are recommended).
```
from models.inference_models import get_inference_model, get_local_response # , get_vllm_infer_model, get_local_response_vllm
from models.value_models import get_value_model, get_local_value # , get_vllm_value_model, get_local_value_vllm

path = 'path/to/model'

INFERENCE_MODEL_DIR = path
```
2. In the desired entry file (`cot.py`, `tot.py`, `mcts.py`), set the path to the dataset you want to use (formatted as a JSON file with only a `question` field), for example, `q.json`.
```
with open('path/to/q.json', 'r') as f: # Your question files
    lines = f.readlines()

model = 'qwen-0.5'
reasoning = open('data/'+ model + '-reasoning' + '.json', 'w', encoding='utf-8')
output_file = 'output-' + model + '.log'
   ```
then
```bash
  CUDA_VISIBLE_DEVICES=0,1 python cot.py 
```
3. After execution, the reasoning results (in natural language) will be saved in `data/reasoning`. Run `data/clean.ipynb` to filter the data by removing specific code content and lines with insufficient characters. The resulting file will be a JSON file with two fields: `question` and `solution`. For example:
```
   {"question": "Given the array `queries` of positive integers between `1` and `m`, you have to process all `queries[i]` (from `i=0` to `i=queries.length-1`) according to the following rules:\n\n*   In the beginning, you have the permutation `P=[1,2,3,...,m]`.\n*   For the current `i`, find the position of `queries[i]` in the permutation `P` (**indexing from 0**) and then move this at the beginning of the permutation `P.` Notice that the position of `queries[i]` in `P` is the result for `queries[i]`.\n\nReturn an array containing the result for the given `queries`.\n\n", "solution": "Step 1: Initialize the map `pos` with keys as numbers from 1 to m and values as their initial positions in the permutation P (which are their indices in the range from 0 to m-1).\nStep 2: Iterate over each query in the array `queries`, and for each query `queries[i]`, find its position in the permutation `P` by looking up its value in the `pos` map, then update the permutation `P` by removing the query from its current position and inserting it at the beginning of `P`, updating the `pos` map accordingly.\n"}
   ```
4. Use `data/translator.ipynb` to generate code for the filtered data. The resulting code will be saved in the `nl2sl` directory.
```
{"question": "### Question: A company has `n` employees with a unique ID for each employee from `0` to `n - 1`. The head of the company is the one with `headID`.\n\nEach employee has one direct manager given in the `manager` array where `manager[i]` is the direct manager of the `i-th` employee, `manager[headID] = -1`. Also, it is guaranteed that the subordination relationships have a tree structure.\n\nThe head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.\n\nThe `i-th` employee needs `informTime[i]` minutes to inform all of his direct subordinates (i.e., After informTime\\[i\\] minutes, all his direct subordinates can start spreading the news).\n\nReturn _the number of minutes_ needed to inform all the employees about the urgent news.\n\n\n### Solution: \nStep 1: Perform a depth-first search (DFS) from the head of the company to traverse the tree structure of the company and calculate the minimum time required for each employee to inform their direct subordinates.\n\n", "solution": "### Problem Solution: Inform All Employees\n\nWe can solve this problem using a depth-first search (DFS) approach. Here's the step-by-step implementation:\n\n```python\nfrom collections import defaultdict, deque\n\ndef numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:\n    \"\"\"\n    Calculate the minimum time required to inform all employees about the urgent news.\n\n    Args:\n    n (int): The number of employees.\n    headID (int): The ID of the head of the company.\n    manager (list[int]): A list of direct managers for each employee.\n    informTime (list[int]): A list of time required for each employee to inform their direct subordinates.\n\n    Returns:\n    int: The minimum time required to inform all employees about the urgent news.\n    \"\"\"\n\n    # Create a graph using an adjacency list representation\n    graph = defaultdict(list)\n    for i in range(n):\n        graph[manager[i]].append(i)\n\n    # Initialize the maximum time and the queue for BFS\n    max_time = 0\n    queue = deque([(headID, 0)])  # (employee ID, time)\n\n    while queue:\n        employee, time = queue.popleft()\n        max_time = max(max_time, time)\n        \n        # Add all the subordinates of the current employee to the queue\n        for subordinate in graph[employee]:\n            queue.append((subordinate, time + informTime[subordinate]))\n\n    return max_time\n```\n\n### Example Use Case:\n\n```python\nn = 6\nheadID = 2\nmanager = [2, 2, -1, 2, 2, 2]\ninformTime = [0, 0, 0, 0, 0, 0]\n\nresult = numOfMinutes(n, headID, manager, informTime)\nprint(result)  # Output: 1\n```\n\nIn this example, the head of the company is employee 2, and all employees are connected to employee 2. The time required for each employee to inform their direct subordinates is 0. Therefore, the minimum time required to inform all employees is 1."}
```
5. Run `merged.ipynb` in the `data/piped` directory to merge the prompts and shuffle the data.
```
{"question": "Create a structured approach to solve the problem, with each step explained in detail. After that, write the Python code that executes the solution.\nGiven an `m x n` matrix `matrix` and an integer `k`, return _the max sum of a rectangle in the matrix such that its sum is no larger than_ `k`.\n\nIt is **guaranteed** that there will be a rectangle with a sum no larger than `k`.\n\n**Example 1:**\n\n**Input:** matrix = \\[\\[1,0,1\\],\\[0,-2,3\\]\\], k = 2\n**Output:** 2\n**Explanation:** Because the sum of the blue rectangle \\[\\[0, 1\\], \\[-2, 3\\]\\] is 2, and 2 is the max number no larger than k (k = 2).\n\n**Example 2:**\n\n**Input:** matrix = \\[\\[2,2,-1\\]\\], k = 3\n**Output:** 3\n\n**Constraints:**\n\n*   `m == matrix.length`\n*   `n == matrix[i].length`\n*   `1 <= m, n <= 100`\n*   `-100 <= matrix[i][j] <= 100`\n*   `-105 <= k <= 105`\n\n**Follow up:** What if the number of rows is much larger than the number of columns?", "solution": "Step 1: Calculate the prefix sum of the matrix by iterating over each cell and adding the current value to the top, left, and top-left cells of the prefix sum matrix, while considering the matrix boundaries to avoid out-of-bounds errors.\nStep 2: Initialize two pointers, `left` and `right`, to the first column of the prefix sum matrix to represent the current window. Then, iterate over each row of the prefix sum matrix and for each row, calculate the maximum sum of the rectangle that can be formed with the current window by iterating over the `right` pointer and keeping track of the maximum sum found so far. After each iteration, move the `right` pointer to the right and update the `left` pointer if the sum of the rectangle exceeds `k`. Repeat this process until the `right` pointer reaches the last column of the prefix sum matrix.\nHere is the Python code that implements the given problem:\n\n```python\nclass Solution:\n    def maxSumSubmatrix(self, matrix, k):\n        m, n = len(matrix), len(matrix[0])\n        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]\n        \n        for i in range(1, m + 1):\n            for j in range(1, n + 1):\n                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]\n        \n        max_sum = float('-inf')\n        for left in range(n):\n            for right in range(left, n):\n                for i in range(1, m + 1):\n                    sum_ = prefix_sum[i][right + 1] - prefix_sum[i][left]\n                    if sum_ <= k and sum_ > max_sum:\n                        max_sum = sum_\n                    if prefix_sum[i][right + 1] - prefix_sum[i][left] > k:\n                        break\n        return max_sum\n```\n\nHere's an explanation of the code:\n\n*   We first create a prefix sum matrix `prefix_sum` of size `(m + 1) x (n + 1)` to store the prefix sums of the input matrix `matrix`.\n*   We then iterate over each cell in the input matrix and calculate the prefix sum for each cell by adding the current value to the top, left, and top-left cells of the prefix sum matrix. We use the formula `prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]` to calculate the prefix sum for each cell.\n*   We initialize two pointers, `left` and `right`, to the first column of the prefix sum matrix to represent the current window.\n*   We then iterate over each row of the prefix sum matrix and for each row, we calculate the maximum sum of the rectangle that can be formed with the current window by iterating over the `right` pointer and keeping track of the maximum sum found so far. We use the formula `sum_ = prefix_sum[i][right + 1] - prefix_sum[i][left"}
```

This process produces the final fine-tuning dataset, which can be used for subsequent fine-tuning tasks. The open-source dataset files are available in the corresponding folders, and you can refer to their formats and content for guidance.

Our inspiration comes from [ReST-MCTS*](https://arxiv.org/abs/2406.03816). The original method was designed to enhance a model's capabilities in mathematical reasoning, using Monte Carlo methods to derive the final results. Our approach extends this concept to the code domain, leveraging Monte Carlo to generate intermediate reasoning processes.

# Citation
If you use this work, please cite:
```
@article{xu2024sra,
  title={SRA-MCTS: Self-driven Reasoning Aurmentation with Monte Carlo Tree Search for Enhanced Code Generation},
  author={Xu, Bin and Lin, Yiguan and Li, Yinghao and others},
  journal={arXiv preprint arXiv:2411.11053},
  year={2024}
}
```
# Acknowledgments
This work was supported by the Major Research Plan of the National Natural Science Foundation of China (Grant No. 92370110).
