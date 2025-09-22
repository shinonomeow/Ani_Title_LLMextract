"""
ANI Title LLM Extract - 动漫标题解析库

使用 LangExtract 和 LLM 从动漫文件名中提取结构化信息
"""

from .models import AnimeTitle
from .parser import AnimeTitleParser

__version__ = "0.1.0"
__all__ = ["AnimeTitle", "AnimeTitleParser"]
