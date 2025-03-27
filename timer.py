from time import perf_counter_ns
from typing import Any


def profiler(method):

    """
        Decorator to measure the execution time of a function.
        Use @profiler on top of the function to measure its execution time.
        This decorator will call the function, measure the time taken to execute it, and return the result.
        :param method: The function to be decorated.
        :return: The result of the function execution.
    """

    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper method to measure the time of the function.
        In the function, what is done is perf_counter_ns() is called before and after the function is executed.
        The difference between the two is calculated and formatted to be displayed in seconds, milliseconds,
        microseconds, or nanoseconds. Then prints the result and the time taken to execute the function.

        :param args: Positional arguments passed to the function being decorated.
        :param kwargs: Keyword arguments passed to the function being decorated.
        :return: The result of the function being decorated.
        """

        start = perf_counter_ns()
        result = method(*args, **kwargs)
        end = perf_counter_ns() - start
        time_len = min(9, ((len(str(end)) - 1) // 3) * 3)
        timeConv = {9: 'seconds', 6: 'milliseconds', 3: 'microseconds', 0: 'nanoseconds'}
        print(f"Result: {result} - Time: {end / (10 ** time_len)} {timeConv[time_len]}")
        return result

    return wrapper_method
