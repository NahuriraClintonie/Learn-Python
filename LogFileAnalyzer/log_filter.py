
def filter_logs(log_lines, severity):
    for log in log_lines:
        if log.startswith(severity):
            yield log
