def rev(s):
    """返回字符串的反转；当 s 为 None 时返回空字符串 ""。"""
    if s is None:
        return ""
    return s[::-1]
