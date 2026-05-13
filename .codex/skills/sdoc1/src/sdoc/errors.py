class SdocError(Exception):
    """sdoc 基础异常。"""


class PathResolutionError(SdocError):
    """路径解析失败。"""


class UnsupportedLanguageError(SdocError):
    """不支持的源代码语言。"""


class ParserDependencyError(SdocError):
    """运行所需解析器依赖未安装。"""


class DocumentGenerationError(SdocError):
    """文档生成失败。"""
