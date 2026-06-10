def create_report(a_file):
    with a_file.open() as f:
        while True:
            line = f.readline()
            print(line)
            if not line:
                break
        