#ifndef BASE_CLASS
#define BASE_CLASS

#include "SlimArray.h"
#include "MethodDescriptor.h"

class MethodDescriptor;

class BaseClass {

    public:
        virtual void elaborate( MethodDescriptor* m ) = 0;

};

template <typename T> class ObjectsManager : public BaseClass {

    protected:
        SlimArray <T*> v;

    public:
        ObjectsManager() {}
        void elaborate( MethodDescriptor* m ) {
            if (strcmp(m->getName(), "remove") == 0) {
                delete(v[m->getObjectId()]);
                v.remove(m->getObjectId());
                Serial.println("0");
            }
        }

};

static SlimArray <BaseClass*> classes;

class Register {

    public:
        
        template <typename T> static void registerClass() {
            classes.insert((BaseClass*)new T());
        }

        static void elaborate(MethodDescriptor* m) {
            for(int i = 0 ; i < classes.getSize() ; i++)
                classes[i]->elaborate(m);

            if(m != NULL) {
                delete(m);
                m = NULL;
            }
        }

};

#define REGISTER_CLASS(cls) Register::registerClass<cls>();

#endif
