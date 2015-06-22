// C extension sample with argument handling.

#include "Python.h"

// string_peek3 return dict of all unique char codes

static PyObject *
string_peek3(PyObject *self, PyObject *args) 
{
   const char *pstr;
   //PyObject* sysmod = PyImport_ImportModuleNoBlock("sys");
   //PyObject* pystdout = PyObject_GetAttrString(sysmod, "stdout");
   //PyObject* result = NULL;
   
   if (!PyArg_ParseTuple(args, "s:string_peek3", &pstr)) {
      //Py_XDECREF(result);
      //Py_XDECREF(pystdout);
      //Py_XDECREF(sysmod);   
      return NULL;
   }

   PyObject *charDict = PyDict_New();
   int i;
   for ( i = 0; i < strlen(pstr); i++ ){
      char char_display = pstr[i];
      int char_value = pstr[i];
      //result = PyObject_CallMethod(pystdout, "write", "c", char_display );

      PyObject *key = Py_BuildValue( "c", char_display );
      PyObject *value = Py_BuildValue( "i", char_value );
      if( PyDict_SetItem( charDict, key, value ) < 0 ){
          Py_XDECREF(charDict);
          //Py_XDECREF(result);
          //Py_XDECREF(pystdout);
          //Py_XDECREF(sysmod);   
          return NULL;
      } 

   }

   //Py_XDECREF(result);
   //Py_XDECREF(pystdout);
   //Py_XDECREF(sysmod);   
   //Py_XDECREF(charDict);   
   return Py_BuildValue("O", charDict);
}

// string_peek4 return list of all character codes

static PyObject *
string_peek4(PyObject *self, PyObject *args) 
{
   const char *pstr;
   PyObject* sysmod = PyImport_ImportModuleNoBlock("sys");
   PyObject* pystdout = PyObject_GetAttrString(sysmod, "stdout");
   PyObject* result = NULL;
   
   if (!PyArg_ParseTuple(args, "s:string_peek3", &pstr)) {
      Py_XDECREF(result);
      Py_XDECREF(pystdout);
      Py_XDECREF(sysmod);   
      return NULL;
   }

   PyObject *charList = PyList_New(strlen(pstr));
   int i;
   for ( i = 0; i < strlen(pstr); i++ ){
      char char_display = pstr[i];
      result = PyObject_CallMethod(pystdout, "write", "c", char_display );

      int char_value = pstr[i];

      PyObject *value = Py_BuildValue( "i", char_value );

      if( PyList_SetItem( charList, i, value ) < 0 ){
          Py_XDECREF(result);
          Py_XDECREF(pystdout);
          Py_XDECREF(sysmod);   
          Py_XDECREF( charList );
          return NULL;
      }
   }

   Py_XDECREF(result);
   Py_XDECREF(pystdout);
   Py_XDECREF(sysmod);   
   //return Py_BuildValue("O", charList);
   return charList;
}

// Module functions table.

static PyMethodDef
module_functions[] = {
   { "string_peek3", string_peek3, METH_VARARGS, "a dictionary of unique char codes from str" },
   { "string_peek4", string_peek4, METH_VARARGS, "a list of charcodes from str" },
   { NULL }
};

// This function is called to initialize the module.  It *must* be
// named initMOD, where MOD is the name of the module.
void
initext4(void)
{
   Py_InitModule3("ext4", module_functions, "A minimal module.");
}


