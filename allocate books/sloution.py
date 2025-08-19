def isPossible(arr, n, m, mid):
    student_count = 1
    pages_sum = 0
    
    for pages in arr:
        if pages > mid:
            return False  # Single book > mid ? not possible
        if pages_sum + pages > mid:
            student_count += 1
            pages_sum = pages
            if student_count > m:
                return False
        else:
            pages_sum += pages
    
    return True


def findPages(arr, n: int, m: int) -> int:
    if m > n:
        return -1  # Not enough books for each student
    
    low, high = max(arr), sum(arr)
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if isPossible(arr, n, m, mid):
            result = mid
            high = mid - 1  # Try smaller maximum
        else:
            low = mid + 1   # Increase limit
    
    return result
