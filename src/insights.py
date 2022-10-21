import src.jobs as jobs


def get_unique_job_types(path):
    data = jobs.read(path)
    print(data)
    types = set()
    for job in data:
        types.add(job["job_type"])

    return list(set(types))


def filter_by_job_type(jobs, job_type):
    filtered = [i for i in jobs if i["job_type"] == job_type]
    return filtered


def get_unique_industries(path):
    data = jobs.read(path)
    industries = []
    for row in data:
        if row["industry"] != "":
            industries.append(row["industry"])

    return list(set(industries))


def filter_by_industry(jobs, industry):
    filtered = [i for i in jobs if i["industry"] == industry]
    return filtered


def get_max_salary(path):
    data = jobs.read(path)
    salaries = set()
    for row in data:
        if row["max_salary"] != "" and row["max_salary"] != "invalid":
            salary = int(row["max_salary"])
            salaries.add(salary)
    return max(salaries)


def get_min_salary(path):
    data = jobs.read(path)
    salaries = set()
    for row in data:
        if row["min_salary"] != "" and row["min_salary"] != "invalid":
            salary = int(row["min_salary"])
            salaries.add(salary)
    return min(salaries)


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError("`salary` isn`t a valid integer")
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("keys not present")
    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError("min and max salary are absent from dictionary")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary cannot be greater than max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
