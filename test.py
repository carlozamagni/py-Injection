import unittest
from broker import IocContainer
from injector import InjectIntoConstructor

__author__ = 'cazamagni'


class InjectorTestCase(unittest.TestCase):

    def setUp(self):
        self.broker = IocContainer()

    def test_provider_registration(self):
        self.broker.register_provider(key='foo', class_name=Foo)
        resolved = self.broker.resolve_provider('foo')
        self.assertIs(isinstance(resolved, Foo), True)

    def test_singleton_provider_registration(self):
        self.broker.register_provider(key='foo', class_name=Foo, as_singleton=True)
        resolved1 = self.broker.resolve_provider('foo')
        resolved2 = self.broker.resolve_provider('foo')

        self.assertIs(isinstance(resolved1, Foo), True)
        self.assertIs(isinstance(resolved1, Foo), True)
        self.assertIs(resolved1, resolved2)

    def test_injection(self):
        self.broker.register_provider('foo', Foo, as_singleton=False)
        argz = {'another_arg': 'asd'}
        footed = FooTed(**argz)
        self.assertIs(footed.sut_foo is not None, True)
        self.assertIs(footed.sut_arg == 'asd', True)

        footed = FooTed2(another_arg='asd', another_arg_2='asd_asd')
        self.assertIs(footed.sut_foo is not None, True)
        self.assertIs(footed.sut_arg == 'asd', True)
        self.assertIs(footed.sut_arg2 == 'asd_asd', True)

if __name__ == '__main__':
    unittest.main()


class Foo(object):
    def __init__(self):
        self.name = 'Foo instance'


class FooTed(object):
    @InjectIntoConstructor(the_required_foo='foo')
    def __init__(self, *args, **kwargs):
        self.sut_foo = kwargs.get('the_required_foo', None)
        self.sut_arg = kwargs.get('another_arg', None)


class FooTed2(object):
    @InjectIntoConstructor(the_required_foo='foo')
    def __init__(self, the_required_foo, another_arg, another_arg_2):
        self.sut_foo = the_required_foo
        self.sut_arg = another_arg
        self.sut_arg2 = another_arg_2