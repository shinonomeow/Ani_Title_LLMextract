"""
提取器的 prompt 定义
"""

import textwrap

import langextract as lx


def get_unified_prompt() -> str:
    """获取统一的提取prompt"""
    return textwrap.dedent(
        """\
    "你是一个专业的动漫标题解析助手，能够从复杂的文件名或标题中提取关键信息。请根据以下示例格式，提取
    中文标题:title_zh, 为动漫的中文名称
    日文标题:title_jp, 为动漫的日文名称
    罗马字标题:title_romaji, 为动漫日文名称的罗马字拼写
    英文标题:title_en, 为动漫的英文名称
    年份:year, 为动漫的制作年份
    季度:season, 为动漫的季度信息，如第一季、第二季等, 名字中不一定有季度信息
    集数:episode, 为动漫的集数信息
    字幕组:fansub, 为制作该动漫字幕的字幕组名称
    字幕信息:subtitle, 为字幕的语言类型，如简体中文、繁体中文、英文等
    字幕类型:subtitle_type, 为字幕的类型，如硬字幕、软字幕等
    版本信息:version, 为该动漫的版本信息，如v1、v2等
    字段。如果某个字段无法提取，则返回空的字符串。"""
    )


def get_unified_examples() -> list[lx.data.ExampleData]:
    """获取统一的示例数据"""
    return [
        lx.data.ExampleData(
            text=" 幻樱字幕组  4月新番  古见同学有交流障碍症 第二季 Komi-san wa, Komyushou Desu. S02  22  GB_MP4  1920X1080 ",
            extractions=[
                lx.data.Extraction(
                    extraction_class="title_zh", extraction_text="古见同学有交流障碍症"
                ),
                lx.data.Extraction(extraction_class="title_jp", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="title_romaji",
                    extraction_text="Komi-san wa, Komyushou Desu.",
                ),
                lx.data.Extraction(extraction_class="title_en", extraction_text=""),
                lx.data.Extraction(extraction_class="year", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="season",
                    extraction_text="第二季",
                    attributes={"season_number": "2"},
                ),
                lx.data.Extraction(
                    extraction_class="episode",
                    extraction_text="22",
                    attributes={"episode_number": "22"},
                ),
                lx.data.Extraction(
                    extraction_class="fansub", extraction_text="幻樱字幕组"
                ),
                lx.data.Extraction(
                    extraction_class="subtitle",
                    extraction_text="GB",
                    attributes={"subtitle_language": "简"},
                ),
                lx.data.Extraction(
                    extraction_class="version",
                    extraction_text="",
                    attributes={"version_number": 0},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=" ANi  Grand Blue Dreaming /  GRAND BLUE 碧蓝之海 2 - 04  1080P  Baha  WEB-DL  AAC AVC  CHT  MP4 ",
            extractions=[
                lx.data.Extraction(
                    extraction_class="title_zh", extraction_text="GRAND BLUE 碧蓝之海"
                ),
                lx.data.Extraction(extraction_class="title_jp", extraction_text=""),
                lx.data.Extraction(extraction_class="title_romaji", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="title_en", extraction_text="Grand Blue Dreaming"
                ),
                lx.data.Extraction(extraction_class="year", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="season",
                    extraction_text="2",
                    attributes={"season_number": "2"},
                ),
                lx.data.Extraction(
                    extraction_class="episode",
                    extraction_text="04",
                    attributes={"episode_number": "4"},
                ),
                lx.data.Extraction(extraction_class="fansub", extraction_text="ANi"),
                lx.data.Extraction(
                    extraction_class="subtitle",
                    extraction_text="CHT",
                    attributes={"subtitle_language": "繁"},
                ),
                lx.data.Extraction(
                    extraction_class="version",
                    extraction_text="",
                    attributes={"version_number": "0"},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=" 天月搬运组  药师少女的独语  药屋少女的呢喃  / Kusuriya no Hitorigoto   47v1  NetFlix 1920x1080 AVC AAC MKV   复制磁连 ",
            extractions=[
                lx.data.Extraction(
                    extraction_class="title_zh", extraction_text="药师少女的独语"
                ),
                lx.data.Extraction(extraction_class="title_jp", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="title_romaji",
                    extraction_text="Kusuriya no Hitorigoto",
                ),
                lx.data.Extraction(extraction_class="title_en", extraction_text=""),
                lx.data.Extraction(extraction_class="year", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="season",
                    extraction_text="",
                    attributes={"season_number": ""},
                ),
                lx.data.Extraction(
                    extraction_class="episode",
                    extraction_text="47",
                    attributes={"episode_number": "47"},
                ),
                lx.data.Extraction(
                    extraction_class="fansub", extraction_text="天月搬运组"
                ),
                lx.data.Extraction(extraction_class="subtitle", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="version",
                    extraction_text="v1",
                    attributes={"version_number": "1"},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=" 极影字幕社 ★4月新番 天国大魔境 Tengoku Daimakyou 第05话 GB 720P MP4 字幕社招人内详 ",
            extractions=[
                lx.data.Extraction(
                    extraction_class="title_zh", extraction_text="天国大魔境"
                ),
                lx.data.Extraction(extraction_class="title_jp", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="title_romaji", extraction_text="Tengoku Daimakyou"
                ),
                lx.data.Extraction(extraction_class="title_en", extraction_text=""),
                lx.data.Extraction(extraction_class="year", extraction_text=""),
                lx.data.Extraction(
                    extraction_class="season",
                    extraction_text="",
                    attributes={"season_number": ""},
                ),
                lx.data.Extraction(
                    extraction_class="episode",
                    extraction_text="05",
                    attributes={"episode_number": "5"},
                ),
                lx.data.Extraction(
                    extraction_class="fansub", extraction_text="极影字幕社"
                ),
                lx.data.Extraction(
                    extraction_class="subtitle",
                    extraction_text="GB",
                    attributes={"subtitle_language": "简"},
                ),
                lx.data.Extraction(
                    extraction_class="version",
                    extraction_text="",
                    attributes={"version_number": "0"},
                ),
            ],
        ),
    ]
