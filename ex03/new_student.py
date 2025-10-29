from dataclasses import dataclass, field

import random
import string


def generate_id() -> str:
    """Generates a random sequence of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student class.

    Constructor required properties: name (str) and surname (str).

    Constructor optional properties: active (bool=True).

    The class creates property login (capitalized first letter of name +
    surname in lowercase) and id that is a random sequence of 15 lowercase
    letters.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Post initialisation treatments."""

        # Property login requires name and surname values to be initialised.
        # This is why it is created in a second phase.
        self.login = self.name[0].capitalize() + self.surname.lower()
