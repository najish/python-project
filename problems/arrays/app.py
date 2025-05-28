import importlib

def main():
    # Dynamically import the module
    module_name = "maxElement"
    try:
        module = importlib.import_module(module_name)
        # Call the run function from the imported module
        if hasattr(module, 'run'):
            module.run()
        else:
            print(f"The module '{module_name}' does not have a 'run' function.")
    except ImportError as e:
        print(f"Error importing module '{module_name}': {e}")

if __name__ == "__main__":
    main()