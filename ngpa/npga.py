from io import TextIOWrapper


class Credit:
  def __init__(self, name: str, score: float, grade: float) -> None:
    self.name = name
    self.score = score
    self.grade = grade

  @property
  def score_grade(self) -> float:
    return self.score * self.grade

  def __eq__(self, __value: object) -> bool:
    if (not isinstance(__value, Credit)):
      return False
    return self.name == __value.name

  def __ne__(self, __value: object) -> bool:
    return not self.__eq__(__value)


def credits_from_file(f: str) -> list[Credit]:
  """takes filepath and returns a list of Credit

  Args:
      f (str): filepath

  Returns:
      list[Credit]: a list of Credits
  """
  with open(f, mode='r', encoding='utf-8'):
    return credits_from_fd(f)

def credits_from_stdin() -> list[Credit]:
  """almost the same function as `credits_from_file` except reading from stdin

  Returns:
      list[Credit]: a list of Credit
  """
  from sys import stdin
  return credits_from_fd(stdin)

def credits_from_fd(f: TextIOWrapper) -> list[Credit]:
  """helper function, takes a TextIOWrapper and returns a list of Credit

  Args:
      f (TextIOWrapper): a TextIOWrapper, eg. an opened file or stdin/stderr

  Returns:
      list[Credit]: a list of Credit
  """
  credits = []
  lines = f.readlines()
  for line in lines:
    component = line.split()
    if (len(component) == 2):
      component = ['_'] + component[:]
    assert len(component) == 3, "invalid format"
    credits.append(Credit(component[0], float(
      component[1]), float(component[2])))
  return credits


def credits_from_list(l: list) -> list[Credit]:
  """another helper function, makes a list of Credit from a list of iterable

  Args:
      l (list): a list of tuple with length at least 2

  Returns:
      list[Credit]: a list of Credit
  """
  credits = []
  for i in l:
    assert (2 <= len(i) <= 3), 'invalid format'
    if (len(i) == 2):
      name = '_'
      score, grade = i
    else:
      name, score, grade = i
    credits.append(Credit(name, score, grade))
  return credits


def gpa(gpa_list: list[Credit]) -> float:
  """takes a list of Credit and reduce it to final gpa. only works with Nanjing University

  Args:
      gpa_list (list[Credit]): a list of Credit

  Returns:
      float: gpa
  """
  return (sum([g.score_grade for g in gpa_list])) / (sum([g.grade for g in gpa_list])) / 20


def merge_gpa(list1: list[Credit], list2: list[Credit]) -> float:
  """merge two list of Credit and calculate the final gpa

  Args:
      list1 (list[Credit]): list1
      list2 (list[Credit]): list2

  Returns:
      float: gpa
  """
  return gpa(list1 + list2)


def exclude_from(gpa_list: list[Credit], exclude_list: list[Credit]) -> float:
  return gpa(gpa_list=list(filter(lambda a: a not in exclude_list, gpa_list)))
