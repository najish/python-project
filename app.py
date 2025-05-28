import importlib

def load_module(module_name):
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError as e:
        print(f"Error importing module {module_name}: {e}")
        return None


if __name__ == "__main__":
    module_name = "datastructure.stack"
    module = load_module(module_name)
    
    if module:
        # Access variables and functions from the module
        if hasattr(module, 'run'):
            module.run()
    else:
        print("Module could not be loaded.")