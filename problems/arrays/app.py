import importlib.util
import sys
import os

def main():
    module_name = "count"
    module_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../python_core/iterators/count.py")
    )
    try:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec is None:
            print(f"Could not load spec for module at {module_path}")
            return
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        # Call the run function from the imported module if it exists
        if hasattr(module, 'run'):
            module.run()
        else:
            print(f"The module '{module_name}' does not have a 'run' function.")
    except Exception as e:
        print(f"Error importing or running module '{module_name}': {e}")

if __name__ == "__main__":
    main()