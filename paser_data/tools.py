def get_satellite_dim(satellite: int) -> int:
    if satellite > 3:
        return 3
    elif satellite == 3:
        return 2
    else:
        return 0
