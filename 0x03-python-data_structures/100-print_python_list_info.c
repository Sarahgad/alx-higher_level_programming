#include <Python.h>
#include <object.h>
#include <listobject.h>
/*
 *
 *
 *
 */
void print_python_list_info(PyObject *p)
{
        long int len;
        int i;
        PyListObject *obj = (PyListObject *)p;
        
	len = PyList_Size(p);
        printf("[*] Size of the Python List = %ld\n", len);
        printf("[*] Allocated = %ld\n", obj->allocated);

        for(i = 0; i < len; ++i)
        {
        printf("Element %d: %s", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
