import progressbar


def progress_bar(max):
    bar = progressbar.ProgressBar(max_value=max)
    return bar
