本项目使用[langextract](https://github.com/google/langextract)来提取动漫标题中的文本信息, 用以辅助用户进行重命名和检索.
能提取的信息如下:

- 中文标题, title_zh
- 日文标题, title_jp
- 罗马字标题, title_romaji
- 英文标题, title_en
- 年份, year
- 季度, season
- 集数, episode
- 字幕组, fansub
- 字幕语言, subtitle
- 字幕类型, subtitle_type
- 特殊, special
如 ova, 6.5
- version, version
如 v1, v2

hello test

下一步的计划:

- 异步支持,看了看好象 langextract 不支持异步, 可能和下面的计划调换
- 减少对langextract的依赖, 把项目做小
