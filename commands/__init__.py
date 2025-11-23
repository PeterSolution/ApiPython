# from importlib import import_module
# from typing import Any

# _registry = {}

# def _load_commands():
#     """Załaduj wszystkie command handlery z folderu commands/handlers/"""
#     #users
#     modules = ["Create_user", "Update_user", "Delete_user"]
#     #entry
#     modules.append("Create_entry")
#     for mod_name in modules:
#         try:
#             mod = import_module(f"commands.handlers.{mod_name}")
#             # Pobierz funkcję z modułu
#             func_name = mod_name.lower()
#             if hasattr(mod, func_name):
#                 _registry[mod_name] = getattr(mod, func_name)
#         except ImportError as e:
#             print(f"Nie udało się załadować {mod_name}: {e}")

# _load_commands()

# def dispatchers(command_name: str, *args, **kwargs) -> Any:
#     """Uruchom handler dla danego command"""
#     handler = _registry.get(command_name)
#     if not handler:
#         raise KeyError(f"Command handler '{command_name}' not found")
#     return handler(*args, **kwargs)


import importlib
import pkgutil
from typing import Any

_registry = {}

def _load_commands():
    """Załaduj wszystkie command handlery z folderu commands/handlers/"""
    pkg = importlib.import_module("commands.handlers")
    for _, name, _ in pkgutil.iter_modules(pkg.__path__):
        try:
            mod = importlib.import_module(f"commands.handlers.{name}")
            if hasattr(mod, "handle"):
                _registry[name] = getattr(mod, "handle")
        except ImportError as e:
            print(f"Nie udało się załadować {name}: {e}")

_load_commands()

def dispatchers(command_name: str, *args, **kwargs) -> Any:
    """Uruchom handler dla danego command"""
    handler = _registry.get(command_name)
    if not handler:
        raise KeyError(f"Command handler '{command_name}' not found")
    return handler(*args, **kwargs)