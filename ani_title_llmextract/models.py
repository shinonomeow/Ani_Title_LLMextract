"""
数据模型定义
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class AnimeTitle:
    """动漫标题解析结果数据模型"""

    # 标题信息
    original_title: str | None = None
    title_zh: str | None = None
    title_jp: str | None = None
    title_romaji: str | None = None
    title_en: str | None = None

    # 时间信息
    year: str | None = None
    season: str | None = None

    # 剧集信息
    episode: str | None = None

    # 制作信息
    fansub: str | None = None

    # 字幕信息
    subtitle: str | None = None

    # 特殊标记
    version: str | None = None


    def to_dict(self) -> dict:
        """转换为字典格式"""
        return {
            field.name: getattr(self, field.name)
            for field in self.__dataclass_fields__.values()
            if getattr(self, field.name) is not None
        }

    def __str__(self) -> str:
        """字符串表示"""
        parts = []
        if self.title_zh:
            parts.append(f"中文: {self.title_zh}")
        if self.title_jp:
            parts.append(f"日文: {self.title_jp}")
        if self.title_romaji:
            parts.append(f"罗马字: {self.title_romaji}")
        if self.title_en:
            parts.append(f"英文: {self.title_en}")
        if self.year:
            parts.append(f"年份: {self.year}")
        if self.season:
            parts.append(f"季度: {self.season}")
        if self.episode:
            parts.append(f"集数: {self.episode}")
        if self.fansub:
            parts.append(f"字幕组: {self.fansub}")

        return " | ".join(parts) if parts else "未解析到信息"
