#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info on python lists
 * @p: a PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int list_len, list_alloc, idx;
	PyObject *element;

	list_len = Py_SIZE(P);
	list_alloc = ((pyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", list_alloc);

	for (idx = 0; idx < list_len; idx++)
	{
		printf("Element %d: ", idx);

		element = PyList_GetItem(p , idx);
		printf("%s\n", Py_TYPE(element)->tp_name);
	}
}
