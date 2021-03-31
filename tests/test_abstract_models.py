from nose.tools import eq_

from imagekit.utils import get_nonabstract_descendants

from .models import AbstractImageModel, ConcreteImageModel, ConcreteImageModelSubclass


def test_nonabstract_descendants_generator():
    descendants = list(get_nonabstract_descendants(AbstractImageModel))
    eq_(descendants, [ConcreteImageModel, ConcreteImageModelSubclass])
