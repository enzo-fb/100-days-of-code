"""API C e módulos de extensão do Python

A API C do Python permite criar módulos de extensão em C para aumentar a performance ou integrar bibliotecas nativas.
O exemplo abaixo mostra como seria a implementação de um módulo em C chamado 'modulo_soma' que soma dois números.

Para usar no Python, compile o código C e importe o módulo resultante:

import modulo_soma

print(modulo_soma.soma(2, 3))  # Saída: 5

Esses módulos são úteis para tarefas que exigem alto desempenho ou integração com código legado em C/C++.
"""

// soma.c
#include <Python.h>

static PyObject* soma(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    return PyLong_FromLong(a + b);
}

static PyMethodDef Metodos[] = {
    {"soma", soma, METH_VARARGS, "Soma dois números"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef modulo = {
    PyModuleDef_HEAD_INIT,
    "modulo_soma",
    NULL,
    -1,
    Metodos
};

PyMODINIT_FUNC PyInit_modulo_soma(void) {
    return PyModule_Create(&modulo);
}
