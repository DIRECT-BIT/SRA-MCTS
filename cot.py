import os
# os.environ['CUDA_VISIBLE_DEVICES']='0,1'

from CoT.task import *
import json
import random
from tqdm import tqdm
import sys
from contextlib import contextmanager

@contextmanager
def redirect_stdout_to_file(filename):
    original_stdout = sys.stdout
    with open(filename, 'a', encoding='utf-8') as file:
        sys.stdout = file
        try:
            yield
        finally:
            sys.stdout = original_stdout

with open('', 'r') as f: # Your question files
    lines = f.readlines()

model = 'qwen-14B'


reasoning = open('data/cot-'+ model + '-reasoning'+ '.json', 'a', encoding='utf-8')

output_file = 'cot-output-' + model + '.log'

count = 0
# 打印抽取的行
for line in tqdm(lines):
    question = json.loads(line)['question']
    with redirect_stdout_to_file(output_file):
        task = CoT_Task(question, model, model)
        output = task.run()
        reasoning.write(json.dumps({'question': question, 'solution': output['solution']}, ensure_ascii=False) + '\n')
        if count % 10 == 0:
            reasoning.flush()
        
reasoning.close()
# print(output[0]['solution'])
# print(output[0]['summary'])

