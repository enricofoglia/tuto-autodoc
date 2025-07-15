import numpy as np


def a_nice_function(
        data: np.array,
        process: bool,
        verbose: bool = False
) -> np.array:
    '''This funciton does nice things.

    A more detailed description of this function.

    Parameters
    ----------
    data : np.array
        The data to process.
    process : bool
        Whether to process the data.
    verbose : bool, optional
        Whether to print verbose output (default is False).

    Returns
    -------
    np.array
        The processed data.

    '''

    pass


def another_function(
        name: str,
        age: int,
):
    '''This function does something else.

    Parameters
    ----------
    name : str
        The name of the person.
    age : int
        The age of the person.

    Returns
    -------
    None

    '''

    pass


def _helper_function(
        value: int
) -> int:
    '''This is a helper function.

    Parameters
    ----------
    value : int
        The value to process.

    Returns
    -------
    int
        The processed value.

    '''

    return value * 2  # Just an example of processing


def public_helper():
    '''This is a public helper function.

    It can be used by other modules.

    Returns
    -------
    None

    '''
    _helper_function(42)  # Call the private helper function
