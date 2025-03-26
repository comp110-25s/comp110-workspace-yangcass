"""The dictionary function will be located"""

__author__: str = "730717480"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This just to switch the key and value in the list"""
    out: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in out:
            raise KeyError("The funtion has a error")
        else:
            out[input_dict[key]] = key
    return out


def count(words: list[str]) -> dict[str, int]:
    """This looks at the count of time a number is shown in the  value"""
    out: dict[str, int] = {}
    idx: int = 0
    while idx < len(words):
        if words[idx] in out:
            out[words[idx]] += 1
            idx += 1
        else:
            out[words[idx]] = 1
            idx += 1
    return out


def favorite_color(name_and_color: dict[str, str]) -> str:
    """Looking at which colors show up the most"""
    out: list[str] = []
    biggest: int = 0
    result_favorite_color: str = ""
    for key in name_and_color:
        out.append(name_and_color[key])
    counter = count(out)
    for key in counter:
        if counter[key] > biggest:
            biggest = counter[key]
            result_favorite_color = key
    return result_favorite_color


def bin_len(bins: list[str]) -> dict[int, set[str]]:
    """This is category the words into how long the words are in lenth"""
    out: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(bins):
        if len(bins[idx]) in out:
            out[len(bins[idx])].add(bins[idx])
        else:
            out[len(bins[idx])] = {bins[idx]}
        idx += 1
    return out
