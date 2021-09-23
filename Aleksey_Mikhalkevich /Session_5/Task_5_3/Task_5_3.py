"""
1. Implement a function which receives file path
and returns names of top performer students.

2. Implement a function which receives the file path
with students info and writes CSV student information
to the new file in descending order of age.
"""

import csv


def csv_reader(path):
    """Read a csv file"""
    data = []

    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data


def get_top_performers(file_path, number_of_top_students=5):
    """
    function which receives file path and
    returns names of top performer students
    """
    data = csv_reader(file_path)

    sorted_list = sorted(data[1:], key=lambda x: float(x[-1]), reverse=True)  # sorting by marks
    result = [i[0] for i in sorted_list[:number_of_top_students]]

    return result


def sort_by_age(student_info):
    """function which sort by age"""
    sorted_list = sorted(student_info[1:], key=lambda x: float(x[1]), reverse=True)
    student_info = student_info[:1] + sorted_list
    return student_info


def save_csv(file_path, student_info):
    """
    function which receives the file path with students
    info and writes CSV student information to the
    new file in descending order of age.
    """
    student_info = sort_by_age(student_info)

    with open(file_path, "w") as file:
        writer = csv.writer(file, delimiter=",")
        for line in student_info:
            writer.writerow(line)


def main():
    path = "../data/students.csv"
    result = get_top_performers(path)
    print(result)

    data = csv_reader(path)
    file_path = "sorted_students.csv"
    save_csv(file_path, data)


if __name__ == '__main__':
    main()
