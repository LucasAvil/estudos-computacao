from cli.parameters import show_parameters, get_file
from features.report import create_report

if __name__ == '__main__':
    show_parameters()
    file = get_file()
    create_report(file)
