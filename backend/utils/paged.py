def page(num, page, counts):
    start = min(num - 1, (page-1) * counts)
    end = min(num - 1, start + counts)
    return {
        'valid': start != end,
        'start': start,
        'end': end
    }