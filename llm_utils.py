import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI
from config import my_model, break_master_prompt

load_dotenv()

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY", default="sk-xxx"),
    base_url=os.getenv("DASHSCOPE_BASE_URL", default="https://dashscope.aliyuncs.com/compatible-mode/v1"),
)

def llm_gen(messages:list[dict], model:str=my_model):
    completion = client.chat.completions.create(
        model = model,
        messages = messages,
        # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
        # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
        extra_body = {"enable_thinking": False},
    )
    result_json = completion.model_dump_json()
    return result_json

def llm_breaking_game(number: int=1, system_prompt:str=break_master_prompt)->dict:
    msgs = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"生成{number}个破冰小游戏"},
    ]
    result_json = llm_gen(messages=msgs)
    result_str =  json.loads(result_json)['choices'][0]['message']['content']
    
    # 提取代码块中的JSON内容
    json_match = re.search(r'```(?:json)?\s*({.*?})\s*```', result_str, re.DOTALL)
    if json_match:
        result_str = json_match.group(1)
    
    result_dict = json.loads(result_str)
    # print(result_dict)
    return result_dict
