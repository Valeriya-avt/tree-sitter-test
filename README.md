## Задача

Реализовать инструмент, который принимает на вход директорию с Python проектом, проходится по всем его исходникам и для каждого собирает объявленные в нем функции и методы класса вместе с их длиной.

## Инструменты

 - https://tree-sitter.github.io/tree-sitter/using-parsers 
 - https://github.com/tree-sitter/py-tree-sitter 

## Начало работы

Из командной строки запустите:
```
pip3 install tree_sitter
git clone https://github.com/tree-sitter/tree-sitter-python vendor
```

## Запуск программы

Из командной строки запустите:
```
python3 work.py
```
Затем введите путь до директории, в которой хранятся файлы, которые необходимо проанализировать.
