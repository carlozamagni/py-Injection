__author__ = 'cazamagni'

'''
class Broker(object):
    providers = {}

    @classmethod
    def register_provider(cls, key, class_name, as_singleton=False):
        if as_singleton:
            cls.providers[key] = class_name()
        else:
            cls.providers[key] = class_name

    @classmethod
    def resolve_provider(cls, key):
        provider = cls.providers.get(key, None)
        if provider is None:
            raise Exception('No registered provider for: %s' % key)

        if isinstance(provider, type):
            # an instance must be created
            return provider()

        # a singleton was registered
        return provider
'''


class IocContainer(object):
    """ A python singleton """

    class __impl(object):
        """ Implementation of the singleton interface """

        def __init__(self):
            self.providers = {}

        def register_provider(self, key, class_name, as_singleton=False):
            if as_singleton:
                self.providers[key] = class_name()
            else:
                self.providers[key] = class_name

        def resolve_provider(self, key):
            provider = self.providers.get(key, None)
            if provider is None:
                raise Exception('No registered provider for: %s' % key)

            if isinstance(provider, type):
                # an instance must be created
                return provider()

            # a singleton was registered
            return provider

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if SingletonBroker.__instance is None:
            # Create and remember instance
            SingletonBroker.__instance = SingletonBroker.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = SingletonBroker.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
