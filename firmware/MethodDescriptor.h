#ifndef METHOD_DESCRIPTOR
#define METHOD_DESCRIPTOR

#include <WString.h>

class MethodDescriptor {

    private:
        char *name;
        int objid;
        char* classname;
        int n_args;
        char **stack;

    public:
        MethodDescriptor();
        int getNArgs();
        char* getClass();
        int getObjectId();
        int getInt(int n);
        float getFloat(int n);
        double getDouble(int n);
        char* getString(int n);
        char* getName();
        void returns(String& val);
        void returns(const char* val);
        void returns(int val);
        void returns(float val);
        void returns(double val);
        void returns(long val);
        ~MethodDescriptor();

};

#endif
