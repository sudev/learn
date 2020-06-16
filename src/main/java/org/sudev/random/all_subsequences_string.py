
def remove_chat_at(s: str, n: int) -> str:
    return s[:(n)] + s[(n + 1):]
###
## Below function works but prints duplicates
def all_subsequences(s: str):
    if len(s) == 0:
        return
    print(s)
    for pos in range(0, len(s)):
        all_subsequences(remove_chat_at(s, pos))

# Works well with duplicates too
def all_subsequences_recur(s: str, index: int, subs: str):
    if len(s) == index:
        print(subs)
        return
    # Include
    all_subsequences_recur(s, index + 1, subs + s[index])
    # Exclude
    all_subsequences_recur(s, index + 1, subs)


all_subsequences_recur("abcd", 0, "")