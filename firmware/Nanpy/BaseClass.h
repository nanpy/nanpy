#ifndef BASE_CLASS
#define BASE_CLASS

#include "cfg.h"
#include "SlimArray.h"
#include "MethodDescriptor.h"

namespace nanpy {

    class BaseClass {

        public:
            virtual void elaborate( nanpy::MethodDescriptor* m ) = 0;
            virtual const char* get_firmware_id() = 0;

    };

    template <typename T> class ObjectsManager : public BaseClass {

        protected:
            nanpy::SlimArray <T*> v;

        public:
            ObjectsManager() {}
            void elaborate( nanpy::MethodDescriptor* m ) {
                if (strcmp(m->getName(), "remove") == 0) {
                    delete(v[m->getObjectId()]);
                    v.remove(m->getObjectId());
                    Serial.println("0");
                }
            }

    };


    class Register {
        static nanpy::SlimArray <nanpy::BaseClass*> classes;

        public:
            
            template <typename T> static void registerClass() {
                nanpy::BaseClass* obj = (nanpy::BaseClass*)new T();
                classes.insert(obj);
            }

            static nanpy::SlimArray <nanpy::BaseClass*> * get_classes() {
                return &classes;
            }

            static void elaborate(nanpy::MethodDescriptor* m) {
                for(int i = 0 ; i < classes.getSize() ; i++)
                {
                    if (strcmp(m->getClass(), classes[i]->get_firmware_id()) == 0)
                    {
                        classes[i]->elaborate(m);
                    }
                }

                if(m != NULL) {
                    delete(m);
                    m = NULL;
                }
            }

    };
}

#define REGISTER_CLASS_CONDITIONAL(cls, condition) if(condition) Register::registerClass<cls>();
#define REGISTER_CLASS(cls) REGISTER_CLASS_CONDITIONAL(cls, 1);

#endif
