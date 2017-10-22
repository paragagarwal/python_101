import db_utils

while True:
    command = raw_input(">:")
    if command != "END":
        db_utils.run_command(command)
    else:
        break