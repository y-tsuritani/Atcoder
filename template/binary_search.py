def bisect_left(sequence: list, target: int, lo=0, hi=None) -> None:
    """sequence内にtargetが存在するか二分探索を実施する関数

    Args:
        sequence (list): 探索する配列
        target (int): 探索範囲
        lo (int, optional): 探索開始位置. Defaults to 0.
        hi (int, optional): 探索終了位置. Defaults to None.

    Raises:
        ValueError: 探索開始位置は0以上

    Returns:
        targetが存在した場合はTrueを返す
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(sequence)
    while lo < hi:
        mid = (lo+hi)//2
        if sequence[mid] < target: lo = mid+1
        else: hi = mid
    return lo