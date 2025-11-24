import inspect
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def evaluate_stack_frame():
    temp = inspect.stack()
    [
        print(item.function)
        for item in temp
        if temp is not None and item.function is not None
    ]


def caller_name():
    temp = inspect.stack()
    match temp:
        # We only care if there are least three elements
        case []:
            return "Matches on an empty list."
        case [x]:  # noqa: F841
            # Note, this would not match a list with more than one element or no elements
            return "Matches on exactly one and only one elemnt and binds the result to the variable 'x'."
        case [_, _, _, _, _, *_]:
            # Matches on at least three (3) elements (or more)
            return temp[2].function
        case [*elements] if len(elements) > 10:
            return "Match with Gaurd clause on bound variable."
        case _:
            return "Not Found"


def execute_and_log(func, *args, **kwargs):
    func_name = func.__name__
    result = None
    exception_occurred = False

    try:
        logging.info(f"BEGIN:\t{caller_name()}")
        logging.info(f"Executing function: '{func_name}' with args: {args}")
        result = func(*args, **kwargs)
        logging.info(f"'{func_name}' executed without errors\tResult: {result}")
    except Exception as e:
        exception_occurred = True
        logging.error(f"'{func_name}' execution error:\t {e}")
    finally:
        logging.info(f"END:\t{caller_name()}")

    return result, exception_occurred
