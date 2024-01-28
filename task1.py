def total_salary(path: str) -> tuple:
    """total_salary Reads files with salary data. Calculates total sum and average salary.

    :param path: path to the file with salary data
    :type path: str
    :return: Returns two values in a tuple
    :rtype: tuple
    """
    lines = []
    salary_sum = 0
    try:
        with open(path, "r", encoding="utf-8") as salary_info:
            while line := salary_info.readline():
                line = line.split(",")
                try:
                    line[1] = int(line[1])
                except ValueError:
                    print("Incorrect data format")
                lines.append(line)
            for line in lines:
                salary_sum += line[1]
            average_salary = salary_sum / len(lines)
            return (salary_sum, average_salary)
    except FileNotFoundError:
        print("File not found, please check filepath")
