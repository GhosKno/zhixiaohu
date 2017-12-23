def page(num, page, counts):
    start = min(num - 1, (page-1) * counts)
    end = min(num - 1, start + counts)
    return {
        'valid':  (page-1)*counts <= num and start >= 0,
        'start': start,
        'end': end + 1
    }