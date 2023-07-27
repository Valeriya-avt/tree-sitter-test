from tree_sitter import Language, Parser
import os


Language.build_library(
    # Store the library in the `build` directory
    'build/my-languages.so',

    # Include one or more languages
    [
      'vendor/tree-sitter-python'
    ]
)


def get_functions_and_methods_info(node, child_count=0, class_name="", functions_and_methods=[]):
    if node.type == 'function_definition':
        # processing root_node to define function definitions
        if child_count == 0:
            function_name = node.child_by_field_name('name').text.decode('utf-8')
            function_body_length = node.child_by_field_name('body').end_point[0] - node.child_by_field_name('body').start_point[0] + 1
            functions_and_methods.append({'type': 'function', 'name': function_name, 'length': function_body_length})
            child_count = 0

        # processing node to define class mathods
        if child_count != 0:
            method_name = class_name.decode('utf-8') + '::' + node.child_by_field_name('name').text.decode('utf-8')
            method_body_length = node.child_by_field_name('body').end_point[0] - node.child_by_field_name('body').start_point[0] + 1
            functions_and_methods.append({'type': 'method', 'name': method_name, 'length': method_body_length})
            child_count -= 1
        
    if node.type == 'class_definition':
        class_name = node.child_by_field_name('name').text
        child_count = node.child_count
        
    # node children recursive traversal
    for child in node.children:
        get_functions_and_methods_info(child, child_count, class_name, functions_and_methods)

    return functions_and_methods


def process_file(file_path, parser):
    with open(file_path, 'r') as file:
        source_code = file.read()
        # parse and create AST for source code
        tree = parser.parse(bytes(source_code, 'utf-8'))
        # get AST root node and traverse
        functions_and_methods = get_functions_and_methods_info(tree.root_node)
        # print result
        print(file_path + ":")
        for item in functions_and_methods:
            if item['type'] == 'function':
                print(f"Function: {item['name']}, Lines: {item['length']}")
            elif item['type'] == 'method':
                print(f"Method: {item['name']}, Lines: {item['length']}")
        functions_and_methods.clear()
        print("\n")



def main():
    PY_LANGUAGE = Language('build/my-languages.so', 'python')

    # parser initialization
    parser = Parser()
    parser.set_language(PY_LANGUAGE)

    print("Please, write the directory name or path")
    project_directory = input()

    # walk for all files in directory
    for root, dirs, files in os.walk(project_directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_file(file_path, parser)



if __name__ == "__main__":
    main()