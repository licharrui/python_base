from typing import List


def long_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    min_str = sorted(strs)[0]
    strs.remove(min_str)
    for i in range(len(min_str)):
        matched_str = []
        for str in strs:
            if str.startswith(min_str[: len(min_str) - i]):
                matched_str.append(str)

        if len(matched_str) == len(strs):
            return min_str[: len(min_str) - i]
    return ""


if __name__ == "__main__":
    strs = ["testfilte", "testdir", "test", "temp"]
    print(long_common_prefix(strs))
