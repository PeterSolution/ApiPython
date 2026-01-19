import importlib
import pkgutil
from typing import Any

_registry = {}

# def _load_queries():
#     """Załaduj wszystkie query handlery z folderu queries/handlers/"""
#     pkg = importlib.import_module("queries.handlers")
#     for _, name, _ in pkgutil.iter_modules(pkg.__path__):
#         try:
#             mod = importlib.import_module(f"queries.handlers.{name}")
#             # szukaj funkcji o nazwie równej nazwie modułu (lowercase)
#             func_name = name[0].lower() + name[1:]  # np. Get_all_users -> get_all_users
#             if hasattr(mod, func_name):
#                 _registry[name] = getattr(mod, func_name)
#             elif hasattr(mod, "handle"):
#                 # alternatywa: jeśli funkcja się nazywa handle
#                 _registry[name] = getattr(mod, "handle")
#         except ImportError as e:
#             print(f"Nie udało się załadować {name}: {e}")

def _load_queries():
    pkg = importlib.import_module("queries.handlers")
    # modulesInRow = importlib.import_module("queries.handlers.EntriesInRow")
    # pkg = pkg+modulesInRow <- zrobilem blad to nie dziala, przeniesiona logika pod spodem
    for _, name, _ in pkgutil.iter_modules(pkg.__path__):
        try:
            mod = importlib.import_module(f"queries.handlers.{name}")
            print(f"Ładowanie modułu: {name}")
            if hasattr(mod, "handle"):
                _registry[name] = mod.handle
        except ImportError as e:
            print(f"Nie udało się załadować {name}: {e}")
    #entries in row:
    entries_pkg = importlib.import_module("queries.handlers.EntriesInRow")
    for _, name, _ in pkgutil.iter_modules(entries_pkg.__path__):
        try:
            mod = importlib.import_module(f"queries.handlers.EntriesInRow.{name}")
            print(f"Ładowanie modułu z EntriesInRow: {name}")
            if hasattr(mod, "handle"):
                _registry[name] = mod.handle
        except ImportError as e:
            print(f"Nie udało się załadować EntriesInRow.{name}: {e}")
    #images
    images_pkg=importlib.import_module("queries.handlers.Images")
    for _, name, _ in pkgutil.iter_modules(images_pkg.__path__):
        try:
            mod = importlib.import_module(f"queries.handlers.Images.{name}")
            print(f"Ładowanie modułu z Images: {name}")
            if hasattr(mod, "handle"):
                _registry[name] = mod.handle
        except ImportError as e:
            print(f"Nie udało się załadować Images.{name}: {e}")
    

_load_queries()

def dispatchers(query_name: str, *args, **kwargs) -> Any:
    """Uruchom handler dla danego query"""
    handler = _registry.get(query_name)
    if not handler:
        raise KeyError(f"Query handler '{query_name}' not found")
    return handler(*args, **kwargs)

# from importlib import import_module
# from typing import Any

# _registry = {}

# def _load_queries():
#     """Załaduj wszystkie query handlery z folderu queries/handlers/"""
#     modules = ["Get_all_users", "Get_user_by_id"]
#     modules.append("Get_entries_pagination")
#     # modules.append("get_entry_by_id")
#     for mod_name in modules:
#         try:
#             mod = import_module(f"queries.handlers.{mod_name}")
#             func_name = mod_name.lower()
#             if hasattr(mod, func_name):
#                 _registry[mod_name] = getattr(mod, func_name)
#         except ImportError as e:
#             print(f"Nie udało się załadować {mod_name}: {e}")

# _load_queries()

# def dispatchers(query_name: str, *args, **kwargs) -> Any:
#     """Uruchom handler dla danego query"""
#     handler = _registry.get(query_name)
#     if not handler:
#         raise KeyError(f"Query handler '{query_name}' not found")
#     return handler(*args, **kwargs)