"""
动漫标题解析器
"""

from __future__ import annotations

import os
import warnings
import logging

from .models import AnimeTitle
import langextract as lx


class AnimeTitleParser:
    """动漫标题解析器类"""

    def __init__(
        self, model_id: str = "gemini-2.5-flash", api_key: str | None = None, **kwargs
    ):
        """
        初始化解析器

        Args:
            model_id: 使用的模型ID
            api_key: API密钥，如果为None则从环境变量获取
            use_modular: 是否使用模块化提取器
            **kwargs: 传递给extractors的其他参数
        """
        # 抑制absl警告
        logging.getLogger('absl').setLevel(logging.ERROR)
        warnings.filterwarnings('ignore', category=UserWarning, module='absl')

        self.model_id: str = model_id
        self.api_key: str | None = api_key or os.environ.get("LANGEXTRACT_API_KEY")
        # 保留旧的实现作为备选
        from .prompts import get_unified_prompt, get_unified_examples

        self._prompt: str = get_unified_prompt()
        self._examples: list[lx.data.ExampleData] = get_unified_examples()

    def parse_title(self, title: str) -> AnimeTitle | None:
        """
        解析动漫标题

        Args:
            title: 动漫文件名或标题

        Returns:
            AnimeTitle: 解析结果
        """
        # 预处理：替换符号为空格
        preprocessed_title = self._preprocess_title(title)
        return self._parse_title(preprocessed_title)

    def _preprocess_title(self, title: str) -> str:
        """
        预处理标题，将符号替换为空格

        Args:
            title: 原始标题

        Returns:
            str: 预处理后的标题
        """
        # 定义需要替换为空格的符号
        symbols_to_replace = [
            "【",
            "】",
            "[",
            "]",
            "★",
            "☆",
            "~",
            "/",
            "\\",
            "|",
            ":",
            "：",
            "–",
            "—",
            "+",
            "=",
            "<",
            ">",
            "{",
            "}",
            "(",
            ")",
            "「",
            "」",
            "『",
            "』",
            "（",
            "）",
        ]

        processed_title = title
        for symbol in symbols_to_replace:
            processed_title = processed_title.replace(symbol, " ")

        return processed_title

    def _parse_title(self, title: str) -> AnimeTitle | None:
        """
        使用原始方法解析标题（向后兼容）

        Args:
            title: 动漫文件名或标题

        Returns:
            AnimeTitle: 解析结果
        """
        try:
            # 使用langextract提取信息
            result = lx.extract(
                text_or_documents=title,
                prompt_description=self._prompt,
                examples=self._examples,
                model_id=self.model_id,
                api_key=self.api_key,
            )

            # 转换为AnimeTitle对象
            anime_title = self._convert_to_anime_title(result, title)
            return anime_title

        except Exception as e:
            # 错误处理：返回仅包含原始文本的对象
            #
            print(f"Error parsing title: {title}")
            print(f"Exception: {e}")
            return None

    def _convert_to_anime_title(self, result, original_title: str) -> AnimeTitle:
        """将langextract结果转换为AnimeTitle对象"""

        # 初始化所有字段
        data = {
            "original_title": original_title,
            "title_zh": None,
            "title_jp": None,
            "title_romaji": None,
            "title_en": None,
            "year": None,
            "season": None,
            "episode": None,
            "fansub": None,
            "subtitle": None,
            "version": None,
        }

        # 处理提取的实体
        for extraction in result.extractions:
            extraction_class = extraction.extraction_class
            extraction_text = extraction.extraction_text

            if extraction_class in data:
                data[extraction_class] = extraction_text
                print(f"Extracted {extraction_class}: {extraction_text},{type(extraction_text)}, attributes: {extraction.attributes}")
                if extraction.attributes is None:
                    continue
                if extraction_class == "episode":
                    # 处理集数的属性
                    episode_number = extraction.attributes.get("episode_number")
                    if episode_number:
                        data["episode"] = episode_number
                elif extraction_class == "season":
                    # 处理季度的属性
                    season_number = extraction.attributes.get("season_number")
                    if season_number:
                        data["season"] = season_number
                elif extraction_class == "subtitle":
                    # 处理字幕组的属性
                    subtitle_language = extraction.attributes.get("subtitle_language")
                    if subtitle_language:
                        data["subtitle"] = subtitle_language
                elif extraction_class == "version":
                    # 处理版本的属性
                    version_number = extraction.attributes.get("version_number")
                    if version_number:
                        data["version"] = version_number


        return AnimeTitle(**data)
