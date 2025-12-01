#!/usr/bin/env python3
"""
FastMCP Meeting Atmosphere Group Template

This is a template for creating a meeting atmosphere group MCP server using the FastMCP framework.
"""

import os
import json
import http.client
from typing import List
from fastmcp import FastMCP
from dotenv import load_dotenv
from llm_utils import llm_breaking_game
load_dotenv()


# Initialize the MCP server
mcp = FastMCP("Meeting Atmosphere Group")


@mcp.tool()
def ice_breaking_game(num_people: int, number: int = 1) -> List[str]:
    """
    Generate ice-breaking games based on the number of participants
    
    Args:
        num_people (int): Number of people participating in the game
        number (int): Number of game suggestions to generate. Defaults to 1.
        
    Returns:
        List[str]: List of ice-breaking game descriptions
    """
    try:
        # Use LLM to generate ice breaking games
        result = llm_breaking_game(number=num_people)
        if "games" in result and isinstance(result["games"], list):
            # Return the requested number of game suggestions
            return result["games"][:number] if number > 0 else [result["games"][0]]
        else:
            # Fallback in case of unexpected response format
            return [f"抱歉，暂时无法生成适合{num_people}人的破冰游戏，请稍后再试。"]
    except json.JSONDecodeError as e:
        return [f"生成破冰游戏时出现JSON解析错误: {str(e)}"]
    except Exception as e:
        return [f"生成破冰游戏时出错: {str(e)}"]


@mcp.tool()
def jokes(count: int) -> List[str]:
    """
    Get a list of jokes
    
    Args:
        count (int): Number of jokes required
        
    Returns:
        List[str]: List of jokes
    """
    try:
        conn = http.client.HTTPSConnection("eolink.o.apispace.com")
        payload = f"pageSize={count}"
        headers = {
            "X-APISpace-Token": os.getenv("JOKE_API_KEY", "l91daxsew9srjqkahn23kmj6fgi9j0ds"),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        conn.request("POST", "/xhdq/common/joke/getJokesByRandom", payload, headers)
        res = conn.getresponse()
        data = res.read()
        response_data = json.loads(data.decode("utf-8"))
        
        # 根据实际API响应结构调整提取笑话的方式
        # API返回的数据结构包含statusCode、desc和result字段，其中result是包含笑话的数组
        if 'result' in response_data and isinstance(response_data['result'], list):
            jokes_list = [item.get('content', '') for item in response_data['result'][:count]]
            return jokes_list
        else:
            return ["获取笑话失败，请稍后再试。"]
            
    except Exception as e:
        print(f"获取笑话时发生错误: {str(e)}")
        return [f"获取笑话时发生错误: {str(e)}"]


def main():
    # mcp.run(transport="streamable-http") # This will start a Uvicorn server on the default host (127.0.0.1), port (8000), and path (/mcp).
    mcp.run( # or: customize your MCP server's port and path
        # transport="streamable-http",
        transport="sse",
        host="0.0.0.0",
        port=8080,
        path="/mcp",
        log_level="debug",
    )

if __name__ == "__main__":
    # Run the server
    main()