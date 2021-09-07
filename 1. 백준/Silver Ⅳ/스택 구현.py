from typing import Any

class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    # 초기화
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity # 스택 크기
        self.ptr = 0 # 스택 포인터

    # 스택에 쌓여있는 데이터 개수를 반환
    def __len(self) -> int:
        return self.ptr

    # 스택이 비어있는가?
    def is_empty(self) -> bool:
        return self.ptr <= 0

    # 스택이 꽉 찼는가?
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    # value를 스택에 푸시
    def push(self, value : Any) -> None:
        if self.is_full(): # 스택이 가득 참
            raise FixedStack.Empty
        self.stk[self.ptr] = value
        self.ptr += 1

    # 스택에서 데이터를 팝
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    # 스택에서 데이터를 피크 (꼭대기를 드려다봄)
    def peek(self) -> Any:
        if self.is_empty(): # 스택이 비어있음
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    # 스택을 비움
    def clear(self) -> None:
        self.ptr = 0