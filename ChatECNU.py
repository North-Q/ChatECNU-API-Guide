import os
from openai import OpenAI
import requests

# 使用 OpenAI SDK 调用 ECNU 大语言模型平台的函数
def call_openai_sdk(api_key, base_url, model, messages):
    # 创建 OpenAI 客户端
    client = OpenAI(
        api_key=api_key,  # API 密钥
        base_url=base_url,  # 基础 URL
    )
    # 创建聊天完成请求
    completion = client.chat.completions.create(
        model=model,  # 模型名称
        messages=messages,  # 消息列表
    )
    # 返回 JSON 格式的响应
    return completion.model_dump_json()

# 直接调用 ECNU 大语言模型平台 API 的函数
def call_api_directly(api_key, url, model, messages, search_mode=None):
    # 设置请求头
    headers = {
        "Authorization": f"Bearer {api_key}",  # 认证信息
        "Content-Type": "application/json"  # 内容类型
    }

    # 设置请求数据
    data = {
        "model": model,  # 模型名称
        "messages": messages  # 消息列表
    }

    # 如果启用了搜索模式，则添加到请求数据中
    if search_mode:
        data["search_mode"] = search_mode

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data)
    # 返回 JSON 格式的响应
    return response.json()

# 示例调用
if __name__ == "__main__":
    api_key = 'your-api-key'  # API 密钥
    base_url = "https://chat.ecnu.edu.cn/open/api/v1"  # 基础 URL
    model = "ecnu-plus"  # 模型名称
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},  # 系统消息
        {'role': 'user', 'content': '你是谁？'}  # 用户消息
    ]

    # 调用使用 OpenAI SDK 的函数并打印结果
    print(call_openai_sdk(api_key, base_url, model, messages))

    url = "https://chat.ecnu.edu.cn/open/api/v1/chat/completions"  # API URL
    model = "ecnu-max"  # 模型名称
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},  # 系统消息
        {"role": "user", "content": "华东师范大学是哪一年成立的？"}  # 用户消息
    ]
    search_mode = "enable"  # 启用搜索模式

    # 调用直接调用 API 的函数并打印结果
    print(call_api_directly(api_key, url, model, messages, search_mode))