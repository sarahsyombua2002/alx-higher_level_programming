#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

void print_python_list_info(PyObject *p) {
    int size, alloc, i;
    PyObject *obj;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++) {
        printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}
