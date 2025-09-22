# Anime Title LLM Extract

A Python library for extracting structured information from anime titles using [langextract](https://github.com/google/langextract). This tool assists users in renaming and searching anime files by parsing various metadata from filename strings.

## Features

The library can extract the following information from anime titles:

- **Chinese Title** (`title_zh`) - 中文标题
- **Japanese Title** (`title_jp`) - 日文标题
- **Romanized Title** (`title_romaji`) - 罗马字标题
- **English Title** (`title_en`) - 英文标题
- **Year** (`year`) - 年份
- **Season** (`season`) - 季度
- **Episode** (`episode`) - 集数
- **Fansub Group** (`fansub`) - 字幕组
- **Subtitle Language** (`subtitle`) - 字幕语言
- **Version** (`version`) - 版本信息 (e.g., v1, v2)

## Installation

```bash
pip install ani-title-llmextract
```

## Usage Examples

### Basic Usage

```python
from ani_title_llmextract import extract_anime_info

# Extract information from a filename
filename = "[桜都字幕组] 进击的巨人 最终季 The Final Season [01][1080p][简繁内封]"
result = extract_anime_info(filename)

print(result)
# Output:
# {
#     'title_zh': '进击的巨人',
#     'fansub': '桜都字幕组',
#     'episode': '01',
#     'subtitle': '简繁内封'
# }
```

### Batch Processing

```python
from ani_title_llmextract import extract_anime_info

filenames = [
    "[ANi] 鬼滅之刃 - 01 [1080P][Baha][WEB-DL][AAC AVC][CHT][MP4]",
    "[Sakurato] 约定的梦幻岛 S2 - 05 [WebRip 1080p HEVC-10bit AAC][简繁内封]",
    "[NC-Raws] 呪術廻戦 - 24 [B-Global][WEB-DL][1080p][AVC AAC][ENG_THA_SUB][MKV]"
]

for filename in filenames:
    info = extract_anime_info(filename)
    print(f"Title: {info.get('title_zh', 'N/A')}, Episode: {info.get('episode', 'N/A')}")
```

## Roadmap

- [ ] **Special Episodes** (`special`) - 特殊集数支持
- [ ] **Subtitle Types** (`subtitle_type`) - 字幕类型识别 (e.g., OVA, 6.5)
- [ ] **Async Support** - 异步处理支持
- [ ] **Reduced Dependencies** - 减少对 langextract 的依赖，优化项目体积

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
