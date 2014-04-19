from broker import IocContainer

__author__ = 'cazamagni'


class InjectIntoConstructor(object):

    def __init__(self, *args, **kwargs):
        self.context = IocContainer()
        self.decorator_arguments = kwargs

    def __call__(self, fn):

        def executor(init_self, *args, **kwargs):
            for provider_name in self.decorator_arguments.keys():
                kwargs[provider_name] = self.context.resolve_provider(key=self.decorator_arguments.get(provider_name))

            return fn(init_self, *args, **kwargs)

        return executor