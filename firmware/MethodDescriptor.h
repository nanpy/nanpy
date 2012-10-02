#ifndef METHOD_DESCRIPTOR
#define METHOD_DESCRIPTOR

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
        ~MethodDescriptor();

};




#endif
