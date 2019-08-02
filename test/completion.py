import jedi
from pprint import pprint
import vapoursynth as vs

# class M(type):
#     def prepare(name, bases, **kwds):
#         print('M.prepare()')
#         return {'dynamic_attr': 'dynamic'}

#     __prepare__ = prepare

#     def __new__(cls, name, bases, dct):
#         print('M.__new__()')
#         dct['foo'] = 'foo'
#         return super(M, cls).__new__(cls, name, bases, dct)

#     def __call__(cls, *args, **kwargs):
#         print('M.__call__()')
#         return super().__call__(*args, **kwargs)

#     def __init__(cls, name, bases, dct):
#         print('M.__init__()')
#         super().__init__(name, bases, dct)


# class A(metaclass=M):
#     def __getattr__(self, name):
#         print(f'A.__getattr__({name})')
#         raise AttributeError

#     def __getattribute__(self, name):
#         print(f'A.__getattribute__({name})')
#         return super().__getattribute__(name)

#     def __dir__(self):
#         print(f'A.__dir__()')
#         return {}

# print('test')
# a = A()
# type(a).foo = 'bar'
# print(a.foo)
# print('-' * 10)
# pprint(type(a).__dict__['foo'])

class A:
    @property
    def core(self):
        return 'core A'

    def __getattr__(self, name):
        return 'A.__getattr__()'

    def __setattr__(self, name, value):
        print(f'A.__setattr__({name})')
        super().__setattr__(name, value)

class B:
    def __getattribute__(self, name):
        print(f'B.__getattribute__({name})')
        if name != '__class__':
            return super().__getattribute__(name)
        return type('C', (), {})

def _make_C():
        dct = {"core": 'core C'}
        return type('C', (), dct)

def _make_D():
        dct = {"core": 'core D'}
        return type('C', (), dct)

C = _make_C()
D = _make_D()

c = C()
d = D()
print(c.core)
print(d.core)

# jedi.settings.no_completion_duplicates = False
# jedi.settings.use_filesystem_cache = False
# jedi.settings.fast_parser = False
# jedi.settings.dynamic_array_additions = False
# jedi.settings.dynamic_params = True
# jedi.settings.dynamic_params_for_other_modules = True
# jedi.settings.additional_dynamic_modules = [vs]
# jedi.settings.call_signatures_validity = 0.0

n = locals()
jedi.set_debug_function()
# print(vs.core.__class__.__dict__["__dict__"])
script = jedi.Interpreter('vs.core.lsmas.LWLibavSourc', [n])
# script = jedi.Interpreter('locals(', [n])
# script = jedi.Interpreter('A().dynamic_attr.', [n])
# script = jedi.Script(
# '''
# from vapoursynth import core
# core.lsmas.LWLibavSource()
# type()
# ''', 3, 25)
pprint(script.completions())
