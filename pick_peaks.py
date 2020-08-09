def pick_peaks(arr):
    # your code here
    pos = []
    peaks = []
    temp_pos = None
    temp_peak = None

    if len(arr) < 3:
        return {'pos': pos, 'peaks': peaks}
    elif len(arr) == 3:
        if arr[1] > arr[0] and arr[1] > arr[2]:
            pos.append(1)
            peaks.append(arr[1])
            return {'pos': pos, 'peaks': peaks}
    else:
        for i, val in enumerate(arr[:-2]):
            if is_max(arr[i:i + 3]):
                pos.append(i + 1)
                peaks.append(arr[i + 1])
            elif is_plateau(arr[i:i + 3], 'start'):
                temp_pos = i + 1
                temp_peak = arr[i + 1]
            elif is_plateau(arr[i:i + 3], 'end'):
                if temp_pos is not None:
                    pos.append(temp_pos)
                    peaks.append(temp_peak)
                    temp_pos = None
                    temp_peak = None

    return {'pos': pos, 'peaks': peaks}


def is_max(arr):
    """Checks an array length 3 - if the middle value is greater than the outer values, return True"""
    if len(arr) != 3:
        return

    if arr[1] > arr[0] and arr[1] > arr[2]:
        return True


def is_plateau(arr, plat_type='start'):
    """Checks for start/end of a plateau, given the plat_type passed"""

    if len(arr) != 3:
        return
    if plat_type == 'start':
        if arr[1] > arr[0] and arr[1] == arr[2]:
            # print('plat start', )
            return True
    elif plat_type == 'end':
        if arr[1] == arr[0] and arr[1] > arr[2]:
            # print('plat end')
            return True


def kata_pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            prob_peak = i
        elif arr[i] < arr[i - 1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}
