
def get_dozens(main_dozen):
    if main_dozen == 0:
        return {}
    dozens_ext = ['PRIMEIRA', 'SEGUNDA', 'TERCEIRA']
    dozens = []
    main_index = [1, 2, 3].index(main_dozen)
    dozens.append(dozens_ext[main_index])
    del dozens_ext[main_index]
    dozens.extend(dozens_ext)
    return {
        'dozen1': dozens[0],
        'dozen2': dozens[1],
        'dozen3': dozens[2]
    }
